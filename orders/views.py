from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from orders.models import Regular_Pizza, Sicilian_Pizza, Toppings, Subs, Pasta, Salad, Dinner_Platters, Order_Number, Order


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    elif request.user.is_superuser:
        orders1 = Order_Number.objects.filter(status='in progress')
        orders2 = Order_Number.objects.filter(status='completed')
        context = {
            "user": request.user,
            'in_progres_orders': orders1,
            'completed_orders': orders2
        }
        return render(request, "orders/userorders.html", context)
    else:
        u = request.user.username
        obj3 = Order_Number.objects.filter(username=u).order_by('-id')[0]
        print('aaaaaa')
        ordnum = 1
        OrNum = Order_Number( order_num=ordnum, status='selecting', username=u )
        OrNum.save()
        print(obj3.id)
        if obj3.status == 'selecting':
            OrNum.delete()
            obj3.username = u
            obj3.save()
            request.session['orderid'] = obj3.id
            print(request.session['orderid'])
            context = {
                'items': Order.objects.filter(number = obj3.id),
                "user": request.user,
                "small": 'small',
                "large": 'large',
                }
            return render(request, "orders/menu.html", context)




    request.session['orderid'] = int(OrNum.id)
    print(request.session['orderid'])
    context = {
        "user": request.user,
        "small": 'small',
        "large": 'large',
    }
    return render(request, "orders/menu.html", context)

def signup(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
        print(username+email+password)
        return render(request, "orders/login.html", {'Rmessage': 'Username or email already registered'})
    else:
        user = User.objects.create_user(username, email, password)
        user.first_name = request.POST['first-name']
        user.last_name = request.POST['last-name']
        user.save()
        order = Order_Number(order_num=1, status='selecting', username=username)
        order.save()        
    return render(request, "orders/signup.html")


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    print(user)
    print(username + password)
    if user is not None:

        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def regular_view(request, option):
    if 'orderid' in request.session:
        oid = request.session.get('orderid')
    if int(option) % 2 == 0:
        option = 'Small'
        context = {
            'items': Order.objects.filter(number = oid),
            'regular_pizzas': Regular_Pizza.objects.filter(size = option),
            'toppings': Toppings.objects.all()
        }
        return render(request, "orders/menu.html", context)
    else:
        option = 'Large'
        context = {
            'items': Order.objects.filter(number = oid),
            'regular_pizzas': Regular_Pizza.objects.filter(size = option),
            'toppings': Toppings.objects.all()
        }
        return render(request, "orders/menu.html", context)


def sicilian_view(request, option):
    if 'orderid' in request.session:
        oid = request.session.get('orderid')
    if int(option) % 2 == 0:
        option = 'Small'
        context = {
            'items': Order.objects.filter(number = oid),
            'sicilian_pizzas': Sicilian_Pizza.objects.filter(size = option),
            'toppings': Toppings.objects.all()
        }
        return render(request, "orders/menu.html", context)
    else:
        option = 'Large'
        context = {
            'items': Order.objects.filter(number = oid),
            'sicilian_pizzas': Sicilian_Pizza.objects.filter(size = option),
            'toppings': Toppings.objects.all()
        }
        return render(request, "orders/menu.html", context)

def sub_view(request, option):
    if 'orderid' in request.session:
        oid = request.session.get('orderid')
    if int(option) % 2 == 0:
        option = 'Small'
        context = {
            'items': Order.objects.filter(number = oid),
            'subs': Subs.objects.filter(size = option)
        }
        return render(request, "orders/menu.html", context)
    else:
        option = 'Large'
        context = {
            'items': Order.objects.filter(number = oid),
            'subs': Subs.objects.filter(size = option)
        }
        return render(request, "orders/menu.html", context)

def pasta_view(request):
    if 'orderid' in request.session:
        oid = request.session.get('orderid')
    context = {
        'items': Order.objects.filter(number = oid),
        'pastas': Pasta.objects.all()
    }
    return render(request, "orders/menu.html", context)

def salad_view(request):
    if 'orderid' in request.session:
        oid = request.session.get('orderid')
    context = {
        'items': Order.objects.filter(number = oid),
        'salads': Salad.objects.all()
    }
    return render(request, "orders/menu.html", context)

def dinner_view(request, option):
    if 'orderid' in request.session:
        oid = request.session.get('orderid')
    if int(option) % 2 == 0:
        option = 'Small'
        context = {
            'items': Order.objects.filter(number = oid),
            'dinners': Dinner_Platters.objects.filter(size = option)
        }
        return render(request, "orders/menu.html", context)
    else:
        option = 'Large'
        context = {
            'items': Order.objects.filter(number = oid),
            'dinners': Dinner_Platters.objects.filter(size = option)
        }
        return render(request, "orders/menu.html", context)

def add_regular(request, pizza_id):
    if 'orderid' in request.session:
        oid = request.session.get('orderid')
    pizza = Regular_Pizza.objects.filter(id= pizza_id)
    type = pizza[0].type
    price = pizza[0].price
    size = pizza[0].size
    toppings = request.POST.getlist('toppings[]')
    desc = "Regular Pizza: " + ' ' + str(size) + ' '+ str(type) + str(toppings)
    new_item = Order(number = oid, description = desc, price = price )
    new_item.save()
    context = {
        'items': Order.objects.filter(number = oid)
    }
    return render(request, "orders/menu.html", context)

def add_sicilian(request, pizza_id):
    if 'orderid' in request.session:
        oid = request.session.get('orderid')
    pizza = Sicilian_Pizza.objects.filter(id= pizza_id)
    type = pizza[0].type
    price = pizza[0].price
    size = pizza[0].size
    toppings = request.POST.getlist('toppings[]')
    desc = "Sicilian Pizza: " + ' ' + str(size) + ' '+ str(type) + str(toppings)
    new_item = Order(number = oid, description = desc, price = price )
    new_item.save()
    context = {
        'items': Order.objects.filter(number = oid)
    }
    return render(request, "orders/menu.html", context)


def add_sub(request, sub_id):
    if 'orderid' in request.session:
        oid = request.session.get('orderid')
    sub = Subs.objects.filter(id= sub_id)
    type = sub[0].type
    price = sub[0].price
    size = sub[0].size
    desc = "Sub: " + ' ' + str(size) + ' '+ str(type)
    new_item = Order(number = oid, description = desc, price = price )
    new_item.save()
    context = {
        'items': Order.objects.filter(number = oid)
    }
    return render(request, "orders/menu.html", context)

def add_pasta(request, pasta_id):
    if 'orderid' in request.session:
        oid = request.session.get('orderid')
    pasta = Pasta.objects.filter(id= pasta_id)
    type = pasta[0].type
    price = pasta[0].price
    desc = "Pasta: " + str(type)
    new_item = Order(number = oid, description = desc, price = price )
    new_item.save()
    context = {
        'items': Order.objects.filter(number = oid)
    }
    return render(request, "orders/menu.html", context)

def add_salad(request, salad_id):
    if 'orderid' in request.session:
        oid = request.session.get('orderid')
    salad = Salad.objects.filter(id= salad_id)
    type = salad[0].type
    price = salad[0].price
    desc = "Salad: " + str(type)
    new_item = Order(number = oid, description = desc, price = price )
    new_item.save()
    context = {
        'items': Order.objects.filter(number = oid)
    }
    return render(request, "orders/menu.html", context)

def add_dinner(request, dinner_id):
    if 'orderid' in request.session:
        oid = request.session.get('orderid')
    dinner = Dinner_Platters.objects.filter(id= dinner_id)
    type = dinner[0].type
    price = dinner[0].price
    size = dinner[0].size
    desc = "Dinner_Platters: " + ' ' + str(size) + ' ' + str(type)
    new_item = Order(number = oid, description = desc, price = price )
    new_item.save()
    context = {
        'items': Order.objects.filter(number = oid)
    }
    return render(request, "orders/menu.html", context)

def confirm_view(request):
    if 'orderid' in request.session:
        oid = request.session.get('orderid')
    orders = Order.objects.filter(number = oid)
    total = 0
    for order in orders:
        total = total + order.price
    O = Order_Number.objects.get(id=oid)
    O.status = 'in progress'
    O.save()
    context = {
        'order': O,
        'items': Order.objects.filter(number = oid),
        'total': total
    }
    return render(request, "orders/confirmed.html", context)

def orders_view(request):
    orders1 = Order_Number.objects.filter(status='in progress').filter(username=request.user.username)
    orders2 = Order_Number.objects.filter(status='completed').filter(username=request.user.username)
    os=Order_Number.objects.all()
    context = {
        'in_progres_orders': orders1,
        'completed_orders': orders2
    }
    return render(request, "orders/userorders.html", context)


def view_order(request, order_id):
    context = {
        "user": request.user,
        'orders': Order.objects.filter(number=order_id),
        'order': order_id
    }
    return render(request, "orders/order.html", context)

def complete(request, id):
    update = Order_Number.objects.get(id=id)
    update.status = 'completed'
    update.save()
    orders1 = Order_Number.objects.filter(status='in progress')
    orders2 = Order_Number.objects.filter(status='completed')
    context = {
        'in_progres_orders': orders1,
        'completed_orders': orders2
    }
    return render(request, "orders/userorders.html", context)

def remove(request, id):
    try:
        item = Order.objects.get(id=id)
    except OrderDoesNotExist:
        return HttpResponseRedirect(reverse("index"))

    number = item.number
    print('aeeaa ')
    print(number)
    item.delete()
    context = {
        'user': request.user,
        'items': Order.objects.filter(number=number)
    }
    return render(request, "orders/menu.html", context)
