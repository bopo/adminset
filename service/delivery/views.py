from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


def index(request):
    projects = models.Delivery.objects.all()
    return render(request, "delivery/delivery_list.html", locals())


class DeliveryViewSet(ModelViewSet):
    """
    """
    serializer_class = serializers.DeliverySerializer
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Delivery.objects.all()
