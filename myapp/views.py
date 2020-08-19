from django.shortcuts import render
from django.http import HttpResponse
from myapp import forms

# Create your views here.

def builtinforms(request):
    form=forms.SampleForm()
    return render(request,"builtin.html",{'form':form})


#forms is afile or a library
#in Forms form is a class so we inherit from forms.Form
