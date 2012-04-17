# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def main(request):
	return render_to_response('index.html')

def about(request):
	return render_to_response('about.html')