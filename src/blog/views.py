from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView

from .models import Article
from account.models import User

# Create your views here.

class AuthorList(ListView):
    paginate_by=3
    template_name='blog/Show_articles_by_author.html' 
    def get_queryset(self):
        global author
        username=self.kwargs.get('username')
        author=get_object_or_404(User,username=username)
        return author.articles.published()
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["author"] = author
        return context
    
class ArticleList(ListView):
    paginate_by=3
    template_name='home_page.html'
    def get_queryset(self):
        global articles
        articles=Article.objects.published()
        return articles
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["Article"] = articles
        return context

class ArticleDetail(DetailView):
    def get_object(self):
        slug=self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(),slug=slug)
    