from django.urls import path

from .models import Brand
from .views import (BrandApiView, BrandRetrieveUpdateDestroyAPIView,
                    ColorApiView, ColorRetrieveUpdateDestroyAPIView,
                    CarApiView, CarRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('brand/', BrandApiView.as_view()),
    path('brand/<int:pk>/', BrandRetrieveUpdateDestroyAPIView.as_view()),

    path('color/', ColorApiView.as_view()),
    path('color/<int:pk>/', ColorRetrieveUpdateDestroyAPIView.as_view()),

    path('car/', CarApiView.as_view()),
    path('car/<int:pk>/', CarRetrieveUpdateDestroyAPIView.as_view()),
]
