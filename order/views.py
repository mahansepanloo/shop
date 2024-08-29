from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from accounts.models import costomer
from Internet_package.models import internet
import json
from django.http import JsonResponse
from .models import Order


@method_decorator(csrf_exempt, name='dispatch')
class CreateOrderView(View):

    def post(self, request):
        try:
            cd = json.loads(request.body)
            users = costomer.objects.filter(name=cd['owner'])
            packages = internet.objects.filter(name=cd['name'])

            if users.exists() and packages.exists():
                user = users.first()
                package = packages.first()

                order = Order.objects.create(
                    user=user,
                    pakage=package,
                    cost=cd['price']
                )
                return JsonResponse({'message': 'Order created successfully'}, status=201)

            if not users.exists():
                return JsonResponse({'error': 'User not found'}, status=404)
            if not packages.exists():
                return JsonResponse({'error': 'Package not found'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


def save_orders_to_file(request):
    try:
        orders = Order.objects.all().values()
        orders_list = list(orders)


        with open('orders.json', 'w') as file:
            json.dump(orders_list, file, ensure_ascii=False, indent=4)

        return JsonResponse({'message': 'Orders saved to file successfully'}, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)