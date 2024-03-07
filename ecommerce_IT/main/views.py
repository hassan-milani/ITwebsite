from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Client, Order, Category
import json
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required


def home_view(request):
    return  render(request, 'index.html')

def contact_view(request):
    return  render(request, 'contact.html')


def product_all_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'products.html', {'products': products, 'categories':categories})


def product_detail_view(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product-detail.html', {'product': product})


######## احتياط
def get_cart_items(request):
    # Retrieve cart items from session
    cart_items = request.session.get('cart', [])
    
    # Return cart items as JSON response
    return JsonResponse({'cart': cart_items})


@require_GET
def get_product_price(request):
    product_id = request.GET.get('product_id')
    
    try:
        product = Product.objects.get(id=product_id)
        response = {
            'name': product.p_name,
            'price': product.p_price,
            'image':product.p_image.url
        }
        return JsonResponse(response)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)


@login_required(login_url='register')    
def create_order(request):
    if request.method == 'POST':
        # Assuming the request data contains product ids and quantities
        data = json.loads(request.body)
        product_ids_quantities = data.get('cart', {})  # Assuming products are sent as a dictionary with product_id as key and quantity as value
        print(product_ids_quantities)
        # Calculate the total price
        total_price = 0
        order_items = {}
        for dictionary in product_ids_quantities:
            product_id = dictionary["product_id"]
            quantity = dictionary["quantity"]
            
            product = Product.objects.get(pk=product_id)
            item_price = product.p_price * quantity
            total_price += item_price
            order_items[product_id] = {'name': product.p_name, 'quantity': quantity, 'price_per_item': str(product.p_price), 'total_price': str(item_price)}

        # Create the order
        client_name = "TEST"
        client_email = "TEST@gmail.com"
        client_phone = 2132140
        # client_name = data.get('client_name', '')
        # client_email = data.get('client_email', '')
        # client_phone = data.get('client_phone', '')

        client, created = Client.objects.get_or_create(c_name=client_name, c_email=client_email, c_phone=client_phone)
        order = Order.objects.create(order_final_price=total_price, order_items=json.dumps(order_items), client=client)

       

        return JsonResponse({'message': 'Order created successfully', 'order_id': str(order.order_id)})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


######## احتياط
def checkout(request):
    if request.method == 'GET':
        order_id = request.session.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            # Assuming you want to retrieve order items from local storage and store them in the order's text field
            order_items = request.session.get('order_items', {})
            order.order_items = json.dumps(order_items)
            order.save()
            return JsonResponse({'message': 'Checkout successful'})
        else:
            return JsonResponse({'error': 'Order not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)