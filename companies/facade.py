import re
import graphene
from graphene_django.utils import camelize
from django.core.exceptions import ValidationError


def validate_cpf(cpf):
    cpf = ''.join(re.findall('\d', str(cpf)))

    if (not cpf) or (len(cpf) < 11):
        raise ValidationError(f"{cpf} is not a valid CPF.")

    cpf_number = list(map(int, cpf))
    print(cpf_number)
    new_cpf_number = cpf_number[:9]

    while len(new_cpf_number) < 11:
        r = sum([(len(new_cpf_number) + 1 - i) * v for i, v in enumerate(new_cpf_number)]) % 11

        if r > 1:
            f = 11 - r
        else:
            f = 0
        new_cpf_number.append(f)

    if new_cpf_number == cpf_number:
        return cpf
    raise ValidationError(f"{cpf} is not a valid CPF.")


def validate_cnpj(cnpj):
    cnpj = ''.join(re.findall('\d', str(cnpj)))

    if (not cnpj) or (len(cnpj) < 14):
        raise ValidationError(f"{cnpj} is not a valid CNPJ.")

    cnpj_number = list(map(int, cnpj))
    print(cnpj_number)
    new_cnpj_number = cnpj_number[:12]

    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    while len(new_cnpj_number) < 14:
        r = sum([x * y for (x, y) in zip(new_cnpj_number, prod)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        new_cnpj_number.append(f)
        prod.insert(0, 6)

        if new_cnpj_number == cnpj_number:
            return cnpj
    raise ValidationError(f"{cnpj} is not a valid CNPJ.")


class ErrorType(graphene.Scalar):
    @staticmethod
    def serialize(errors):
        if isinstance(errors, dict):
            if errors.get("__all__", False):
                errors["non_field_errors"] = errors.pop("__all__")
            return camelize(errors)
        raise Exception("'errors' should be dict!")
