from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from service.accounts.permission import permission_verify


class finder(LoginRequiredMixin, View):

    # @method_decorator(permission_verify())
    def get(self, request):
        return render('mfile/finder.html', locals())
