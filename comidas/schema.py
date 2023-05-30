import graphene
from graphene_django import DjangoObjectType
from .models import Comida
from users.schema import UserType
from comidas.models import Comida, Vote
from graphql import GraphQLError
from django.db.models import Q


class ComidaType(DjangoObjectType):
    class Meta:
        model = Comida


# Add after the LinkType
class VoteType(DjangoObjectType):
    class Meta:
        model = Vote
        

class Query(graphene.ObjectType):
    comidas = graphene.List(ComidaType, search=graphene.String())
    votes = graphene.List(VoteType)

    def resolve_comidas(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(nombre__icontains=search) 
                #| Q(description__icontains=search)
            )
            return Comida.objects.filter(filter)
        
        return Comida.objects.all()
    
    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()
    
    
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
    posted_by = graphene.Field(UserType)

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
        
        user = info.context.user or None
        
        comida = Comida(
                        nombre=nombre, 
                        tipo_platillo=tipo_platillo, 
                        calorias=calorias, 
                        proteinas=proteinas,
                        pais_origen=pais_origen, 
                        ingredientes=ingredientes, 
                        saludable=saludable, 
                        tiempo_coccion=tiempo_coccion,
                        dificultad_preparacion=dificultad_preparacion, 
                        utensilios_requeridos=utensilios_requeridos,
                        posted_by=user,
                        )
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
            posted_by = comida.posted_by,
        )


# Add the CreateVote mutation
class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    platillo = graphene.Field(ComidaType)

    class Arguments:
        platillo_id = graphene.Int()

    def mutate(self, info, platillo_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged to vote!')

        platillo = Comida.objects.filter(id=platillo_id).first()
        if not platillo:
            raise Exception('Invalid Platillo!')

        Vote.objects.create(
            user=user,
            platillo=platillo,
        )

        return CreateVote(user=user, platillo=platillo)



# 4
class Mutation(graphene.ObjectType):
    create_comida = CreateComida.Field()
    create_vote = CreateVote.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
