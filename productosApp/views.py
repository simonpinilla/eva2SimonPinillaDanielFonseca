from django.shortcuts import render

# Create your views here.


# Create your views here.
def index(request):
    return render(request, 'productosApp/index.html')

def juguetes(request):

    data = {
        "titulo": "JUGUETES",
        "producto1": "LEGO STAR WARS",
        "producto2": "MONOPOLY",
        "producto3": "LANZADOR NERF",
        'url': '/www.inacap.cl',
        'imagen1': 'images/juguetes/producto1.png',
        'imagen2': 'images/juguetes/producto2.png',
        'imagen3': 'images/juguetes/producto3.png',
    }
    return render(request, 'productosApp/catalogo.html', data)

def electronica(request):
    data = {
        "titulo": "ELECTRÓNICA",
        "producto1": "TV LG",
        "producto2": "APPLE TV",
        "producto3": "APPLE WATCH",
        'url': '/www.inacap.cl',
        'imagen1': 'images/electronica/producto1.png',
        'imagen2': 'images/electronica/producto2.png',
        'imagen3': 'images/electronica/producto3.png',
    }
    return render(request, 'productosApp/catalogo.html', data)

def ropa(request):
    data = {
        "titulo": "ROPA",
        "producto1": "POLERON BUFFALO",
        "producto2": "POLERON MAUI",
        "producto3": "CAMISA LEVIS",
        'url': '/www.inacap.cl',
        'imagen1': 'images/ropa/producto1.png',
        'imagen2': 'images/ropa/producto2.png',
        'imagen3': 'images/ropa/producto3.png',
    }
    return render(request, 'productosApp/catalogo.html', data)


