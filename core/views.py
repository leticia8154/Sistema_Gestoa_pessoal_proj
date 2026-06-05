from rest_framework import viewsets
from .models import Receita, Despesa
from .serializers import ReceitaSerializer, DespesaSerializer

class ReceitaViewSet(viewsets.ModelViewSet):
    """
    Controlador que fornece automaticamente as ações de CRUD para as Receitas.
    """
    queryset = Receita.objects.all().order_by('-data') # Ordena pelas datas mais recentes
    serializer_class = ReceitaSerializer


class DespesaViewSet(viewsets.ModelViewSet):
    """
    Controlador que fornece automaticamente as ações de CRUD para as Despesas.
    """
    queryset = Despesa.objects.all().order_by('-data') # Ordena pelas datas mais recentes
    serializer_class = DespesaSerializer