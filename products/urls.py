from django.urls import path
from .views import HomeView,checkoutView,ProductView,cart,Search,Smartphones,Headphones,Tablets
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('checkout/',checkoutView,name='checkout'),
    path('products/<slug>/',ProductView.as_view(),name = 'product'),
    path('add-to-cart/',cart,name='cart'),
    path('search/',Search.as_view(),name='search'),
    path('smartphones/',Smartphones.as_view(),name='smart'),
    path('tablets/',Tablets.as_view(),name='tablets'),
    path('headphones/',Headphones.as_view(),name='head'),
]