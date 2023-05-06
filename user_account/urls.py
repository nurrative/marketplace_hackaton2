from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import  RegisterUserView, ActivationView, LogoutView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    path('logout/', LogoutView.as_view()),

]