from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime


# Create your views here.

def home(request):
    if request.method=='GET':
        return render(request,"home.html")

def calculate(request,interest=None):
    if request.method=="POST":
        
        start_date = request.POST['firstDate']
        end_date = request.POST['secondDate']
        amount = request.POST['amount']
        interest = request.POST['interest']

        if interest:
            start=datetime.strptime(start_date, "%Y-%m-%d")
            end=datetime.strptime(end_date, "%Y-%m-%d")
            amt=int(amount)
            roi=(int(interest))/100
            ans=0
        
            year=((end-start).days)//360
            month=(((end-start).days)%360)//30
            day=((((end-start).days)%360)%30)
            try:
                for i in range(1,year+1):
                    amt=amt+(amt*roi*12)
                ans=amt+(amt*roi*month)+(((amt*roi)//30)*day)
                return render(request,"home.html", {"result":ans})

            except:
                ans=amt+(amt*roi*month)+(((amt*roi)//30)*day)
                return render(request,"home.html", {"result":ans})
        else:
            start=datetime.strptime(start_date, "%Y-%m-%d")
            end=datetime.strptime(end_date, "%Y-%m-%d")
            amt=int(amount)
            val=0
            if (amt<=5000):
                roi=0.03
            else:
                roi=0.02
            year=((end-start).days)//360
            month=(((end-start).days)%360)//30
            day=((((end-start).days)%360)%30)
            try:
                for i in range(1,year+1):
                    amt=amt+(amt*roi*12)
                ans=amt+(amt*roi*month)+(((amt*roi)//30)*day)
                return render(request,"home.html", {"result":ans})

            except:
                ans=amt+(amt*roi*month)+(((amt*roi)//30)*day)
                return render(request,"home.html", {"result":ans})
       