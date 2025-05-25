from django.urls import path

from .views import (
    ArticleList,
    ArticleCreate,
    ArticleUpdate,
    Article_Delete,
    Profile,
)

app_name = 'account'

urlpatterns = [
	path('', ArticleList.as_view(), name="home"),
	path('article/create', ArticleCreate.as_view(), name="ArticleCreate"),
	path('article/update/<int:pk>', ArticleUpdate.as_view(), name="ArticleUpdate"),
	path('article/delete/<int:pk>', Article_Delete.as_view(), name="Article_Delete"),
	path('profile/', Profile.as_view(), name="profile"),
]
