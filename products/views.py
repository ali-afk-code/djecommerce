from django.shortcuts import render, get_object_or_404
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin
# def homeView(request):
#       context={
#           'items':Item.objects.all()
#       }
#     return render(request, "home-page.html")


class HomeView(LoginRequiredMixin,ListView):
    template_name = "home-page.html"
    model = Item
    login_url = 'account_login'
    # context_object_name= 'items' instead  we will use object_list


class ProductView(LoginRequiredMixin,DetailView):
    model = Item
    template_name = 'product-page.html'
    login_url = 'account_login' # new


def checkoutView(request):
    return render(request, "checkout-page.html")


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0,
                 'get_cart_items': 0,  # if user is not logged in it will describe empty list and $0
                 }
    context = {'items': items,
               'order': order}  # this for get_cart_total and get_cart_items
    return render(request, 'cart.html', context)


class Search(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'search.html'
    login_url = 'account_login'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Item.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
class Smartphones(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'smartphones.html'
    login_url = 'account_login'
    def get_queryset(self):
        return Item.objects.filter(
            Q(category__icontains="smartphones")
        )
class Tablets(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'tablets.html'
    login_url = 'account_login'
    def get_queryset(self):
        return Item.objects.filter(
            Q(category__icontains="tablets") )
class Headphones(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'headphones.html'
    login_url = 'account_login'
    def get_queryset(self):
        return Item.objects.filter(
            Q(category__icontains="headphones"))
