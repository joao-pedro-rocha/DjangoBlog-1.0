from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    
    # Conecta a url que cai na lista de posts
    # quando não houver argumento na url
    path('', views.PostListView.as_view(), name = 'list'),
    
    # Conecta a url que cai direto no post argumentado na url
    path('<slug:slug>/', views.PostDetailView.as_view(), name = 'detail'),
]
