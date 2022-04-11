from mailbox import linesep
import os

# Fazer perguntas

def start():
    #apresentação
    print("Olá, bem-vindo(a) a apresentação do curso de informática da EEEP Comendador Miguel Gurgel!")
    #pegar a informação do nome
    name = input("Digite seu nome: ")

    while True:

        #menu de perguntas mais frequentes
        ask = input(   
            f"###################################################### {os.linesep} Qual a sua dúvida? {os.linesep} [1] - Quantos anos dura o curso? {os.linesep} [2] - Qual a grade curricular do curso? {os.linesep} [3] - O curso de Informática é bem aceito no mercado de trabalho? {os.linesep} [4] - Qual o salário médio de Técnico de Informática? {os.linesep} [5] - Por que escolher informática? {os.linesep} {os.linesep} Se a sua dúvida não estiver exposta aqui, digite 6 e veja as redes sociais e contatos da escola para ser respondido. {os.linesep}###################################################### {os.linesep}" 
            )

        #processar resposta

        resp(ask, name)

# Processar resposta

def resp (ask,name):
    if ask == "1":
        print(f"{os.linesep}Olá, {name}, o curso tem duração total de 6 semestres, sendo o sexto semestre resevado para o estágio na área de T.I.{os.linesep}")
    elif ask == "2":
        print(f"{os.linesep}Olá, {name}, o curso forma profissionais que possuam uma visão crítica que lhes permita participar ativamente das mudanças da realidade nacional vigente, desenvolvendo uma boa visão crítica, não só da empresa, mas também do contexto social, político e econômico em que ela se insere. Que estejam aptos há para atuar em atividades de concepção, especificação, implementação, avaliação, suporte e manutenção de sistemas e de tecnologias de processamento e transmissão de dados e informações.{os.linesep}")
    elif ask == "3":
        print(f"{os.linesep}Olá, {name}, com o crescimento da Internet e das redes de computadores, além do aumento do número de computadores em residências e empresas, o Técnico em Informática tem sido um profissional bastante requisitado. Ele pode atuar com vínculo empregatício ou de forma autônoma, nos limites de sua responsabilidade técnica, junto a residências, indústrias, empresas comerciais ou instituições governamentais que utilizem tecnologias de informação. Pode trabalhar com atividades de manutenção de equipamentos de Informática; manutenção, instalação e configuração de redes de computadores; assessoria, consultoria e treinamento em Informática; desenvolvimento de softwares; e provedores de acesso à Internet.{os.linesep}")
    elif ask == "4":
        print(f"{os.linesep}Olá, {name}, o salário nessa área é muito relativo, pois depende da área de atuação. Mas, em média o salário de um profissional do setor de tecnologia é em média R$ 2.000,00.{os.linesep}")
    elif ask == "5":
        print(f"{os.linesep}Olá, {name}, informática é o curso da tecnologia. Dado o crescimento do setor tecnológico; nunca vai faltar espaço para os técnicos em T.I.{os.linesep}")
    elif ask == "6":
        print(f"Instagram: @eeepmiguelgurgel {os.linesep}Telefone para contato: 3101-2071{os.linesep}A escola está localizada em Rua José Baíma, 340, Fortaleza, Brasil. {os.linesep}")
    else:
        print(f"Digite apenas 1, 2, 3, 4, 5 ou 6, por favor, {name}.")

if __name__ == '__main__':
    start()