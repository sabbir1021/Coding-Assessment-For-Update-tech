from rest_framework import serializers
from .models import Sales


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = (
            'id',
            'order_id', 
            'order_date', 
            'ship_date', 
            'ship_mode',
            'customer_id',
            'customer_name',
            'segment' ,
            'country',
            'city' ,
            'state',
            'postal_code',
            'region',
            'product_id' ,
            'category' ,
            'sub_category' ,
            'product_name' ,
            'sales'
            )