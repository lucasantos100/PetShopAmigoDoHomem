# LUCAS VINICIUS DOS SANTOS, BRUNO VITOR DOS SANTOS, KAUAN DOS ANJOS

import os
import platform

def limpar_tela():

    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

class Animal:
    def __init__(self, nome, idade, especie, servico):
        self._nome = nome
        self._idade = idade
        self._especie = especie
        self._servico = servico

    def calcular_preco_servico(self):
        pass

class Cachorro(Animal):
    def calcular_preco_servico(self):
        return 50

class Gato(Animal):
    def calcular_preco_servico(self):
        return 40

class Passaro(Animal):
    def calcular_preco_servico(self):
        return 30

def menu():
    print("\nMenu:")
    print("1. Cadastrar animal")
    print("2. Consultar animal")
    print("3. Calcular preço de serviço")
    print("4. Sair")

def main():
    limpar_tela()
    animais = {}
    
    while True:
        menu()

        opcao = input("\nEscolha uma opção: ")
        
        #opcao 1 cadastro
        if opcao == '1':
            nome = input("\nNome do animal: ")
            idade = int(input("Idade do animal: "))
            especie = input("Espécie do animal (cachorro/gato/passaro): ").lower()
            servico = input("Serviço para ser executado (tosa/banho/vacina): ").lower()

            if especie == "cachorro":
                animal = Cachorro(nome, idade, especie, servico)
            elif especie == "gato":
                animal = Gato(nome, idade, especie, servico)
            elif especie == "passaro":
                animal = Passaro(nome, idade, especie, servico)
            else:
                print("\nEspécie inválida!")
                continue

            animais[nome] = animal
            print(f"[{especie} {nome} de {idade} anos cadastrado!]")

        #opcao 2 consultar animal cadastardo
        elif opcao == '2':
            if not animais:
                print("\nNenhum animal cadastrado.")
                continue
            else:
                print("\nAnimais cadastrados:")
                for i, nome in enumerate(animais.keys(), start=1):
                    print(f"{i}. {nome}")
                
            nome = input("\nDigite o nome do animal que deseja consultar: ")
            
            if nome in animais:
                animal = animais[nome]
                print(f"\n[Nome: {animal._nome}, Idade: {animal._idade}, Espécie: {animal._especie}, Serviço: {animal._servico}]")
            else:
                print("Animal não encontrado.")

        #opcao 3 calcular preço para o animal em questao
        elif opcao == '3':
            if not animais:
                print("\nNenhum animal cadastrado.")
                continue
            else:
                print("\nAnimais cadastrados:")
                for i, nome in enumerate(animais.keys(), start=1):
                    print(f"{i}. {nome}")
            if animais:
                nome = input("\nDigite o nome do animal para calcular o preço do serviço: ")
                if nome in animais:
                    animal = animais[nome]
                    preco = animal.calcular_preco_servico()
                    print(f"[O preço do serviço para {animal._nome} é R$ {preco}.]")
                else:
                    print("Animal não encontrado.")

        #opcao 4 saida do programa
        elif opcao == '4':
            print("Saindo do programa.")
            break

        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()