from django.contrib import admin
from .models import Company, Employee


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'cnpj')


@admin.register(Employee)
class CompanyEmployee(admin.ModelAdmin):
    list_display = ('id', 'company', 'name', 'cpf')
