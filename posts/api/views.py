import math

from django.db.models import Q

from rest_framework.generics import ListAPIView, RetrieveAPIView
from posts.api.serializers import PostSummarySerializer, PostDetailSerializer
from posts.models import Post
from tags.models import Tag
from posts.api.pagination import SmallResultsSetPagination


class PostListAPIView(ListAPIView):
    serializer_class = PostSummarySerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get('q')

        if query is not None:
            tagSearch = Tag.objects.all()
            tagSearch = tagSearch.filter(name__icontains = query).first()

            qs = qs.filter(
                Q(title__icontains = query) |
                Q(content__icontains = query) |
                Q(tags = tagSearch)
            ).distinct()
        
        # Pagination - sets pagination_class to show pagination view
        # provided pagination is True
        paginationStatus = self.request.GET.get('pagination')
        if paginationStatus is not None and paginationStatus == 'True':
            self.pagination_class = SmallResultsSetPagination

        orderBy = self.request.GET.get('order_by')
        if orderBy is not None and orderBy == 'published':
            qs = qs.order_by('published').reverse()

        limit = self.request.GET.get('limit')
        if limit is not None and limit.isnumeric():
            qs = qs[:int(limit)]

        return qs


class PostDetailAPIView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'