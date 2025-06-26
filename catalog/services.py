from .models import Product, Category


class ProductService:
    @staticmethod
    def get_products_by_category(category_id):
        return Product.objects.filter(category_id=category_id).select_related('category')
