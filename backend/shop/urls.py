from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartItemViewSet, OrderViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('cart', CartItemViewSet)
router.register('checkout', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
