from post_app.serializer import PostSerializer
from post_app.models import Post
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class PostList(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer