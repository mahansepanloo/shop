from django.urls import path
from . import views
urlpatterns = [
    path('save-orders/', views.save_orders_to_file),
    path('create/',views.CreateOrderView.as_view())

]
