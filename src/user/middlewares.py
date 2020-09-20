from time import time
from user.models import GclidClick


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print('Before View Func')
        start = time()
        response = self.get_response(request)
        end = time()
        print(f'Path: {request.path}, Time: {end - start}')
        print('After View Func')

        # Code to be executed for each request/response after
        # the view is called.

        return response

class GoogleLead:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        gclid = request.GET.get('gclid')
        if gclid:
            # if not GclidClick.objects.filter(value=gclid).exists():
            #     GclidClick.objects.create(value=gclid)
            instance, created = GclidClick.objects.get_or_create(value=gclid)

        response = self.get_response(request)
        return response
