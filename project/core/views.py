from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):  #Solicitud (request) de la vista

    return render(request, "core/inicio.html") #Respuesta del la vista html (templates)
