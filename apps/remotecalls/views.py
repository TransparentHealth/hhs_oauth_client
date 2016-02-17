#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json


# Create your views here.

@login_required
def call_read(request):
    return JsonResponse({"foo":"bar"})
    
    
    