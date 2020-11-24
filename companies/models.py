from django.db import models


class Company(models.Model):
    company_name = models.CharField('Company', max_length=100)
    cnpj = models.CharField('CNPJ (somente números)', max_length=14, unique=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Employee(models.Model):
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=100)
    cpf = models.CharField('CPF (somente números)', max_length=11, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
