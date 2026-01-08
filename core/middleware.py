from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse

class AuthRequiredMiddleware:
    """
    Middleware that requires a user to be authenticated to view any page,
    except for the login/signup/reset pages.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # List of paths that are accessible without login
        self.exempt_starts = [
            '/accounts/', 
            '/admin/', 
            '/static/', 
            '/media/'
        ]

    def __call__(self, request):
        if not request.user.is_authenticated:
            path = request.path_info
            if not any(path.startswith(prefix) for prefix in self.exempt_starts):
                return redirect(settings.LOGIN_URL)
        
        response = self.get_response(request)
        return response
