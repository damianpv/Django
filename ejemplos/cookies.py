# Author: Damian Perez
# Description: Guardar y Leer valor en cookie

from django.http import HttpResponse

# guardar valor en cookie
def set_cookie(request):
	response = HttpResponse()
	response.set_cookie("favorite_color", 'blue')
	return response

# leer valor de cookie
def get_cookie(request):
	ctx = {
		'content':request.COOKIES["favorite_color"],
	}
		
	return render_to_response('index.html', ctx)
