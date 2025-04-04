from django.utils import translation

class AdminLocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            translation.activate('ar')
            request.LANGUAGE_CODE = 'ar'
        response = self.get_response(request)
        return response