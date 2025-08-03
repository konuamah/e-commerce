from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product, CartItem, Order
from .serializers import ProductSerializer, CartItemSerializer, OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        # Simulate checkout: calculate total from cart items
        cart_item_ids = request.data.get('items', [])
        items = CartItem.objects.filter(id__in=cart_item_ids)

        total = sum(item.product.price * item.quantity for item in items)
        order = Order.objects.create(total_amount=total)
        order.items.set(items)
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
