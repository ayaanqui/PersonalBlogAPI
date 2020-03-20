from django.urls import path
from tags.api.views import TagListAPIView, TagDetailAPIView

urlpatterns = [
    path('', TagListAPIView.as_view()), # Show all tags
    path('<int:id>/', TagDetailAPIView.as_view()), # Show specific tag
]