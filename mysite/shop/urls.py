from django.urls import path
from .views import *


urlpatterns = [
    path('user_profiles/', UserProfileViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='user_profile_list'),
    path('user_profiles/<int:pk>/', UserProfileViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_profile_detail'),


    path('categories/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='category_list'),
    path('categories/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),


    path('products/', ProductViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='product_list'),
    path('products/<int:pk>/', ProductViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_detail'),


    path('reviews/', ReviewViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='review_list'),
    path('reviews/<int:pk>/', ReviewViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='review_detail'),


    path('ratings/', RatingViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='ratings_list'),
    path('ratings/<int:pk>/', RatingViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='ratings_detail'),


    path('product_photos/', ProductPhotosViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='product_photos_list'),
    path('product_photos/<int:pk>/', ProductPhotosViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_photos_detail'),


    path('favorites/', FavoriteViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='favorites_list'),
    path('favorites/<int:pk>/', FavoriteViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='favorites_detail'),


    path('baskets/', BasketViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='baskets_list'),
    path('baskets/<int:pk>/', BasketViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='baskets_detail'),
]
