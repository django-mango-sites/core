from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from django.core.exceptions import MiddlewareNotUsed
from django.utils.encoding import DjangoUnicodeDecodeError
from django.utils.html import strip_spaces_between_tags as minify_html


class LoginCheckMiddleware:

    available_paths = [
        '/admin/',
    ]

    def __init__(self, get_response):
        self.get_response = get_response

        if not settings.LOGIN_CHECK_ENABLED:
            raise MiddlewareNotUsed

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path in self.available_paths:
            return redirect(reverse('account:login'))

        response = self.get_response(request)

        return response


class HTMLMinifyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

        if not settings.HTML_MINIFY_ENABLED:
            raise MiddlewareNotUsed

    def __call__(self, request):
        response = self.get_response(request)

        if response.has_header('Content-Type') and 'text/html' in response['Content-Type']:

            try:
                response.content = minify_html(response.content.decode('utf-8', errors='ignore').strip())
                response['Content-Length'] = str(len(response.content))

            except DjangoUnicodeDecodeError:
                pass

        return response