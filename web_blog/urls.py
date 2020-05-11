"""web_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Blog.views import about_blog, post_listview, post_detailview, post_createview, like_post, userPage
from users.views import register_view, profile
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('nishant/admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', post_listview.as_view(), name="Blog-home"),
    path('likes/', like_post, name="Blog-like"),
    path('post/<int:pk>/', post_detailview.as_view(), name="Blog-detail"),
    path('user/<str:username>/', userPage.as_view(), name="User-page"),
    path('about/', about_blog, name="Blog-about"),
    path('register/', register_view, name="Register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="Login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="Logout"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name="PasswordReset"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name="password_reset_done"),
    path('profile/', profile, name="Profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
