import yt_dlp
import random
import os
import requests

def calculadora ():
    
    os.system ('cls')
    
    def somar (x,y):
        soma = x+y
        print ("O resultado da soma é: ",soma)
        print ("-----------------------------------------")
        return soma;
    
    def subtrair (x,y):
        subtracao = x-y
        print ("O resultado da subtração é: ",subtracao)
        print ("-----------------------------------------")
        return subtracao;
    
    def dividir (x,y):
        divisao = x/y
        print ("O resultado da divisão é: ",divisao)
        print ("-----------------------------------------")
        return divisao;
    
    def multiplicar (x,y):
        multiplicacao = x*y
        print ("O resultado da multiplicação é: ",multiplicacao)
        print ("-----------------------------------------")
        return multiplicacao;
    
    while True:
        print ("[1]. Somar")
        print ("[2]. Subtração")
        print ("[3]. Divisão")
        print ("[4]. Multiplicação")
        print ("[0]. Encerrar programa")
        escolha = int(input("Digite o numero de sua escolha: "))
        
        if escolha == 0:
            break
    
        os.system('cls')
    
        numero_1 = int(input("Digite o primeiro numero: "))
        
        if escolha == 1:
            print ("+")
            
        elif escolha == 2:
            print ("-")
            
        elif escolha == 3:
            print ("/")
            
        elif escolha == 4:
            print ("*")

        numero_2 = int(input("Digite o segundo numero: "))
    
        if escolha == 1:
            somar(numero_1,numero_2)
    
        elif escolha == 2:
            subtrair(numero_1,numero_2)
        
        elif escolha == 3:
            dividir(numero_1,numero_2)
        
        elif escolha == 4:
            multiplicar(numero_1,numero_2)
        
        else:
            print ("Digite uma opção valida ]: ")
    
    return;

def calcular_media ():
    
    os.system ('cls')
    
    def media_turma():
        
        contador = 0
        nota = 0
        
        quantidade_alunos = int(input("Digite a quantidade de alunos: "))
        
        os.system ('cls')
        
        while contador < quantidade_alunos:
            contador += 1
            nota += int(input("Digite a nota do aluno: "))
            
        nota_final = int(nota/quantidade_alunos)
        #developed by vrg8778
        os.system ('cls')
        print ("--------------------------")
        print ("A media da classe é ",nota_final)
        print ("--------------------------")
        
        return;
    
    def media_aluno():
        contador = 0
        nota = 0
        
        quantidade_alunos = int(input("Digite a quantidade de materias: "))
        
        os.system ('cls')
        
        while contador < quantidade_alunos:
            contador += 1
            nota += int(input("Digite a nota da materia: "))
            
        nota_final = int(nota/quantidade_alunos)
        os.system ('cls')
        print ("--------------------------")
        print ("A media do aluno é ",nota_final)
        print ("--------------------------")
        return;
    
    while True:
        
        print ("[1]. Calcular media dos alunos")
        print ("[2]. Calcular media da turma")
        print ("[0]. Encerrar programa")
    
        escolha = int(input("Digite a escolha: "))
    
        if escolha == 1:
            media_aluno()
            
        elif escolha == 2:
            media_turma()
            
        elif escolha == 0:
            break;
        
        else:
            print ("Digite um numero valido!")
    
    return;

def calcular_imc():
    
    os.system ('cls')
    
    print ("Calcular IMC")
    print ("Use ponto e nao virgula")
    print ("---------------------------------------")
    
    peso = float(input("Digite seu peso em KG: "))
    altura = float(input("Digite sua altura em metros: "))
    
    imc = peso / (altura ** 2)
    print (f"Seu IMC é {imc:.2f}")
    
    return;

def conversor_temperatura():
    
    os.system ('cls')
    
    while True:
        print ("[1]. Converter Fahrenheit para Celsius")
        print ("[2]. Converter Celsius para Fahrenheit")
        print ("[0]. Encerrar programa")
    
        escolha = int(input("Digite sua escolha: "))
    
        if escolha == 1:
            f = int(input("Digite o Fahrenheit: "))
            c = (f-32)*5/9
            print (f"{f}°F é igual a {c:.2f}°C")
        
        elif escolha == 2:
            c = int(input("Digite o  Celsius: "))
            f = (c*9/5)+32
            print (f"{c}°C é igual a {f:.2f}°F")
            
        elif escolha == 0:
            break;
        
        else:
            print("Digite uma opção valida")
            
    return;

def baixar_imagem():
    
    os.system ('cls')
    
    url = input("Digite sua URL: ")
    nome_do_arquivo = input("Digite o nome do arquivo:  ")
    
    os.system ('cls')
    
    print ("[1]. Baixar imagem PNG")
    print ("[2]. Baixar imagem JPG")
    
    escolha = int(input("Digite sua escolha: "))
    
    if escolha == 1:
        nome_do_arquivo += ".png"
        
    elif escolha == 2:
        nome_do_arquivo += ".jpg"
        
    
    try:
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            with open (nome_do_arquivo, 'wb') as arquivo:
                arquivo.write(resposta.content)
            print (f"Imagem salva com sucesso {nome_do_arquivo}")
            
        else:
            print ("Erro ao baixar a imagem")
            
    except Exception as e:
        print ("Erro", e)
    
    return;

def baixar_video_yt():
    
    os.system ('cls')
    
    url = input("digite a URL o video o YouTube: ")
    
    try:
        ydl_opts = {
            'format': 'best', 
            'noplaylist': True
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print ("Baixando...")
            ydl.download([url])
            print("Download concluido!")
        
    except Exception as e:
        print (f"Erro ao fazer download {e}")
    
    return;

def conversor_de_moeda():
    
    return;

while True:
    os.system ('cls')
    print ("-------------------------------------")
    print ("Utilidades")
    print ("[1]. Calculadora")
    print ("[2]. Calculador de medias")
    print ("[3]. Calculador de IMC")
    print ("[4]. Conversor de temperatura")
    print ("[5]. Baixar imagens")
    print ("[6]. Baixar video Youtube")
    print ("[7]. Conversar de moeda")
    print ("[0]. Encerrar programa")
    
    escolha = int(input("Digite a sua escolha: "))
    
    if escolha == 1:
        calculadora()
        
    elif escolha == 2:
        calcular_media()
        
    elif escolha == 3:
        calcular_imc()
        
    elif escolha == 4:
        conversor_temperatura()
        
    elif escolha == 5:
        baixar_imagem()
        
    elif escolha == 6:
        baixar_video_yt()
        
    elif escolha == 7:
        conversor_de_moeda()
        
    elif escolha == 0:
        break
        
    else:
        print("Digite uma esscolha valida")
        
####### DESENVOLVIDO POR VICTOR GABRIEL F.B. DIAS #######