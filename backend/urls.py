from django.urls import path
from . import views
from . import template


#URL Conf
urlpatterns = [
    path('vendors/',views.VendorList.as_view()),
    path('vendors/<int:pk>/',views.VendorDetail.as_view()),
    path('vendors/<int:vendor_id>/performance/',views.vendor_performance,name="vendor_performance"),
    path('purchase_orders/',views.PurchaseOrderList.as_view()),
    path('purchase_orders/<int:pk>/',views.PurchaseOrderDetail.as_view()),
   
]
