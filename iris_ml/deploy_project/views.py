from django.shortcuts import render,redirect
from django.views import View 
from .models import *
import pickle
import pandas as pd
from pickle import load

# Create your views here.

def mlview(request):
    result=''
    if request.method == "POST":
        SepalLengthCm = float(request.POST.get("SepalLengthCm"))
        SepalWidthCm = float(request.POST.get("SepalWidthCm"))
        PetalLengthCm = float(request.POST.get("PetalLengthCm"))
        PetalWidthCm = float(request.POST.get("PetalWidthCm"))

        model = pd.read_pickle(r'C:\Users\User\Desktop\ML IRIS-2\new_model.pickle')

        result = model.predict([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]])

        result=result[0]

    return render(request, "deploy/base.html",{'result':result})