from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('search/', views.catalog, name="search"),
    path('add/', views.add, name="add"),
    path('<slug:category_slug>/', views.catalog, name="index"),
    path('product/<int:product_id>/', views.product, name="product"),
]

