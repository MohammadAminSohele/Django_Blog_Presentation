from django.urls import path

from .import views

app_name='blog'

urlpatterns = [
    path('',views.ArticleList.as_view(),name='home_page'),
    path('<slug:slug>',views.ArticleDetail.as_view(),name='ArticleDetail'),
    path('preview/<int:pk>',views.ArticlePreView.as_view(),name='ArticlePreView'),
    path('author/<slug:username>',views.AuthorList.as_view(),name='AuthorList'),
    path('catagory/<slug:slug>',views.Articles_By_catagory.as_view(),name='Articles_By_catagory'),
]
