from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView ,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from borrow.models import Borrow

from.forms import userUpdateForm

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        borrowed_books = Borrow.objects.filter(
            user =self.request.user,
            returned = False
        ).select_related("book")

    
        context["borrowed_books"] = borrowed_books
        return context

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = userUpdateForm
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self,):
        return self.request.user

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/registration.html', {'form': form})

class userLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True