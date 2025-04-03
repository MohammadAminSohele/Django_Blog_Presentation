from django.urls import path
from django.contrib.auth import views

from .views import (
    ArticleList,
    ArticleCreate,
    ArticleUpdate,
    Article_Delete,
    LogoutView,
    Profile,
    Login
)

app_name = 'account'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/',LogoutView, name='logout'),

    # path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns += [
	path('', ArticleList.as_view(), name="home"),
	path('article/create', ArticleCreate.as_view(), name="ArticleCreate"),
	path('article/update/<int:pk>', ArticleUpdate.as_view(), name="ArticleUpdate"),
	path('article/delete/<int:pk>', Article_Delete.as_view(), name="Article_Delete"),
	path('profile/', Profile.as_view(), name="profile"),
]
