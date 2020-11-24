import graphene
import companies.schema


class Query(companies.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
