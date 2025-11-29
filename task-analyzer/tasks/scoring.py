from __future__ import annotations

from datetime import date, datetime
from typing import Any, Dict


def _parse_due_date(value: Any) -> date | None:
    """
    Accepts a date or a string and tries to convert it to a date object.
    Returns None if parsing fails.
    """
    if value is None:
        return None

    if isinstance(value, date) and not isinstance(value, datetime):
        return value

    if isinstance(value, datetime):
        return value.date()

    if isinstance(value, str):
        # Try common formats; keep it simple for this assignment.
        for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y", "%Y/%m/%d"):
            try:
                return datetime.strptime(value, fmt).date()
            except ValueError:
                continue
    return None


def calculate_task_score(task_data: Dict[str, Any]) -> float:
    """
    Calculates a priority score for a single task dictionary.

    The scoring strategy is:
    - Urgency (time until due date) has the highest impact.
    - Importance is strongly weighted.
    - Effort gives a small bonus for "quick wins".
    - Unmet dependencies slightly reduce the score.

    Higher score = Higher priority.
    """
    score: float = 0

    # --- 1. Urgency Calculation ---
    today = date.today()
    due = _parse_due_date(task_data.get("due_date"))

    if due is not None:
        days_until_due = (due - today).days

        if days_until_due < 0:
            # OVERDUE! Huge priority boost
            score += 100
        elif days_until_due <= 1:
            score += 70
        elif days_until_due <= 3:
            score += 50
        elif days_until_due <= 7:
            score += 25
        else:
            # Far in the future, small baseline
            score += 5
    else:
        # Missing due date: treat as medium-term with a neutral baseline
        score += 20

    # --- 2. Importance Weighting ---
    importance = task_data.get("importance")
    try:
        importance_val = int(importance)
    except (TypeError, ValueError):
        importance_val = 5  # Sensible default if missing/invalid

    # Clamp to 1-10
    importance_val = max(1, min(importance_val, 10))
    score += importance_val * 5

    # --- 3. Effort (Quick wins logic) ---
    est_hours = task_data.get("estimated_hours")
    try:
        est_hours_val = float(est_hours)
    except (TypeError, ValueError):
        est_hours_val = 1.0

    if est_hours_val <= 0:
        est_hours_val = 0.5

    # Prefer quick tasks: if estimated < 2 hours give a bonus,
    # else apply a small penalty so extremely large tasks don't dominate.
    if est_hours_val < 2:
        score += 10  # Small bonus for quick tasks
    elif est_hours_val > 8:
        score -= 5

    # --- 4. Dependencies Handling ---
    # Expect dependencies as list of IDs, and possibly a field telling us which ones are completed.
    dependencies = task_data.get("dependencies") or []
    completed_deps = set(task_data.get("completed_dependencies") or [])

    try:
        dep_count = len(dependencies)
    except TypeError:
        dep_count = 0
        dependencies = []

    if dep_count:
        unmet = [d for d in dependencies if d not in completed_deps]
        if unmet:
            # If there are unmet dependencies, slightly reduce score:
            score -= 10

    return score


def sort_tasks_with_scores(tasks: list[Dict[str, Any]]) -> list[Dict[str, Any]]:
    """
    Returns a new list of tasks sorted by descending score.
    Each task dict will be augmented with a 'score' field.
    """
    enriched = []
    for task in tasks:
        task_copy = dict(task)
        task_copy["score"] = calculate_task_score(task_copy)
        enriched.append(task_copy)

    # Higher score first
    enriched.sort(key=lambda t: t["score"], reverse=True)
    return enriched



