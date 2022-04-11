#Variáveis
dia = int(input("digite o dia em que você nasceu: "))
mes = input("digite o mês em que você nasceu: ")

#aries
if (dia >= 21) and (mes == "março"):
    print("Seu signo é áries")
elif (dia <= 20) and (mes == "abril"):
    print("Seu signo é áries")

#touro
if (dia >= 21) and (mes == "abril"):
    print("Seu signo é touro")
elif (dia <= 20) and (mes == "maio"):
    print("Seu signo é touro")

#gemeos
if (dia >= 21) and (mes == "maio"):
    print("Seu signo é gêmeos")
elif (dia <= 20) and (mes == "junho"):
    print("Seu signo é gêmeos")

#cancer
if (dia >= 21) and (mes == "junho"):
    print("Seu signo é câncer")
elif (dia <= 22) and (mes == "julho"):
    print("Seu signo é câncer")

#leao
if (dia >= 23) and (mes == "julho"):
    print("Seu signo é leão")
elif (dia <= 22) and (mes == "agosto"):
    print("Seu signo é leão")

#virgem
if (dia >= 23) and (mes == "agosto"):
    print("Seu signo é virgem")
elif (dia <= 22) and (mes == "setembro"):
    print("Seu signo é virgem")

#libra
if (dia >= 23) and (mes == "setembro"):
    print("Seu signo é libra")
elif (dia <= 22) and (mes == "outubro"):
    print("Seu signo é libra")

#escorpiao
if (dia >= 23) and (mes == "outubro"):
    print("Seu signo é escorpião")
elif (dia <= 21) and (mes == "novembro"):
    print("Seu signo é escorpião")

#sagitario
if (dia >= 22) and (mes == "novembro"):
    print("Seu signo é sagitário")
elif (dia <= 21) and (mes == "dezembro"):
    print("Seu signo é sagitário")

#capricornio
if (dia >= 22) and (mes == "dezembro"):
    print("Seu signo é capricórnio")
elif (dia <= 20) and (mes == "janeiro"):
    print("Seu signo é capricórnio")

#aquario
if (dia >= 21) and (mes == "janeiro"):
    print("Seu signo é aquário")
elif (dia <= 18) and (mes == "fevereiro"):
    print("Seu signo é aquário")
    
#peixes
if (dia >= 19) and (mes == "fevereiro"):
    print("Seu signo é peixes")
elif (dia <= 20) and (mes == "março"):
    print("Seu signo é peixes")
    
print(";)")
