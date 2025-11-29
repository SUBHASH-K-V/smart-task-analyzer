import json
from datetime import date
from typing import Any, Dict, List

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .scoring import sort_tasks_with_scores


@require_http_methods(["GET"])
def health_check(request):
    """Health check endpoint for deployment platforms."""
    return JsonResponse({
        "status": "healthy",
        "message": "Smart Task Analyzer API is running",
        "timestamp": str(date.today()),
    })


def _parse_request_body(body: bytes) -> Dict[str, Any]:
    try:
        data = json.loads(body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return {}
    if not isinstance(data, dict):
        return {}
    return data


@csrf_exempt
def analyze_tasks(request):
    """
    POST /api/tasks/analyze/

    Expects JSON body:
    {
        "tasks": [ { ...task fields... }, ... ],
        "strategy": "default" | "fastest" | "deadline"
    }

    Returns tasks sorted by score, plus the score for each task.
    """
    if request.method != "POST":
        return JsonResponse({"error": "Only POST is allowed."}, status=405)

    payload = _parse_request_body(request.body)
    raw_tasks: List[Dict[str, Any]] = payload.get("tasks") or []
    strategy: str = payload.get("strategy") or "default"

    # Ensure we always deal with a list of dicts
    tasks: List[Dict[str, Any]] = []
    for item in raw_tasks:
        if isinstance(item, dict):
            tasks.append(item)

    scored_tasks = sort_tasks_with_scores(tasks)

    # Optional alternative simple strategies applied after scoring.
    if strategy == "fastest":
        scored_tasks.sort(key=lambda t: t.get("estimated_hours", 0))
    elif strategy == "deadline":
        today = date.today()
        # Missing/invalid due dates go to the end
        def _deadline_key(t: Dict[str, Any]):
            due_raw = t.get("due_date")
            # Try to parse common string formats before falling back
            try:
                if isinstance(due_raw, str):
                    return date.fromisoformat(due_raw)
                return due_raw or today.replace(year=today.year + 50)
            except Exception:
                return today.replace(year=today.year + 50)

        scored_tasks.sort(key=_deadline_key)

    return JsonResponse({"tasks": scored_tasks})


@csrf_exempt
def suggest_tasks(request):
    """
    GET or POST /api/tasks/suggest/

    If called without body (GET), it expects nothing and just echoes an example message.
    If called with POST and a list of tasks, it returns the top 3 with text explanations.
    """
    if request.method == "GET":
        return JsonResponse(
            {
                "message": "POST a JSON body with a 'tasks' list to get top 3 suggestions.",
                "example": {
                    "tasks": [
                        {
                            "title": "Example task",
                            "due_date": str(date.today()),
                            "importance": 7,
                            "estimated_hours": 2,
                            "dependencies": [],
                        }
                    ]
                },
            }
        )

    if request.method != "POST":
        return JsonResponse({"error": "Only GET and POST are allowed."}, status=405)

    payload = _parse_request_body(request.body)
    raw_tasks: List[Dict[str, Any]] = payload.get("tasks") or []

    tasks: List[Dict[str, Any]] = []
    for item in raw_tasks:
        if isinstance(item, dict):
            tasks.append(item)

    scored_tasks = sort_tasks_with_scores(tasks)
    top_three = scored_tasks[:3]

    # Build explanations for each suggestion
    explanations: List[Dict[str, Any]] = []
    today = date.today()
    for t in top_three:
        title = t.get("title", "Untitled task")
        importance = t.get("importance", 5)
        est = t.get("estimated_hours", 1)
        due_raw = t.get("due_date")

        try:
            if isinstance(due_raw, str):
                due = date.fromisoformat(due_raw)
            else:
                due = due_raw
        except Exception:
            due = None

        if due:
            days_until = (due - today).days
            if days_until < 0:
                urgency_text = "is overdue and should be handled immediately"
            elif days_until == 0:
                urgency_text = "is due today and needs your attention now"
            elif days_until == 1:
                urgency_text = "is due tomorrow and is coming up very soon"
            else:
                urgency_text = f"is due in {days_until} days"
        else:
            urgency_text = "has no due date, so treat it as flexible but important"

        explanation = (
            f"'{title}' {urgency_text}. "
            f"It has importance {importance}/10 and is estimated at {est} hour(s). "
            f"Overall score: {t.get('score', 0):.1f}."
        )
        explanations.append({"task": t, "reason": explanation})

    return JsonResponse({"suggestions": explanations})

