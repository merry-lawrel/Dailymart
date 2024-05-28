from django.shortcuts import render,redirect
from adminapp.models import *
from .models import *
from django.db.models.aggregates import Sum

# Create your views here.
def userindex(request):
    pdata = Prdb.objects.all()
    cdata = Catdb.objects.all()
    return render(request,'userindex.html',{'pdata':pdata,'cdata':cdata})

def singleprd(request,id):
    pdata = Prdb.objects.filter(id=id)
    return render(request,'singleprd.html',{'pdata':pdata})

def product(request,category):
    data1 = Prdb.objects.all()
    for i in data1:
        if category == i.productcat:
            data2 = Prdb.objects.filter(productcat=category)
            return render(request,'product.html',{'prdata':data2})
    return render(request,'product.html',{'prdata':data1})

def reg(request):
    return render(request,'reg.html')

def getreg(request):
    if request.method == 'POST':
        n = request.POST['rname']
        p = request.POST['rpswd']
        m = request.POST['rmail']
        a = request.POST['radd']
        data = Regdb(regname = n, regpswd = p, regmail = m, regadd = a)
        data.save()
    return redirect('login')

def login(request):
    return render(request,'login.html')

def getlog(request):
    if request.method == 'POST':
        ln = request.POST['lname']
        lp = request.POST['lpswd']
        if Regdb.objects.filter(regname = ln, regpswd = lp).exists():
            data = Regdb.objects.filter(regname = ln, regpswd = lp).values('regmail','regadd','id').first()
            request.session['uname'] = ln
            request.session['umail'] = data['regmail']
            request.session['uadd'] = data['regadd']
            request.session['uid'] = data['id']
            return redirect('userindex')
    return redirect('login')

def contact(request):
    return render(request,'contact.html')

def getct(request):
    if request.method == 'POST':
        m = request.POST['cmsg']
        cname = request.session['uname']
        cmail = request.session['umail']
        data = Condb(contactmsg = m, contactname = cname, contactmail = cmail)
        data.save()
    return redirect('userindex')

def logout(request):
    del request.session['uname']
    del request.session['umail']
    del request.session['uadd']
    del request.session['uid']
    return redirect('userindex')

def cartdata(request,id):
    if request.method == 'POST':
        uid = request.session.get('uid')
        qty = request.POST['prdqty']
        tot = request.POST['prdtot']
        data = Cartdb(userid = Regdb.objects.get(id = uid),prdid = Prdb.objects.get(id = id), cqty = qty, ctot = tot)
        data.save()
        return redirect('cart')
    return redirect('userindex')

def cart(request):
    u = request.session.get('uid')
    data = Cartdb.objects.filter(userid = u,status=0)
    return render(request,'cart.html',{'data':data})

def checkout(request):
    u = request.session.get('uid')
    data = Cartdb.objects.filter(userid = u,status=0)
    s = Cartdb.objects.filter(userid = u,status=0).aggregate(Sum('ctot'))
    return render(request,'checkout.html',{'data':data,'s':s})

def checkoutdata(request):
    if request.method == 'POST':
        u = request.session.get('uid')
        ad = request.POST['adds']
        c = request.POST['cty']
        s = request.POST['stt']
        cr = request.POST['ctr']
        p = request.POST['ptc']
        m = request.POST['mob']
        ml = request.POST['eml']
        order = Cartdb.objects.filter(userid = u,status = 0)
        for i in order:
            data = Checkout(userid = Regdb.objects.get(id=u),cartid = Cartdb.objects.get(id = i.id),address = ad,city = c,state = s, country = cr, postalcode = p, mobile = m, mail = ml)
            data.save()
        Cartdb.objects.filter(id=i.id).update(status=1)
        return render(request,'contact.html',{'msg':'Order Succesful, thank you very much! Let us know your experience.'})
    return redirect('userindex')