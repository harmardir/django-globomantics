from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello there, Globomantics E-commerce store front coming here ...")


def detail(request):
    return HttpResponse("Hello there, Globomantics E-commerce store front coming here ...")


def electronics(request):
    return HttpResponse("Hello there, Globomantics E-commerce store front coming here ...")

