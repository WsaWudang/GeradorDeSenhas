from random import random, choice
import string

def senha():
	valores = string.ascii_letters #todas as letras
	valores += string.digits #todos ps números 
	valores += string.punctuation #caracteres especiais 

	tamanho = int(input("Digite o número de caracteres que deseja que a senha tenha: "))
	senha = ""

	for i in range (tamanho):
		senha += choice(valores)

	print(f"\nA senha aleatória é: {senha}")
	nova_senha()

def nova_senha():
	resposta = input("\nDeseja fazer uma nova senha? S/N ")

	if (resposta == "S" or resposta == "s" or resposta == "sim" or resposta == "SIM"):
		senha()
	elif (resposta == "N" or resposta == "n" or resposta == "nao" or resposta == "NAO"):
		exit()
	else:
		nova_senha()

senha()