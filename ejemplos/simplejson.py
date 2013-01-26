# Autor: Damian Perez

from django.http import HttpResponse
from django.utils import simplejson

# obtener listado
def get_listado_view(request):

	to_json = {
        "key1": "value1",
        "key2": "value2"
    }
	return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')