from django.urls import path
from main.views import (show_main,product_add,product_details,edit_product,delete_product,register,login_user,logout_user,show_json,show_xml, show_json_by_id,show_xml_by_id,)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("add-product/", product_add, name="product_add"),
    path("product/<uuid:id>/", product_details, name="product_details"),
    path("edit-product/<uuid:id>/", edit_product, name="edit_product"),
    path("delete-product/<uuid:pk>/", delete_product, name="delete_product"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout_user"),
    path("json/", show_json, name="show_json"),
    path("xml/", show_xml, name="show_xml"),
    path("json/<uuid:product_id>/", show_json_by_id, name="show_json_by_id"),
    path("xml/<uuid:product_id>/", show_xml_by_id, name="show_xml_by_id"),
]
