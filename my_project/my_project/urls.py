"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from my_project.news import views as zcv
from my_project.weather import views as zdv
from my_project.accounts import views as zev
from my_project.posts import views as zpv

from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth import views as auth_views

from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/',zcv.news,name='news'),
    path('category/<str:tag>', zcv.category, name='category'),
    path('about/',zcv.about,name='about'),
    path('weather/',zdv.weather,name='weather'),
    path('delete_city/<city_name>/',zdv.delete_city,name='delete_city'),
    path('', include('django.contrib.auth.urls')),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', auth_views.LoginView.as_view(),name='home'),
    path('signup/',zev.signup,name='signup'),
    path('editorial/',zcv.editorial,name='editorial'),
    path('articles/',zcv.articles,name='articles'),
    path('falseuser/',zcv.falseuser,name='falseuser'),
    path('delete_article/<article_name>/',zcv.delete_article,name='delete_article'),
    path('oauth/', include('social_django.urls', namespace='social')),



    path('upload/', zpv.Blog.as_view(), name='upload'),
    path('display/', zpv.BlogView2, name='display'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)