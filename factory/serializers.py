from rest_framework import serializers

from .models import (
    Client,
    Order,
    NewOrder,
    DailyWork,
    SewingModel,
    FabricCutting,
    RawStuff,
    Storage,
    Price,
    QuantityModel
)


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"


class SewingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SewingModel
        fields = "__all__"
        
class SewingModelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SewingModel
        fields = ['color', 'material', 'type', 'labor_cost', 'client_price']


class OrderSerializer(serializers.ModelSerializer):

    sewing_model = SewingModelDetailSerializer(many=True, read_only=True)
        

    sewing_model = SewingModelSerializer(many=True, read_only=True)


    class Meta:
        model = Order
        fields = ['data_poluchenia', 'quantity_zayav', 'quantity_fact', 'data_zakup', 'raskroi_tkani', 'pod_flizelin',
                  'sewing_model']


class NewOrderSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()

    class Meta:
        model = NewOrder
        fields = ['description', 'price', 'color', 'client_name', 'received_date', 'delivery_date']

    def get_client_name(self, obj):
        return obj.client.full_name

    def create(self, validated_data):
        client_name = self.context['request'].data.get('client_name')
        client, _ = Client.objects.get_or_create(full_name=client_name)
        validated_data['client_id'] = client.id
        return super().create(validated_data)


class QuantityModelSerializer(serializers.ModelSerializer):
    # sewing_model = serializers.StringRelatedField()

    class Meta:
        model = QuantityModel
        fields = '__all__'


class DailyWorkSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = DailyWork
        fields = '__all__'


class FabricCuttingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FabricCutting
        fields = '__all__'


class RawStuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawStuff
        fields = '__all__'


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'
