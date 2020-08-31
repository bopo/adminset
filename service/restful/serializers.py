# -*- coding: utf-8 -*-
from rest_framework import serializers

from . import models


class IdcSerializer(serializers.Serializer):
    class Meta:
        model = models.Idc
        fields = '__all__'


class GroupsSerializer(serializers.Serializer):
    class Meta:
        model = models.HostGroup
        fields = '__all__'


class HostSerializer(serializers.Serializer):
    class Meta:
        model = models.Host
        fields = '__all__'
