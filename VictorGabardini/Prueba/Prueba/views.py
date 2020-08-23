from django.http import HttpResponse
from django.template import loader
import datetime


def hola(request):
	return HttpResponse("Hola")

def hora_actual(request):
	hora = datetime.datetime.now()
	html = loader.get_template('../templates/hora.html')

	return HttpResponse(html.render())
	