from django.shortcuts import render
from app1.forms import inputweb
from random import randint

start = 0
end = 100
randnum = randint(start,end)
def home(request):
    msg =""
    num1 = end+1
    attempts = 0
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            while num1 != randnum:
                attempts += 1
                num1 = data1.get("input1")
                if num1<randnum:
                    msg = "Low! Try again."
                if num1>randnum:
                    msg="High! Try again."
                if num1==randnum:
                    msg="Congrats!You have guessed the number."
                return render(request,'app1/index.html',{'param1':msg,"form":form1})
    else:
        form1=inputweb()
    return render(request,'app1/index.html',{"form":form1})

