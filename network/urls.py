from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusinessUnitViewSet, ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

app_name = 'network'

router = DefaultRouter()
router.register(r'businessunits', BusinessUnitViewSet)

urlpatterns = [
    # BusinessUnit
    path('', include(router.urls)),

    # Product
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
]
