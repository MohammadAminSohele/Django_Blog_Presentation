from django.shortcuts import render
from django.views.generic import ListView

from .models import Article

# Create your views here.

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
    