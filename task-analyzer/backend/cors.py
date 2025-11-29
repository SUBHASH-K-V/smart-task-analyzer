from __future__ import annotations

from typing import Callable

from django.http import HttpRequest, HttpResponse


class SimpleCORSMiddleware:
    """
    Very small CORS middleware used to ensure development requests from the
    frontend (e.g. http://127.0.0.1:5500) to http://127.0.0.1:8000 succeed.

    It unconditionally allows all origins and handles OPTIONS preflight
    requests for API endpoints.
    """

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        # Handle preflight
        if request.method == "OPTIONS":
            response = HttpResponse()
        else:
            response = self.get_response(request)

        origin = request.headers.get("Origin")
        if origin:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Vary"] = "Origin"

        response.headers.setdefault(
            "Access-Control-Allow-Methods", "GET, POST, OPTIONS"
        )
        response.headers.setdefault(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        response.headers.setdefault("Access-Control-Allow-Credentials", "true")

        return response


