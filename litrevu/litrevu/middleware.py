from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMiddleware:
    """
    Redirige les utilisateurs non authentifiés vers la page de connexion.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            not request.user.is_authenticated
            and not request.path.startswith(reverse("login"))
            and not request.path.startswith(reverse("signup"))
        ):
            return redirect("login")
        response = self.get_response(request)
        return response
