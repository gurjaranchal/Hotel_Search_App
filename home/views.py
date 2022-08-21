from django.http import JsonResponse
from django.shortcuts import render
from .models import *

# Create your views here.
# def homepage(request):
#     return render(request,'homepage.html')
    
def login(request):
    return render(request,'login.html')

def home(request):
    emenities=Emenities.objects.all()
    context ={'emenities':emenities}
    return render(request,'home.html',context)



def api_hotels(request):
    hotels_objs = Hotels.objects.all()
    
    price=request.GET.get('price')
    # print(price)
    if price:
        hotels_objs=hotels_objs.filter(price__lte=price)

    emenities=request.GET.get('emenities')
    if emenities:
        emenities=emenities.split(',')
        em=[]
        for e in emenities:
            try:
                em.append(int(e))
            except Exception as e:
                pass
        hotels_objs=hotels_objs.filter(emenities__in=em)


        # print(em)


    payload=[]
    for hotel_obj in hotels_objs:
        result={}
        result['hotel_name']=hotel_obj.hotel_name
        result['hotel_description']=hotel_obj.hotel_description
        result['hotel_image']=hotel_obj.hotel_image
        result['hotel_price']=hotel_obj.price
        result['hotel_link']=hotel_obj.hotel_link
        payload.append(result)

    return JsonResponse(payload,safe=False)

def aboutus(request):
    return render(request,"about.html")

def facility(request):
    return render(request,"facility.html")


    

