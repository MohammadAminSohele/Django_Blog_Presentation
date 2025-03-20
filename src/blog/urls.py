from django.urls import path

from .import views

app_name='blog'

urlpatterns = [
    path('',views.ArticleList.as_view(),name='home_page'),
    path('<slug:username>',views.AuthorList.as_view(),name='AuthorList'),
    path('<slug:slug>',views.ArticleDetail.as_view(),name='ArticleDetail'),
]
