from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def criar_novo(documento):
        doc_str = str(documento)
        if len(doc_str) == 11:
            return Cpf(doc_str)
        if len(doc_str) == 14:
            return Cnpj(doc_str)
        else:
            raise ValueError("Documento incorreto!")


class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF INVÁLIDO!!")

    def __str__(self):
        return self.formata_cpf()

    @staticmethod
    def valida_cpf(cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("CPF INVÁLIDO!!")

    def formata_cpf(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)


class Cnpj:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ INVÁLIDO!!")

    def __str__(self):
        return self.formata_cnpj()

    @staticmethod
    def valida_cnpj(cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("Falta Dígitos!!")

    def formata_cnpj(self):
        cnpj_mask = CNPJ()
        return cnpj_mask.mask(self.cnpj)
