from .views import (
    page_404,
    ContactView,
    Messages,
    DetailView,
    NewsUpdateView,
    localNews,
    abroadNews,
    techNews,
    sportNews,
)
from django.urls import path

app_name = "news"
urlpatterns = [
    path("abroad-news/", abroadNews, name="abroad"),
    path("local-news/", localNews, name="local"),
    path("technalogy-news/", techNews, name="tech"),
    path("sport-news/", sportNews, name="sport"),
    path("404/", page_404, name="404"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("messages/", Messages, name="messages"),
    path("<slug:news>/", DetailView.as_view(), name="detail"),
    path("<slug>/edit/", NewsUpdateView.as_view(), name="update"),
]
