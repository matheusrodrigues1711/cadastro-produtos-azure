from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='produto_list'),
    path('novo/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('<int:pk>/editar/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('<int:pk>/excluir/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
]