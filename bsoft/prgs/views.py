from django.http import HttpResponse
from django.shortcuts import render


def index(requst):
    return HttpResponse('hello from box11')
