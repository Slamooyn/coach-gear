from django import forms
from main.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "stock"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "bg-gray-800 text-white border border-gray-600 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-500"
            }),
            "price": forms.NumberInput(attrs={
                "class": "bg-gray-800 text-white border border-gray-600 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-500"
            }),
            "description": forms.Textarea(attrs={
                "class": "bg-gray-800 text-white border border-gray-600 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-500",
                "rows": 4
            }),
            "stock": forms.NumberInput(attrs={
                "class": "bg-gray-800 text-white border border-gray-600 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-500"
            }),
            "is_featured": forms.CheckboxInput(attrs={
                "class": "h-5 w-5 accent-yellow-500 focus:ring-yellow-400 rounded"
            }),
            "thumbnail": forms.URLInput(attrs={
                "class": "bg-gray-800 text-white border border-gray-600 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-500"
            }),
            "category": forms.Select(attrs={
                "class": "bg-gray-800 text-white border border-gray-600 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-500"
            }),
        }

        labels = {
            "name": "Nama",
            "price": "Harga",
            "description": "Deskripsi",
            "thumbnail": "Thumbnail",
            "category": "Kategori",
            "is_featured": "Viral",
            "stock": "Stok",
        }
