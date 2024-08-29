from .models import internet
from accounts.models import provider
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from django.http import JsonResponse
from django.core import serializers

class Show(View):
    def get(self,request):
        internets = internet.objects.all()
        s = serializers.serialize('json',internets)
        return JsonResponse(s,safe=False)




@method_decorator(csrf_exempt, name='dispatch')
class create_i(View):

    def post(self,request):
        cd = json.loads(request.body)
        users = provider.objects.filter(name = cd['owner'])
        if users .exists():
            prodact = internet.objects.create( owner=users,
                                   name=cd['name'],
                                               price=cd['price'])
            prodact.save()
            return JsonResponse('done')
        return JsonResponse('erorr')




