from django.urls import path
from . import views

urlpatterns = [
    path('create_publication/', views.create_publication_view, name='create_publication'),
    path('create_article/', views.create_article_view, name='create_article'),
    path('get_publications/', views.get_publications_view, name='get_publications'),
    path('get_articles/', views.get_articles_view, name='get_articles'),
]
