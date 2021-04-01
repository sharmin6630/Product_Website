from django.shortcuts import render
from django.http import HttpResponse
from .models import products
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.conf import settings
# Create your views here.

def home(request):
    product1 = products("Amazon Basics Kids Ultra-Soft Micromink Sherpa Blanket", "https://images-na.ssl-images-amazon.com/images/I/81ET5Y7uyKL._AC_SL1500_.jpg", 
    "https://tinyl.io/3qBk", 2026.03)
    product2 = products("Sony MDRNC13 Noise-Canceling Headphones", "https://images-na.ssl-images-amazon.com/images/I/51EbIJypsgL._AC_SL1000_.jpg",
     "https://tinyl.io/3qBo", 16185)
    product3 = products("Bose QuietComfort 20 Acoustic Noise Cancelling Headphones", "https://images-na.ssl-images-amazon.com/images/I/51e1Xd%2B4ddL._AC_SL1500_.jpg",
     "https://tinyl.io/3qBs", 20667)
    product4 = products("Bose QuietComfort 35", "https://images-na.ssl-images-amazon.com/images/I/81%2BjNVOUsJL._AC_SL1500_.jpg", 
    "https://tinyl.io/3qBu", 16810)
    product5 = products("New Apple iPad (10.2-inch, Wi-Fi, 32GB)", "https://images-na.ssl-images-amazon.com/images/I/71xP2cB-HjL._AC_SL1500_.jpg",
     "https://tinyl.io/3qBz", 34000)
    product6 = products("Belkin Lightning Audio + Charge", "https://images-na.ssl-images-amazon.com/images/I/41xAbswN2aL._AC_SL1000_.jpg",
     "https://tinyl.io/3qC3", 3237)
    product7 = products("Amazon Basics 5-Way Multi Headphone", "https://images-na.ssl-images-amazon.com/images/I/61DBGcrKMhL._AC_SL1500_.jpg",
     "https://tinyl.io/3qC4", 1000)
    product8 = products("Samsung Galaxy Watch 3", "https://images-na.ssl-images-amazon.com/images/I/81Iu41zFPwL._AC_SL1500_.jpg",
     "https://tinyl.io/3qCB", 30000)
    product9 = products("Casio F91W-1 Classic Resin Strap", "https://images-na.ssl-images-amazon.com/images/I/91JegIxgwML._AC_SL1500_.jpg", 
    "https://tinyl.io/3qC9", 1500)
    product10 = products("New Apple Watch Series 6 ", "https://images-na.ssl-images-amazon.com/images/I/71bf9IpGjtL._AC_SL1500_.jpg",
     "https://tinyl.io/3qC8", 60000)
    
    product_list = [product1, product2, product3, product4, product5, product6, 
    product7, product8, product9, product10]
    return render(request, 'home.html', {'product_list': product_list})