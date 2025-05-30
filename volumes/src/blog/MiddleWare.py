from .models import IP_Address

class Save_IpAddress_Middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        try:
            IP_address=IP_Address.objects.get(IP_address=ip)
        except IP_Address.DoesNotExist:
            IP_address=IP_Address(IP_address=ip)
            IP_address.save()
        request.user.IP_address = IP_address
        
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response