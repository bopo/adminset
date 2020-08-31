from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class AssetsViewSet(ModelViewSet):
    """
    """
    serializer_class = serializers.HostSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Host.objects.all()


class GroupsViewSet(ModelViewSet):
    """
    """
    serializer_class = serializers.GroupsSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = models.HostGroup.objects.all()


class IdcViewSet(ModelViewSet):
    """
    """
    serializer_class = serializers.HostSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Idc.objects.all()
