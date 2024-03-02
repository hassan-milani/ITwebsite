from django.urls import path
from .views import product_all_view, product_detail_view, get_cart_items, create_order, checkout, home_view, contact_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('products/', product_all_view, name='product_all'),
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('products/<int:product_id>/', product_detail_view, name='product_detail'),
    path('cart/items/', get_cart_items, name='get_cart_items'),
    path('order/create/', create_order, name='create_order'),
    path('checkout/', checkout, name='checkout'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
