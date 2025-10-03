from django.shortcuts import render

def index(request):
    """
    Esta función prepara una lista de diccionarios con datos de casas
    para ser mostrados en una página web.
    """
    casas = [
        {
            'id': 1,
            'nombre': 'Casa Moderna en la Ciudad',
            'ubicacion': 'Centro Urbano',
            'precio': '250,000 USD',
            'habitaciones': 3,
            'banos': 2,
            'metros_cuadrados': 150,
            'imagen': 'https://via.placeholder.com/400x250?text=Casa+Moderna'
        },
        {
            'id': 2,
            'nombre': 'Acogedora Cabaña Rural',
            'ubicacion': 'Afueras del Pueblo',
            'precio': '180,000 USD',
            'habitaciones': 2,
            'banos': 1,
            'metros_cuadrados': 100,
            'imagen': 'https://via.placeholder.com/400x250?text=Cabaña+Rural'
        },
        {
            'id': 3,
            'nombre': 'Lujosa Villa con Vistas al Mar',
            'ubicacion': 'Costa',
            'precio': '750,000 USD',
            'habitaciones': 5,
            'banos': 4,
            'metros_cuadrados': 300,
            'imagen': 'https://via.placeholder.com/400x250?text=Villa+Lujosa'
        }
    ]

    context = {
        'lista_casas': casas
    }
    return render(request, 'index.html', context)
