from django.contrib import admin
from django.urls import path, include

urlpatterns = [
      path('', include('django_prometheus.urls')),  
    path('admin/', admin.site.urls),
    path('api/', include('shop.urls')),  # ⬅️ Add this line
]
