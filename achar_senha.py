from random import*
import time

def senha():
    tempo_inicial = time.time()

    senha= input("Digite a senha que vc quer encontrar: ")

    letras=['a','b','c','d','e','f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t',
            'u','v','w','x','y','z','ç','1','2','3',
            '4','5','6','7','8','9','0','!','@','#',
            '$','%','*','(',')','{','}','^','¨','?',
            'A','B','C','D','E','F','G','H','I','J',
            'K','L','M','N','O','P','Q','R','S','T',
            'U','V','W','X','Y','Z']

    achar=""
    while(achar != senha):
        achar = ""
        for letra in senha:
            achar_letra = letras[randint(0,75)]
            achar = str(achar_letra) + str(achar)
        print(achar)

    tempo_final = time.time()

    tempo_codigo = tempo_final - tempo_inicial
    print(f"Demorou {tempo_codigo:.2f} segundos para encontar a senha: {achar}")
    novaOperacao()
    

def novaOperacao():
	resposta = input("\nDeseja fazer uma nova operação? S/N ")

	if (resposta == "S" or resposta == "s" or resposta == "sim" or resposta == "SIM"):
		senha()
	elif (resposta == "N" or resposta == "n" or resposta == "nao" or resposta == "NAO"):
		exit()
	else:
		novaOperacao()

senha()