from Cpf_Cnpj import Documento
from Telefones_Br import TelefonesBr
from datas_br import DataBr


cpf = 43120720780
objeto_1 = Documento.criar_novo(cpf)

cnpj = 54146246000103
objeto_2 = Documento.criar_novo(cnpj)

print(objeto_1)
print(objeto_2)

texto = "rua america, 134, tel.:551144117769-Atibaia, 54146246000103 egeg,egegeg 43120720780"
teste = TelefonesBr(texto)
print(teste)

hoje = DataBr()
print(hoje)
