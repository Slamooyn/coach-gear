from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'aplikasi' : 'CoachGear',
        'name': 'Muhammad Salman Fahri',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)

