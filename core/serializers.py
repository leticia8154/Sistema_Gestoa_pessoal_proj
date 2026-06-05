from rest_framework import serializers
from .models import Receita, Despesa

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'  # Inclui automaticamente todos os campos do Model


class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'  # Inclui automaticamente todos os campos do Model