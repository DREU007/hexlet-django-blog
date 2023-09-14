from django.urls import path

from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.Index.as_view(), name='articles'),
    path('<str:tags>/<int:article_id>', views.Index.article, name='article'),
]
