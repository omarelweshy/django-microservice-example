import requests
from rest_framework.response import Response
from rest_framework import status


def validate_user_token(view_func):
    def _wrapped_view(self, request, *args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION", "")

        user_service_url = "http://127.0.0.1:8000/auth/validate"
        response = requests.get(user_service_url, headers={"Authorization": token})

        if response.status_code == status.HTTP_200_OK:
            return view_func(self, request, *args, **kwargs)
        else:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
            )

    return _wrapped_view
