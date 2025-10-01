from django.urls import path
from main.views import (
    show_main, show_json, show_json_by_id, show_xml, show_xml_by_id,
    product_add, product_details, register,
    login_user, logout_user, edit_product, delete_product , product_list , my_product
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),

    # UUID version
    path('xml/<uuid:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:product_id>/', show_json_by_id, name='show_json_by_id'),

    path('product/<uuid:id>/', product_details, name='product_details'),
    path('product-add/', product_add, name='product_add'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path("products/", product_list, name="product_list"),
    path("my-products/", my_product, name="my_product"),
]
