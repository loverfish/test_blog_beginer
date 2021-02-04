from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        print(kwargs)
        return super().get_context_data(**kwargs)
