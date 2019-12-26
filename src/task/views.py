from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


class KeyValueView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in ['get', 'post', 'put', 'patch',]:
            return super().dispatch(request, *args, **kwargs)
        else:
            response = {
                'status': False,
                'message': 'Method not allowed (' + request.method+ ')'
            }
            return JsonResponse(response, status=405)
    def get(self, reqeust):
        if 'key_value_data' not in reqeust.session:
            key_value_data = {
                'eyakub': 'sorkar',
                'sorkar': 'eyakub',
            }
            request.session['key_value_data'] = key_value_data
            reqeust.session.set_expiry(60)
        elif 'key_value_data' in reqeust.session:
            key_value_data = reqeust.session['key_value_data']
        