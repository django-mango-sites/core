from django.views.decorators.http import require_GET
from django.http import HttpResponse


@require_GET
def robots_txt(request):
    lines = [
        'User-Agent: *',
        'Disallow: /admin/',
        'Disallow: /account/',
    ]

    return HttpResponse('\n'.join(lines), content_type='text/plain')