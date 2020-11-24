import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Company, Employee


class CompanyNode(DjangoObjectType):
    class Meta:
        model = Company
        filter_fields = ['id', 'company_name', 'cnpj']
        interfaces = (graphene.relay.Node,)


class EmployeeNode(DjangoObjectType):
    class Meta:
        model = Employee
        filter_fields = ['id', 'company', 'name', 'cpf']
        interfaces = (graphene.relay.Node,)


class Query(object):
    company = graphene.relay.Node.Field(CompanyNode)
    all_companies = DjangoFilterConnectionField(CompanyNode)

    employee = graphene.relay.Node.Field(EmployeeNode)
    all_employees = DjangoFilterConnectionField(EmployeeNode)
