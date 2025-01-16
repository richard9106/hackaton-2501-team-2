from django.shortcuts import render
from  django.http import HttpResponse


def reports(request):
    """reports view test"""
    return HttpResponse("hello")