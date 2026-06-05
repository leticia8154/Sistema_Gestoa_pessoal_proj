from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReceitaViewSet, DespesaViewSet

# Cria o roteador automático do DRF
router = DefaultRouter()
router.register(r'receitas', ReceitaViewSet, basename='receita')
router.register(r'despesas', DespesaViewSet, basename='despesa')

# As rotas mapeadas serão: /api/receitas/ e /api/despesas/
urlpatterns = [
    path('', include(router.urls)),
]