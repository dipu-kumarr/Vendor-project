from rest_framework import serializers
from . import models
from dataclasses import fields


class VendorSerializers(serializers.ModelSerializer):
    class Meta:
        model= models.Vendor
        fields=['name','address','contact_details','vendor_code']


class VendorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model= models.Vendor
        fields=['id','name','address','contact_details','vendor_code']

    def __init__(self, *args, **kwargs):
        super(VendorDetailSerializers, self).__init__(*args, **kwargs)
        self.Meta.depth = 1



class PurchaseOrderSerializers(serializers.ModelSerializer):
    class Meta:
        model= models.PurchaseOrder
        fields=['po_number','vendor','order_date','delivery_date','items','quantity',
                'status','quality_rating','issue_date','acknowledgment_date']

    def __init__(self, *args, **kwargs):
        super(PurchaseOrderSerializers, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class PurchaseOrderDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model= models.PurchaseOrder
        fields=['po_number','vendor','order_date','delivery_date','items','quantity',
                'status','quality_rating','issue_date','acknowledgment_date']

    def __init__(self, *args, **kwargs):
        super(PurchaseOrderDetailSerializers, self).__init__(*args, **kwargs)
        self.Meta.depth = 1



class HistoricalPerformance(serializers.ModelSerializer):
    class Meta:
        model= models.HistoricalPerformance
        fields = ['vendor','date','on_time_delivery_rate','quality_rating_avg',
                  'average_response_time','fulfillment_rate' ]