from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("catalog/product_list/", ProductListView.as_view(), name="product_list"),
    path("catalog/create/", ProductCreateView.as_view(), name="product_create"),
    path("catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("catalog/<int:pk>/detail/", ProductDetailView.as_view(), name="product_detail"),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete")
]
