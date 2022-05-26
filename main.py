import sys, os, time

limpar = 'clear' if sys.platform == 'linux' else 'cls'

class Contatos:
  def __init__(self):
    self.contatos = {'Henrique': '99999', 'Jonas': '55555', 'Lincoln': '111111'}

  def contatosVazios(self):
    return True if not self.contatos else False

  def ordenarContatos(self):
    self.contatos = {nome:self.contatos[nome] for nome in sorted(self.contatos)}
  
  def cadastroContato(self):
    print(f"{'ADICIONAR CONTANTO':{'-'}^30}\n")

    nome = input("Qual o nome do contato: ")
    telefone = input("Qual o número do contato: ")
    self.contatos[nome] = telefone

    self.ordenarContatos()
    print("\n\nContato adicionado com sucesso!")
    time.sleep(1)

  def pesquisarContato(self):
    print(f"{'PESQUISAR CONTANTO':{'-'}^20}\n")

    if self.contatosVazios():
      print("Ainda não existem contatos na agenda.")
      time.sleep(1.5)
      return None

    for n,nome in enumerate(self.contatos.keys()):
      print(f"{n+1}. {nome}")
    print()
    
    nome = input("Qual o nome/índice do contato que deseja ver as informações?\n--> ")

    if nome.isdigit():
      nome = list(self.contatos.keys())[int(nome)-1]
    
    os.system(limpar)
    
    if nome in self.contatos.keys():
      print(f"Contato {list(self.contatos.keys()).index(nome) + 1}")
      print(f"Nome: {nome}")
      print(f"Telefone: {self.contatos[nome]}")
    elif nome not in self.contatos:
      print("Contato não encontrado.")
      time.sleep(1)
      os.system(limpar)
      
      while True:
        sub = int(input("Deseja pesquisar novamente?\n1 - Sim\n2 - Não\n--> "))

        if sub == 1:
          os.system(limpar)
          self.alterarContato()
        elif sub == 2:
          return None

        os.system(limpar)

    self.ordenarContatos()
    input("\n\nPressione qualquer tecla para voltar ao menu...\n")

  def listarContatos(self):
    print(f"{'LISTAR CONTANTOS':{'-'}^20}\n")

    if self.contatosVazios():
      print("Ainda não existem contatos na agenda.")
      time.sleep(1.5)
      return None

    print(f"{'-'*30}")
    for n, i in enumerate(self.contatos.keys()):
      print(f"Contato {n+1}\n")
      print(f"{'Nome:'} {i}")
      print(f"Telefone: {self.contatos[i]}")
      print(f"{'-'*30}")
      
    input("\n\nPressione qualquer tecla para voltar ao menu...\n")

  def alterarContato(self):
    print(f"{'ALTERAR CONTANTO':{'-'}^20}\n")

    if self.contatosVazios():
      print("Ainda não existem contatos na agenda.")
      time.sleep(1.5)
      return None

    for n,nome in enumerate(self.contatos.keys()):
      print(f"{n+1}. {nome}")
    print()
    
    nome = input("Qual nome do contato que você deseja alterar?\n--> ")

    if nome.isdigit():
      nome = list(self.contatos.keys())[int(nome)-1]

    os.system(limpar)
    
    if nome not in self.contatos:
      print("Contato não encontrado.")
      time.sleep(1)
      os.system(limpar)
      
      while True:
        sub = int(input("Deseja pesquisar novamente?\n1 - Sim\n2 - Não\n--> "))

        if sub == 1:
          os.system(limpar)
          self.alterarContato()
        elif sub == 2:
          return None

        os.system(limpar)

    while True:
      os.system(limpar)
      print(f"Informações do contato\n")
      print(f"{'Nome:'} {nome}")
      print(f"Telefone: {self.contatos[nome]}\n")
      
      sub = int(input("1 - Alterar Nome\n2 - Alterar Contato\n--> "))
      if sub == 1:
        novoNome = input("Qual o novo nome do contato?\n")
        self.contatos[novoNome] = self.contatos[nome]
        self.contatos.pop(nome)
        break
      if sub == 2:
        novoTelefone = int(input("Qual o novo número do contato?\n--> "))
        self.contatos[nome] = novoTelefone
        break
    self.ordenarContatos()

    print("\n\nContato alterado com sucesso!")
    time.sleep(1)

  def deletarContato(self):
    print(f"{'DELETAR CONTANTO':{'-'}^20}\n")

    if self.contatosVazios():
      print("Ainda não existem contatos na agenda.")
      time.sleep(1.5)
      return None

    for n,nome in enumerate(self.contatos.keys()):
      print(f"{n+1}. {nome}")
    print()
    
    nome = input("Qual nome/índice do contato que você deseja deletar?\n--> ")

    if nome.isdigit():
      nome = list(self.contatos.keys())[int(nome)-1]
      
    self.contatos.pop(nome)

    print("\n\nContato deletado com sucesso!")
    time.sleep(1)
    self.ordenarContatos()


def menu():
  contatos = Contatos()
  opcoes = {
    '1': contatos.cadastroContato,
    '2': contatos.pesquisarContato,
    '3': contatos.listarContatos,
    '4': contatos.alterarContato,
    '5': contatos.deletarContato,
    '6': sys.exit
    
  }
  while True:
    os.system(limpar)
    print(f"{'MENU':{'-'}^25}\n")
    print(f"1 - Cadastrar um contato")
    print(f"2 - Pesquisar um contato")
    print(f"3 - Listar contatos")
    print(f"4 - Alterar um contato")
    print(f"5 - Deletar um contato")
    print(f"6 - Sair")
  

    op = input("Insira a opção desejada: ")
    if op in ''.join(map(str, range(1,7))):
      os.system(limpar)
      opcoes[op]()
    else:
      print("Opção inválida.")
      time.sleep(1.2)

if __name__ == '__main__':
  menu()