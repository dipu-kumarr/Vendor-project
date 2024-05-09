
from rest_framework import generics,permissions
from rest_framework .generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .serializers import VendorSerializers,VendorDetailSerializers,PurchaseOrderSerializers,PurchaseOrderDetailSerializers
from . import models
from . models import Vendor,PurchaseOrder


# Create your views here.
class VendorList(ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializers
    permission_classes = [permissions.IsAuthenticated]


class VendorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorDetailSerializers
    # permission_classes = [permissions.IsAuthenticated]


class PurchaseOrderList(ListCreateAPIView):
    queryset = models.PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializers
    # renderer_classes = (JSONRenderer,)
    # parser_classes = (JSONParser,)

class PurchaseOrderDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderDetailSerializers
    

# def delete(self,request,pk):
#     vendor = get_object_or_404(Vendor, pk= pk)   
#     if vendor.p     
from django.shortcuts import render
from .models import Vendor, PurchaseOrder  # Replace with your models
from rest_framework.decorators import api_view


@api_view()
def vendor_performance(request, vendor_id):
    try:
        vendor = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
        return render(request, 'vendor_not_found.html')  # Handle vendor not found

    # Filter purchase orders for this vendor
    purchase_orders = PurchaseOrder.objects.filter(vendor=vendor)

    # Calculate on-time delivery rate (assuming 'delivery_date' and 'expected_delivery_date' fields exist)
    total_orders = purchase_orders.count()
    on_time_orders = purchase_orders.filter(delivery_date__lte = on_time_delivery_rate).count()
    on_time_delivery_rate = (on_time_orders / total_orders) * 100 if total_orders > 0 else 0.0

    # Calculate other performance metrics as needed (e.g., quality rating, communication responsiveness)
    # ...

    context = new_func(vendor, on_time_delivery_rate)

    return render(request, 'vendor_performance.html', context)

def new_func(vendor, on_time_delivery_rate):
    context = {
        'vendor': vendor,
        'on_time_delivery_rate': on_time_delivery_rate,
        # Add other performance metrics to context
    }
    
    return context
