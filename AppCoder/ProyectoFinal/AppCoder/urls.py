
from django.urls import path



from .views import agregaarticulos, inicio, bkp
# from .views import curso, cursoformulario, estudiantes, entregables, inicio, profesores

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('inicio/', inicio, name="Inicio"),
    # path('agrega-curso/<nombre>/<camada>', curso),
    path('backup/', bkp, name="backup"),
    #path('recuperar_articulos/', recuperar_articulos, name="recuperar_articulos"),
    #path('agregaarticulos/', agregaarticulos, name="agregaarticulos"),
    # path('entregables/', entregables, name="Entregables"),
    #path('pedidormulario/', pedidoformulario, name="pedidoformulario"),
    
]

