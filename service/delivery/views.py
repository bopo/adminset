from django.shortcuts import render

from .models import Delivery


def index(request):
    projects = Delivery.objects.all()
    return render(request, "delivery/delivery_list.html", locals())
