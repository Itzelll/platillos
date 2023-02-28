import graphene
from graphene_django import DjangoObjectType

from .models import Comida


class ComidaType(DjangoObjectType):
    class Meta:
        model = Comida


class Query(graphene.ObjectType):
    comidas = graphene.List(ComidaType)

    def resolve_comidas(self, info, **kwargs):
        return Comida.objects.all()