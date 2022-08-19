from django.http import JsonResponse
from .models import Drink
from .serializerers import DrinkSerializer


def drin_list(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({'drinks': serializer.data}, safe=False)
