from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet

router = DefaultRouter()
router.register('cart', CartViewSet)
# router.register('cartitems', CartitemsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]