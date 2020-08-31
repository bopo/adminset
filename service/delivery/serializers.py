# -*- coding: utf-8 -*-
from rest_framework import serializers

from . import models


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Delivery
        fields = '__all__'
