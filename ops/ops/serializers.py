from rest_framework import serializers
from officenotes.models import OfficeNote
from order.models import Order
from customer.models import Customer
from timeworker.models import TWorker
from graph.models import DateRange

class FirstOfficenoteField(serializers.RelatedField):
    def to_representation(self, value):
        return value.num

class OrderSerializer(serializers.ModelSerializer):
    firstofficenote = FirstOfficenoteField(read_only=True)

    customer = serializers.SerializerMethodField('getcustomer')
    def getcustomer(self, model):
        return model.firstofficenote.oncustomer.name

    dates = serializers.SerializerMethodField('getdates')
    def getdates(self, model):
        return model.get_shipmen()

    statusdata = serializers.SerializerMethodField('getstatusdata')
    def getstatusdata(self, model):
        return model.get_status()

    status = serializers.SerializerMethodField('getstatus')
    def getstatus(self, model):
        if model.ready:
            return "ready"
        else:
            st = model.get_status()
            if st != None:
                if st < 0: 
                    return "overdue"
                if st < 10: 
                    return "lesstendays"
                if st > 10: 
                    return "moretendays"
            else:
                return "notproduced"

    class Meta:
        model = Order
        fields = ("id", "product", "ordernum", "quantity", "firstofficenote", "customer", "dates", "statusdata", "status")
    

class GetOrderSerializer(serializers.ModelSerializer):
    firstofficenote = FirstOfficenoteField(read_only=True)

    customer = serializers.SerializerMethodField('getcustomer')
    def getcustomer(self, model):
        return model.firstofficenote.oncustomer.name

    dates = serializers.SerializerMethodField('getdates')
    def getdates(self, model):
        return model.get_shipmen()

    statusdata = serializers.SerializerMethodField('getstatusdata')
    def getstatusdata(self, model):
        return model.get_status()

    status = serializers.SerializerMethodField('getstatus')
    def getstatus(self, model):
        if model.ready:
            return "ready"
        else:
            st = model.get_status()
            if st != None:
                if st < 0: 
                    return "overdue"
                if st < 10: 
                    return "lesstendays"
                if st > 10: 
                    return "moretendays"
            else:
                return "notproduced"

    officenoteplan = serializers.SerializerMethodField('getofficenoteplan')
    def getofficenoteplan(self, model):
        return model.firstofficenote.date

    officenotefact = serializers.SerializerMethodField('getofficenotefact')
    def getofficenotefact(self, model):
        return model.firstofficenote.datereceiving
        
    officenoteexpired = serializers.SerializerMethodField('getofficenoteexpired')
    def getofficenoteexpired(self, model):
        return model.firstofficenote.get_expired()

    class Meta:
        model = Order
        fields = ("firstofficenote", "customer", "dates", "statusdata", "status", 
        # комплектовочные
        "pickingplan", "pickingfact", 
        # отгрузочные
        "shippingplan", "shippingfact",
        # конструкторские
        "engineeringplan", "engineeringfact",
        # изменения чертежей
        "drawingchangepercent", "drawingchangefact",
        # служебная записка
        "officenoteplan", "officenotefact", "officenoteexpired"
        )
    