from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


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
        if 'key_values' not in request.session:
            key_value_data = {
                'eyakub': 'sorkar',
                'sorkar': 'eyakub',
            }
            request.session['key_values'] = key_value_data
            request.session.set_expiry(60)
        elif 'key_values' in request.session:
            key_value_data = request.session['key_values']
        else:
            key_value_data = {}
        
        if len(request.GET.getlist('keys')) > 0:
            keys = request.GET.get('keys').split(',')
            key_value_data = {k: v for (k, v) in key_value_data.items() if k in keys}

        request.session.set_expiry(300)
        return JsonResponse(data=key_value_data, status=200)
        
    def post(self, request):
        if 'key_values' in request.session:
            key_value_data = dict(request.session['key_values'])
            key_value_data.update(request.POST.dict())
            request.session['key_values'] = key_value_data
        else:
            request.session['key_values'] = request.POST.dict()
        request.session.set_expiry(300)
        return JsonResponse(
            {'message': 'Data stored successfully'},
            status=200
        )

    def patch(self, request):
        print('re...')
        if 'key_values' in request.session:
            print('inside key-values')
            key_value_data_update = json.loads(request.body)
            # key = key_value_data_update.get('eyakub')
            print(key_value_data_update)
        else:
            key_value_data_update = {}
        
        keys = list(key_value_data_update.keys())
        print('body...', key_value_data_update)
        return JsonResponse(
            {'message': 'Data updated successfully.'},
            status = 200
        )