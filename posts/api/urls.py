from django.urls import path
from posts.api.views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    path('', PostListAPIView.as_view()),
    path('<str:slug>/', PostDetailAPIView.as_view())
]