from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def indexjuegos(request):
    return render(request, 'juegos/index.html')

def fortnite(request):
    data = {
        "titulo": "Fortnite",
        "imagen": "images/fortnite.png",
        "descripcion": "Fortnite es un videojuego del año 2017 desarrollado por la empresa Epic Games lanzado como diferentes paquetes de software que presentan diferentes modos de juego, pero que comparten el mismo motor de juego y mecánicas. Fue anunciado en los premios Spike Video Game Awards en 2011."
    }
    return render(request, 'juegos/index.html', data)

def valorant(request):
    data = {
        "titulo": "Valorant",
        "imagen": "images/valorant.png",
        "descripcion": "Valorant es un hero shooter en primera persona multijugador gratuito desarrollado y publicado por Riot Games. El juego se anunció por primera vez con el nombre en clave Project A en octubre de 2019. Fue lanzado para Microsoft Windows el 2 de junio de 2020 después de su beta cerrada lanzada el 7 de abril de 2020"
    }
    return render(request, 'juegos/index.html', data)

def lol(request):
    data = {
        "titulo": "League of Legend",
        "imagen": "images/lol.png",
        "descripcion": "League of Legends, es un videojuego multijugador de arena de batalla en línea desarrollado y publicado por Riot Games. Inspirándose en Defense of the Ancients, un mapa personalizado para Warcraft III, los fundadores de Riot buscaron desarrollar un juego independiente del mismo género."
    }
    return render(request, 'juegos/index.html', data)

