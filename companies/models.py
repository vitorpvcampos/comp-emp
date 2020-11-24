from django.db import models
from django.core.exceptions import ValidationError
from validate_docbr import CNPJ, CPF


def validate_cnpj(cnpj):
    cnpj = CNPJ()
    if cnpj.validate:
        return cnpj
    else:
        raise ValidationError('Invalid CNPJ')


def validate_cpf(cpf):
    cpf = CPF()
    if cpf.validate:
        return cpf
    else:
        raise ValidationError('Invalid CPF')


class Company(models.Model):
    company_name = models.CharField('Company', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=20, validators=[validate_cnpj], unique=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Employee(models.Model):
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=100)
    cpf = models.CharField('CPF', max_length=20, validators=[validate_cnpj], unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
