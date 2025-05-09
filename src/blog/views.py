from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView
from django.db.models import Q

from .models import Article,Catagory
from account.models import User
from account.mixins import Author_Access_Mixin

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

class Search_List(ListView):
    paginate_by=1
    template_name='blog/Search_List.html' 

    def get_queryset(self):
        global query
        query = self.request.GET.get('q')
        return Article.objects.filter(Q(description__icontains = query ) | Q(title__icontains = query ) ).published()
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["search"] = query
        return context
    
class ArticleList(ListView):
    paginate_by = 3
    template_name = 'blog/article_list.html'
    def get_queryset(self):
        global articles
        articles=Article.objects.published()
        return articles
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["object_list"] = articles
        return context

class ArticleDetail(DetailView):
    def get_object(self):
        slug=self.kwargs.get('slug')
        article= get_object_or_404(Article.objects.published(),slug=slug)
        ip_address = self.request.user.IP_address
        if not ip_address in article.hits.all():
            article.hits.add(ip_address)
        return article

class ArticlePreView(Author_Access_Mixin,DetailView):
    def get_object(self):
        pk=self.kwargs.get('pk')
        return get_object_or_404(Article,pk=pk)
    
class Articles_By_catagory(ListView):
    paginate_by=3
    template_name='blog/Show_articles_by_Catagory.html'
    def get_queryset(self):
        global catagory
        slug=self.kwargs.get('slug')
        catagory=get_object_or_404(Catagory.objects.active(),slug=slug,status=True)
        return catagory.articles.published()
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["Catagory"] = catagory
        return context
    