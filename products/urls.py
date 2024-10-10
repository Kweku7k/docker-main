from django.urls import path

# from admin.products.views import ProductViewSet
from .views import ProductViewSet, UserAPIView

urlpatterns = [
    path('products/', ProductViewSet.as_view({
        # method:function
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', UserAPIView.as_view())
]
