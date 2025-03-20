from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.BlogPostListCreate.as_view(), name='blogpost_view_create'),
]