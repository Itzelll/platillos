import graphene

import comidas.schema


class Query(comidas.schema.Query, graphene.ObjectType):
    pass

class Mutation(comidas.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
