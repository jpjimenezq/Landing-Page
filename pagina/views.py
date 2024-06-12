from django.shortcuts import render, redirect
from django.templatetags.static import static
from .models import Correo

def landing_page(request):
    fondo_url = static('Fondo.jpg')
    if request.method == 'POST':
        email = request.POST.get('email')
        Correo.objects.create(email=email)
        return redirect('landing_page')

    return render(request, 'landingPage.html', {'fondo_url': fondo_url})
