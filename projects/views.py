from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def hello(request: HttpRequest):
    return HttpResponse("<h1> Hello world </h1>")


def projects(request: HttpRequest):
    return HttpResponse("<h1> List of projects </h1>")

def project(request: HttpRequest, pk: int):
    return HttpResponse(f"<h1> Single project id: {pk} </h1>")
