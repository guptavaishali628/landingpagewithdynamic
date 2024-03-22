from django.shortcuts import render

# Create your views here.
def index(request,id):
    data = id
    return render(request,'home.html',{'key':data})


def combination(request,id,pk,idpk,pkid):
    data = {
        'data1':id,
        'data2':pk,
        'data3':idpk,
        'data4':pkid
    }
    return render(request,'combination.html',{'key':data})
