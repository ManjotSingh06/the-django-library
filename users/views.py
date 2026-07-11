from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from borrow.models import Borrow

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