from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all().order_by('-published_date') 
    serializer_class = BlogPostSerializer


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

def index(request):
    return render(request, 'index.html')