from rest_framework.generics import ListAPIView, RetrieveAPIView

from tags.models import Tag
from tags.api.serializers import TagSerializer


class TagListAPIView(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

class TagDetailAPIView(RetrieveAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    lookup_field = 'id'