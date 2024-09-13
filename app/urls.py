from django.contrib import admin
from django.urls import path

from app.inventory.views.inventory_view import InventoryView
from app.inventory.views.product_type_view import ProductTypeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventories/', InventoryView.as_view(), name="Inventories"),
    path('inventories/<str:id>/', InventoryView.as_view(), name="InventoriesID"),
    path(r'product-types/', ProductTypeView.as_view(), name="ProductType"),
    path('product-types/<int:id>/', ProductTypeView.as_view(), name="ProductTypeID")
]
