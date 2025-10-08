from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import datetime


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    search_query = request.GET.get("q", "")

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = serializers.serialize("json", products)
        return JsonResponse({"products": data}, safe=False)

    context = {
        'aplikasi': 'CoachGear',
        'name': request.user.username,
        'class': 'PBP A',
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'search_query': search_query,
    }
    return render(request, "main.html", context)


@login_required(login_url='/login')
def product_add(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ProductForm(request.POST)
        if form.is_valid():
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            return JsonResponse({"status": "success", "product_id": product_entry.id})
        else:
            return JsonResponse({"status": "error", "errors": form.errors})
    else:
        form = ProductForm()
        return render(request, "product_add.html", {"form": form})


@login_required(login_url='/login')
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = serializers.serialize("json", [product])
        return JsonResponse({"product": data})
    return render(request, "product_details.html", {"product": product})


@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if product.user != request.user:
        return JsonResponse({"status": "forbidden"}, status=403)

    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "error", "errors": form.errors})
    else:
        form = ProductForm(instance=product)
        return render(request, "edit_product.html", {"form": form, "product": product})


@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.user != request.user:
        return JsonResponse({"status": "forbidden"}, status=403)

    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        product.delete()
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "invalid_request"}, status=400)


@login_required(login_url='/login')
def product_list(request):
    products = Product.objects.all()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = serializers.serialize("json", products)
        return JsonResponse({"products": data})
    return render(request, "product_list.html", {"products": products})


@login_required(login_url='/login')
def my_product(request):
    products = Product.objects.filter(user=request.user)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = serializers.serialize("json", products)
        return JsonResponse({"products": data})
    return render(request, "my_product.html", {"products": products})


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = JsonResponse({"status": "success"})
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({"status": "error", "errors": form.errors})
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    response = JsonResponse({"status": "success"})
    response.delete_cookie('last_login')
    return response


def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")


def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
   

def show_json_by_id(request, product_id):
    try:
        product_item = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
