from django.urls import path
from .views import ArticleListView , ArticleDetailView , ArticlesPageSettingsView

urlpatterns = [
    path("" , ArticleListView.as_view() , name = "article-list") ,
    path("settings/" , ArticlesPageSettingsView.as_view() , name = "articles-settings") ,
    path("<str:slug>/" , ArticleDetailView.as_view() , name = "article-detail") ,
]