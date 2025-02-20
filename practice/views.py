from django.shortcuts import render

from django.http import HttpResponse

def practice(request,name):
    return HttpResponse(
        """
f"Hello,{name}"
"""
    )

# Create your views here.
