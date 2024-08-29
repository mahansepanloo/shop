from .models import costomer,provider
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from django.http import JsonResponse


@method_decorator(csrf_exempt, name='dispatch')
class Sing_in_p(View):

    def post(self,request):
        cd = json.loads(request.body)


        prodact = provider.objects.create( name=cd['name'],
                               phone_number=cd['phone_number'])
        prodact.save()

        return JsonResponse('done')


@method_decorator(csrf_exempt, name='dispatch')
class Sing_in_c(View):

    def post(self,request):
        cd = json.loads(request.body)


        prodact = costomer.objects.create( name=cd['name'],
                               phone_number=cd['phone_number'])
        prodact.save()

        return JsonResponse('done')
