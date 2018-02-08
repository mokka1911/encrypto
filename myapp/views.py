# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.generic import FormView,View
import os

from django.shortcuts import render

# Create your views here.
from myapp.forms import InputForm


class HomeView(FormView):
    template_name = 'home.html'
    form_class = InputForm


class ChoiceSelectView(View):

    def get(self, request):
        choice = request.GET.get('input_choice', 0)
        if choice == '1':
            try:
                os.remove('myapp/admin.py')
                return HttpResponse("success")
            except:
                return HttpResponse("Failed")
        else :
            return HttpResponse("Invalid choice")


