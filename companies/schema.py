import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Company, Employee
from graphql_relay.node.node import from_global_id


class CompanyNode(DjangoObjectType):
    class Meta:
        model = Company
        filter_fields = ['id', 'company_name', 'cnpj']
        interfaces = (graphene.relay.Node,)


class EmployeeNode(DjangoObjectType):
    class Meta:
        model = Employee
        filter_fields = ['id', 'company__company_name', 'name', 'cpf']
        interfaces = (graphene.relay.Node,)


class CreateCompany(graphene.relay.ClientIDMutation):
    company = graphene.Field(CompanyNode)

    class Input:
        company_name = graphene.String(required=True)
        cnpj = graphene.String(required=True)

    def mutate_and_get_payload(root, info, **input):
        company = Company(
            company_name=input.get('company_name'),
            cnpj=input.get('cnpj'),
        )
        company.save()

        return CreateCompany(company=company)


class CreateEmployee(graphene.relay.ClientIDMutation):
    employee = graphene.Field(EmployeeNode)

    class Input:
        company = graphene.String(required=True)
        name = graphene.String(required=True)
        cpf = graphene.String(required=True)

    def mutate_and_get_payload(root, info, **input):
        employee = Employee(
            company=Company.objects.get(company_name=input.get('company')),
            name=input.get('company'),
            cpf=input.get('cpf'),
        )
        employee.save()

        return CreateEmployee(employee=employee)


class UpdateCompany(graphene.relay.ClientIDMutation):
    company = graphene.Field(CompanyNode)

    class Input:
        id = graphene.String()
        company_name = graphene.String()
        cnpj = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        company = Company.objects.get(pk=from_global_id(input.get('id'))[1])
        company.company_name = input.get('company_name')
        company.cnpj = input.get('cnpj')
        company.save()

        return UpdateCompany(employee=company)


class UpdateEmployee(graphene.relay.ClientIDMutation):
    employee = graphene.Field(EmployeeNode)

    class Input:
        id = graphene.String()
        company = graphene.String()
        name = graphene.String()
        cpf = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        employee = Employee.objects.get(pk=from_global_id(input.get('id'))[1])
        employee.company = Company.objects.get(company_name=input.get('company'))
        employee.name = input.get('name')
        employee.cpf = input.get('cpf')
        employee.save()

        return UpdateEmployee(employee=employee)


class DeleteCompany(graphene.relay.ClientIDMutation):
    company = graphene.Field(CompanyNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        company = Company.objects.get(pk=from_global_id(input.get('id'))[1])
        company.delete()

        return DeleteEmployee(company=company)


class DeleteEmployee(graphene.relay.ClientIDMutation):
    employee = graphene.Field(EmployeeNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        employee = Employee.objects.get(pk=from_global_id(input.get('id'))[1])
        employee.delete()

        return DeleteEmployee(employee=employee)


class Query(object):
    company = graphene.relay.Node.Field(CompanyNode)
    all_companies = DjangoFilterConnectionField(CompanyNode)

    employee = graphene.relay.Node.Field(EmployeeNode)
    all_employees = DjangoFilterConnectionField(EmployeeNode)


class Mutation(graphene.AbstractType):
    create_company = CreateCompany.Field()
    create_employee = CreateEmployee.Field()
    update_company = UpdateCompany.Field()
    update_employee = UpdateEmployee.Field()
    delete_company = DeleteCompany.Field()
    delete_employee = DeleteEmployee.Field()
