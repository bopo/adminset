# -*- coding: utf-8 -*-
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ..cmdb.views import AssetsViewSet,GroupsViewSet,IdcViewSet
from ..delivery.views import DeliveryViewSet

router = DefaultRouter()
router.register('delivery', DeliveryViewSet, 'delivery')
router.register('assets', AssetsViewSet, 'assets')
router.register('groups', GroupsViewSet, 'groups')
router.register('idc', IdcViewSet, 'idc')

urlpatterns = (
    path('', include(router.urls)),
    path('cmdb/', include('service.cmdb.urls')),
    path('delivery/', include('service.delivery.urls')),
    # path('auth/', include('service.backends.passport.urls')),
    path('rest/', include('rest_framework.urls', namespace='rest_framework')),
)
