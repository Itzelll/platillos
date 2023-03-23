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

# ...code
# 1
class CreateComida(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    tipo_platillo = graphene.String()
    calorias = graphene.Float()
    proteinas = graphene.Float()
    pais_origen = graphene.String()
    ingredientes = graphene.String()
    saludable = graphene.String()
    tiempo_coccion = graphene.Int()
    dificultad_preparacion = graphene.Int()
    utensilios_requeridos = graphene.String()

    # 2 - Argumentos que se van y consume el API
    class Arguments:
        nombre = graphene.String()
        tipo_platillo = graphene.String()
        calorias = graphene.Float()
        proteinas = graphene.Float()
        pais_origen = graphene.String()
        ingredientes = graphene.String()
        saludable = graphene.String()
        tiempo_coccion = graphene.Int()
        dificultad_preparacion = graphene.Int()
        utensilios_requeridos = graphene.String()

    # 3
    def mutate(self, info, nombre, tipo_platillo, calorias, proteinas, pais_origen, ingredientes,
               saludable, tiempo_coccion, dificultad_preparacion, utensilios_requeridos):
        comida = Comida(nombre=nombre, 
                        tipo_platillo=tipo_platillo, 
                        calorias=calorias, 
                        proteinas=proteinas,
                        pais_origen=pais_origen, 
                        ingredientes=ingredientes, 
                        saludable=saludable, 
                        tiempo_coccion=tiempo_coccion,
                        dificultad_preparacion=dificultad_preparacion, 
                        utensilios_requeridos=utensilios_requeridos)
        comida.save() #insert into Comida(...) values(...)

        return CreateComida(
            id = comida.id,
            nombre = comida.nombre,
            tipo_platillo = comida.tipo_platillo,
            calorias = comida.calorias,
            proteinas = comida.proteinas,
            pais_origen = comida.pais_origen,
            ingredientes = comida.ingredientes,
            saludable = comida.saludable,
            tiempo_coccion = comida.tiempo_coccion,
            dificultad_preparacion = comida.dificultad_preparacion,
            utensilios_requeridos = comida.utensilios_requeridos,
        )


# 4
class Mutation(graphene.ObjectType):
    create_comida = CreateComida.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)