
import json
from django.http import JsonResponse
from django.views import View
from app.inventory.models.product_type import ProductType
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class ProductTypeView(View):
    def get(self, request, *args, **kwargs):
        product_types = ProductType.objects.all()

        data = list([{"name": i.name} for i in product_types])
        return JsonResponse({"data": data}, safe=False)


    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            name = data.get('name')
            ProductType.objects.create(name=name)

            return JsonResponse({
                "message": "Product type created successfully",
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def put(self, request, id, *args, **kwargs):
        try:
            data = json.loads(request.body)
            name = data.get('name')
            product_type = ProductType.objects.get(id=id)
            product_type.name = name
            product_type.save()

            return JsonResponse({
                "message": "Product type created successfully",
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def delete(self, request, id, *args, **kwargs):
        try:
            try:
                product_type = ProductType.objects.get(id=id)
            except ProductType.DoesNotExist:
                return JsonResponse({"error": "Product type not found"}, status=404)
            product_type.delete()
            return JsonResponse({
                "message": "Product type deleted successfully"
            }, status=204)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)