from django.http import HttpResponse
from django.shortcuts import redirect, render

from .cart import Cart
from .models import Product,OrderItems,Order
from twilio.rest import Client
import random
import datetime
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def Home(request):
    return render(request,'app/index.html')
def Fruits(request):
    return render(request, 'app/fruit.html')
def Services(request):
    return render(request, 'app/service.html')

def Contact(request):
    return render(request,'app/contact.html')

def Details(request):
    product = Product.objects.all().order_by('id')
    p = Paginator(product,3)
    page_number = request.GET.get('page')
    datafinal = p.get_page(page_number)

    return render(request,'app/details.html',{'product':datafinal})

def BuyProduct(request, pk):
    product_info = Product.objects.get(id= pk)
    return render(request,'app/buyproduct.html',{'info':product_info})


def show_cart(request):
    cart = Cart(request)
    carts = cart.List()
    total = cart.get_total()
    
    
        
    
    return render(request,'app/checkout.html',{'carts':carts ,'total':total})



    


def Add_to_cart(request):
    if request.method == 'POST':
        id = request.POST.get('p_id')
        # print(id)
        product = Product.objects.get(id =id)
        quantity = request.POST['quantity']        
        if not quantity:
            quantity = 1    
        cart = Cart(request)
        cart.add(product,quantity)

        carts = Cart(request)
        print(carts)
        # if cart['product_id'] != id:
        #     cart.add(product,quantity)
        # else:
        #     cart.add(product, quantity, override_quantity=True)
        return show_cart(request)
        # return render(request, 'app/index.html')
    else:
        return show_cart(request)

    
def Delete(request,pk):
    product = Product.objects.get(id = pk)
    cart = Cart(request)
    cart.remove(product)
    return show_cart(request)

def Update(request):
    if request.method == 'POST':
        id = request.POST['p_id']
        quantity = request.POST['number']
        print(quantity)
        product = Product.objects.get(id = id)
        cart = Cart(request)
        cart.add(product, quantity, override_quantity= True)
        return show_cart(request)
    else:
        return HttpResponse("Cannot update")


def Orders(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phn_number  = request.POST.get('number')
        phone_number = '+977'+" "+ phn_number 
        # print(phone_number)
        location = request.POST.get('location')
        otpcode = random.randint(1000,9999)
        request.session['otp'] = otpcode
        print(otpcode)
        print(otpcode)
        order_date = datetime.datetime.now()
        print (order_date)

        orders = Order(name= name, location= location, phone_number=phn_number, order_date = order_date, otp = otpcode)
        orders.save()
        if phn_number:
            account_sid = 'ACd5b4357d6c0bb415043e572ad7258d8c'
            auth_token = '126ea9ebdb4851735c497b8ff7681699'
            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body=f"Your OTP code is {otpcode}",
                                from_='+19897155832',
                                to=phone_number
                            )
 
            print(message.sid)
            
        
        return show_cart(request)

    else:
        return render(request, 'app/checkout.html')
    
def PayMent(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        # OTP = Order.objects.all()
        
        # if request.session.has_key('otp'):
        #     otpcode = request.session['otp']
        #     print (otpcode)
        #     print("==================================")
        #     print(number)
        #     if otpcode == number:
        #         order = Order.objects.get(otp = number)
        #         cart = Cart(request)
        #         carts = cart.List()
        #         for i in carts:
        #             OrderItems.objects.create(order= order, product = i['obj'], quantity = i['quantity'])
                    
        #         cart.clear()
        #         return render(request, 'app/paymentsuccess.html')
        #     else:
        #         messages.success(request,"Incorrect OTP code..")
        #         return show_cart(request)
        # else:
        #     cart = Cart(request)
        #     cart.clear()  
        #     messages.success(request,"Sorry your otp is expired!! get new otp")
        #     return show_cart(request)


       
        if request.session.has_key('otp'):
            if Order.objects.filter(otp = number):
            #if Order.objects.get(otp = number):
                
                order = Order.objects.get(otp = number)
                cart = Cart(request)
                carts = cart.List()
                for i in carts:
                    OrderItems.objects.create(order= order, product = i['obj'], quantity = i['quantity'])
                    
                cart.clear()
                return render(request, 'app/paymentsuccess.html')
            else:
                messages.success(request,"Incorrect OTP code..")
                return show_cart(request)
        else:
            messages.success(request,"Sorry your otp is expired!! get new otp")
            return show_cart(request)
    else:
        return show_cart(request)



