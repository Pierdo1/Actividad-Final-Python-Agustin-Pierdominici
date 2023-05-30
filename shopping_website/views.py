from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json


# Create your views here.

def index(request):
    
    allprods = []
    catwiseprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catwiseprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nslide = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod, range(1, nslide), nslide])
    params = {"allprods":allprods}
    return render(request, 'shopping_website/index.html', params)

def about(request):
    return render(request, 'shopping_website/about.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    
    return render(request, 'shopping_website/tracker.html')

def productview(request, myid):
    product = Product.objects.filter(id = myid)
    return render(request, 'shopping_website/products.html', {"product":product[0]})

def checkout(request):
    if request.method=="POST":
        print(request.POST)
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        add1 = request.POST.get('address1', '')
        print(add1)
        add2 = request.POST.get('address2', '')
        print(add2)
        address= add1 + add2
        print(request.POST.get('address1'))
        print(request.POST.get('address2'))
        print(address)
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        oid = order.order_id
        update= OrderUpdate(order_id= order.order_id, update_desc="The order has been placed")
        update.save()
        return render(request, 'shopping_website/checkout.html', {'thank':thank, 'id': oid})

    
    return render(request, 'shopping_website/checkout.html')

def search(request):
    return render(request, 'shopping_website/search.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        return HttpResponse('<script>alert("Mensaje enviado correctamente."); window.location.href="/shopping_website/contact/";</script>')
    
    return render(request, 'shopping_website/contact.html')