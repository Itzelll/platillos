import graphene

import comidas.schema


class Query(comidas.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)