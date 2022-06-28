from .models import Post
from .serializers import PostSerializer
from rest_framework import generics

# Create your views here.
class Posts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer