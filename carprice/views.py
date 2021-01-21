from django.shortcuts import render,HttpResponse
from babel.numbers import format_currency

import pickle
model=pickle.load(open('./trainedModel/trainedModel','rb'))
# Create your views here.
def index(request):
    return render(request,'index.html')


def predict(request):
    if request.method=="POST":
       kilometre=float(request.POST.get('kilometre'))
       price=int(request.POST.get('price'))
       year=int(request.POST.get('year'))
       engine=int(request.POST.get('engine'))
       power=float(request.POST.get('power'))
       fuel=request.POST.get('fuel')
       transmission=request.POST.get('transmission')
       ownertype=request.POST.get('ownertype')
       if fuel=='cng':
           diesel=0
           petrol=0
       elif fuel=='diesel':
           diesel=1
           petrol=0
       else:
           petrol=1
           diesel=0
       if transmission=="manual":
           t_val=1
       else:
           t_val=0
       if ownertype=='first':
           second=0
           third=0
       elif ownertype=='second':
           second=1
           third=0
       else:
           second=0
           third=1
    year=2021-year
    pred=model.predict([[kilometre,price,year,engine,power,petrol,diesel,t_val,second,third]])  
    pred_price=format_currency(price,'INR',locale="en_IN")
    
    
    context={"pred":pred_price}    
    return render(request,'index.html',context)