
from django.shortcuts import render,redirect
from .models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from userapp.models import *
from adminapp.models import *

# Create your views here.
def index(request):
    prdct = Prdb.objects.all().count()
    catct = Catdb.objects.all().count()
    userct = Regdb.objects.all().count()
    conct = Condb.objects.all().count()
    odrct = Checkout.objects.all().count()
    return render(request,'index.html',{'prdct':prdct,'catct':catct,'userct':userct,'conct':conct,'odrct':odrct})

def addcat(request):
    return render(request,'addcat.html')

def getcat(request):
    if request.method=='POST':
        cn = request.POST['catname']
        cd = request.POST['catdes']
        ci = request.FILES['catimg']
        data = Catdb(categoryname = cn, categorydesc = cd, categoryimg = ci)
        data.save()
        return render(request,'index.html')
    return render(request,'index.html')

def addprd(request):
    data = Catdb.objects.all()
    return render(request,'addprd.html',{'data':data})

def getprd(request):
    if request.method=='POST':
        pn = request.POST['prdname']
        pp = request.POST['prdprc']
        pc = request.POST['prdcat']
        pi = request.FILES['prdimg']
        pdata = Prdb(productname = pn, productcat = pc, productimg = pi,productprc = pp)
        pdata.save()
        return render(request,'index.html')
    return render(request,'index.html')

def viewcat(request):
    data = Catdb.objects.all()
    return render(request,'viewcat.html',{'data':data})

def viewprd(request):
    data = Prdb.objects.all()
    return render(request,'viewprd.html',{'data':data})

def viewcon(request):
    data = Condb.objects.all()
    return render(request,'viewcon.html',{'data':data})

def editcat(request,id):
    data = Catdb.objects.filter(id=id)
    return render(request,'editcat.html',{'data':data})

def updatecat(request,id):
    if request.method=='POST':
        cn = request.POST['catname']
        cd = request.POST['catdes']
        try:
            ci = request.FILES['catimg']
            fs = FileSystemStorage()
            file = fs.save(ci.name, ci)
        except MultiValueDictKeyError:
            file = Catdb.objects.get(id=id).catimg
        Catdb.objects.filter(id=id).update(categoryname = cn, categorydesc = cd, categoryimg = file)
        return render(request,'index.html')
    return render(request,'index.html')

def deletecat(request,id):
    Catdb.objects.filter(id=id).delete()
    return render(request,'index.html')

def editprd(request,id):
    pdata = Prdb.objects.filter(id=id)
    data = Catdb.objects.all()
    return render(request,'editprd.html',{'pdata':pdata,'data':data})

def updateprd(request,id):
    if request.method=='POST':
        pn = request.POST['prdname']
        pp = request.POST['prdprc']
        pc = request.POST['prdcat']
        try:
            pi = request.FILES['prdimg']
            fs = FileSystemStorage()
            file = fs.save(pi.name, pi)
        except MultiValueDictKeyError:
            file = Prdb.objects.get(id=id).productimg
        Prdb.objects.filter(id=id).update(productname = pn,productprc = pp,productcat = pc, productimg = file)
        return redirect('viewprd')
    return render(request,'index.html')

def deleteprd(request,id):
    Prdb.objects.filter(id=id).delete()
    return render(request,'index.html')

# def msg(request):
#     data = Condb.objects.all()
#     return render(request,'msg.html',{'data':data})

def usrcheckout(request):
    data = Checkout.objects.all()
    return render(request,'usrcheckout.html',{'data':data})