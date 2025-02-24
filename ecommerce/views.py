# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render

from .models import Product
from django.core.paginator import Paginator


items_per_page = 2
def products_view(request):
    try:
        products = Product.objects.all()
        paginator = Paginator(products, items_per_page)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        response = {
            'products': [product.to_dict() for product in page_obj],
            'has_next_page': page_obj.has_next(),
            'next_page': page_obj.next_page_number() if page_obj.has_next() else None,
            'has_previous_page': page_obj.has_previous(),
            'previous_page': page_obj.previous_page_number() if page_obj.has_previous() else None,
        }
        return JsonResponse({"data": response}, status=200)
    except Exception as e :
        return JsonResponse({"error": str(e)}, status=500)



def specific_product_view(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        response = product.to_dict()
        return JsonResponse(response, status=200)
    except Product.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=404)
    except Exception as e :
        return JsonResponse({"error": str(e)}, status=500)

def get_product_by_id(request, id):
    try:
        product = Product.objects.get(pk=id)
        response = product.to_dict()
        return JsonResponse({"data": response}, status=200)
    except Product.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=404)
    except Exception as e :
        return JsonResponse({"error": str(e)}, status=500)