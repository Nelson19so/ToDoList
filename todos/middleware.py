from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.deprecation import MiddlewareMixin

class AutoLoginMiddleware(MiddlewareMixin):

    def process_request(self, request):
      if not request.user.is_authenticated:
        demo_user = User.objects.get(username="demoaccount")
        login(request, demo_user)