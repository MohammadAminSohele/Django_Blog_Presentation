from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect

from blog.models import Article
from .models import User
from .forms import ProfileForm

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .mixins import (
    FieldsMixin,
    FormValidMixin,
    Author_Access_Mixin,
    SuperUser_Access_Mixin,
    AuthorsAccessMixin,
)

def LogoutView(request):
    logout(request)
    return redirect('account:login')
# Create your views here.
class ArticleList(AuthorsAccessMixin,ListView):
    template_name="registration/home.html"
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)

class ArticleCreate(AuthorsAccessMixin,FieldsMixin,FormValidMixin, CreateView):
    model = Article
    template_name = "registration/article-create-update.html"

class ArticleUpdate(Author_Access_Mixin,FieldsMixin,FormValidMixin,UpdateView):
     model = Article
     template_name = "registration/article-create-update.html"

class Article_Delete(SuperUser_Access_Mixin,DeleteView):
    model=Article
    success_url=reverse_lazy('account:home')
    template_name="registration/article_confirm_delete.html"

class Profile(LoginRequiredMixin,UpdateView):
     model = User
     template_name = "registration/profile.html"
     form_class=ProfileForm
     success_url=reverse_lazy('account:profile')
     def get_object(self):
         return User.objects.get(pk=self.request.user.pk)
     def get_form_kwargs(self):
        kwargs = super(Profile,self).get_form_kwargs()
        kwargs.update(
            {
                'user':self.request.user
            }
        )
        return kwargs
     
class Login(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_superuser:
            return reverse_lazy('account:home')
        else:
            return reverse_lazy('account:profile')