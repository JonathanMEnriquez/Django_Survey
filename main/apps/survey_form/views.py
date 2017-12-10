# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'survey_form/index.html')

def process(request):
    if request.method == 'POST':
        try:
            request.session['counter'] += 1
        except:
            request.session['counter'] = 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        if len(request.POST['comment']) < 1:
            request.session['comment'] = ':('
        else:
            request.session['comment'] = request.POST['comment']
        return redirect('/display')
    else:
        return redirect('/')

def display(request):
    return render(request, 'survey_form/display.html')