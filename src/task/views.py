from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


class KeyValueView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in ['get', 'post', 'put', 'patch',]:
            return super(KeyValueView, self).dispatch(request, *args, **kwargs)
        else:
            response = {
                'status': False,
                'message': 'Method not allowed (' + request.method+ ')'
            }
            return JsonResponse(response, status=405)
    def get(self, request):

        # if there is any data exist in session
        if 'key_value_data' not in request.session:
            key_value_data = {
                'eyakub': 'sorkar',
                'sorkar': 'eyakub',
            }
            request.session['key_value_data'] = key_value_data
            request.session.set_expiry(60)
        elif 'key_value_data' in request.session:
            key_value_data = request.session['key_value_data']
        else:
            key_value_data = {}
        
        if len(request.GET.getlist('keys')) > 0:
            keys = request.GET.get('keys').split(',')
            print('key.s...', keys)
            key_value_data = {
                key: value for (key, value) in key_value_data.items() if key in keys
            }
            for k, v in key_value_data.items():
                if k in keys:
                    print('key found...')
                    key_value_data = {k: v}

        request.session.set_expiry(300)
        return JsonResponse(data=key_value_data, status=200)
        

        