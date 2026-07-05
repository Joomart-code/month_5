from django.urls import path
from .views import *

urlpatterns = [
    path('categories/',category_list_api_view),
    path('categories/<int:id>/',category_detail_api_view),
    path('product/',product_list_api_view),
    path('product/<int:id>/',product_detail_api_view),
    path('reviews/',review_list_api_view),
    path('reviews/<int:id>/',review_detail_api_view),
]
