from rest_framework import serializers

from officenotes.models import OfficeNote
from order.models import Order
from timeworker.models import TWorker
from graph.models import DateRange

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("shipmentfrom", "shipmentto", "product", "ordernum", "quantity", "firstofficenote")