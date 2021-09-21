from django.shortcuts import render

# DetailView para mostrar um post
# ListView para listar vários posts
from django.views.generic import DetailView, ListView

# Para herdar classes
from .models import Post

# Create your views here.
# Herda ListView
class PostListView(ListView):
    model = Post
    
# Herda DetailView
class PostDetailView(DetailView):
    model = Post
