from django.urls import path
from .views import *

urlpatterns = [
    path('categories/',CatrgoryListCreateAPIView.as_view()),
    path('categories/<int:id>/',CategoryDetailAPIView.as_view()),
    path('product/',ProductListCreateAPIView.as_view()),
    path('product/<int:id>/',ProductDetailAPIView.as_view()),
    path('reviews/', ReviewListCreateAPIView.as_view()),
    path('reviews/<int:id>/',ReviewDetailAPIView.as_view()),
]
