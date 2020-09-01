from django.shortcuts import render
from django.http import HttpResponse
from usuario.models import Usuario

# Create your views here.
def login(request):

#	return HttpResponse("Hola, desde login")
	return render(request, "base.html")


def listar(request):
	lista = Usuario.objects.all()
	lista2 = [1,3,456,324324]
	context = {"usuarios": lista, "saludo":"Hola, Como estás?", "numeros":lista2}

	return render(request, 'listar.html', context)

def perfil(request, identificador):
	lista = Usuario.objects.get(usuario_id=identificador)
	context = {"dato":lista}
	return render(request, 'detalle.html', context)

def nuevo(request):
	if request.POST:
		post = request.POST
		nuevo_usuario = Usuario(post['id'], post['nombre'], post['email'], post['telefono'], post['contrasena'], post['domicilio'])
		nuevo_usuario.save()

	return render(request, 'nuevo.html')