import json
from django.http import JsonResponse
from django.views import View
from app.inventory.models.inventory import Inventory
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class InventoryView(View):
    def get(self, request, *args, **kwargs):
        inventories = Inventory.objects.all()
        data = list([{"name": i.name, "product_type": i.product_type, "serial": i.serial, "date": i.date, "status": i.status} for i in inventories])
        return JsonResponse({"data": data}, safe=False)


    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            name = data.get('name')
            product_type = data.get('product_type')
            serial = data.get('serial')
            date = data.get('date')
            status = data.get('status')
            print(data)
            inventory = Inventory.objects.create(name=name, product_type=product_type, serial=serial, date=date, status=status)

            return JsonResponse({
                "message": "Inventory created successfully",
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def put(self, request, id, *args, **kwargs):
        try:
            data = json.loads(request.body)
            name = data.get('name')
            product_type = data.get('product_type')
            serial = data.get('serial')
            date = data.get('date')
            status = data.get('status')
            try:
                inventory = Inventory.objects.filter(serial=id).first()
            except Inventory.DoesNotExist:
                return JsonResponse({"error": "Product type not found"}, status=404)
            inventory.name = name
            inventory.product_type = product_type
            inventory.serial = serial
            inventory.date = date
            inventory.status = status
            inventory.save()

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
                inventory = Inventory.objects.get(id=id)
            except Inventory.DoesNotExist:
                return JsonResponse({"error": "Product type not found"}, status=404)
            inventory.delete()
            return JsonResponse({
                "message": "Product type deleted successfully"
            }, status=204)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
