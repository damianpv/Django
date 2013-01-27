# Author: Damian Perez
# Description: Ignorar el CSRF

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def save_data(request):
	message = ''
	ctx = {
		'message':message,
	}
	return render_to_response('index.html', ctx, context_instance=RequestContext(request))