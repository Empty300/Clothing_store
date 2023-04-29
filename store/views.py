from django.contrib.auth.models import User
from django.views.generic import ListView


class IndexView(ListView):
    template_name = 'store/index_page.html'
    model = User
