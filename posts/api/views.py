import math

from django.db.models import Q

from rest_framework.generics import ListAPIView, RetrieveAPIView
from posts.api.serializers import PostSummarySerializer, PostDetailSerializer
from posts.models import Post
from tags.models import Tag

class PostListAPIView(ListAPIView):
    serializer_class = PostSummarySerializer
    queryset = Post.objects.all()

    def paginationAlgo(self, qs, limit, pageNum):
        maxPages = math.ceil(qs.count() / limit) # Gives us the max amount each page can have
        if pageNum > maxPages:
            return qs

        min = (pageNum-1) * limit
        max = min + limit
        return qs[min : max]

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
        
        orderBy = self.request.GET.get('order_by')
        if orderBy is not None:
            if (orderBy == 'published'):
                qs = qs.order_by('published').reverse()

        limit = self.request.GET.get('limit')
        if limit is not None and limit.isnumeric():
            limit = int(limit)

            # Pagination -- works only if limit is provided
            page = self.request.GET.get('page')
            if page is not None and page.isnumeric():
                page = int(page)
                qs = self.paginationAlgo(qs, limit, page)
            else:
                qs = qs[:limit]

        return qs


class PostDetailAPIView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'