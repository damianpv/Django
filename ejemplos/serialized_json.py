# Author: Damian Perez
# Description: Obtener datos de un modelo, serializarlos y generar JSON

from django.http import HttpResponse
from django.core import serializers
from demo.apps.productos.models import Productos

# obtener listado
def get_rest_view(request):
	#se obtienen todos los productos
	productos = Productos.objects.all()
	#solo nos interesa obtener como json el id_producto y producto.
	data = serializers.serialize('json', producto, fields=('id_producto','producto'))
	return HttpResponse(data, mimetype='application/javascript')