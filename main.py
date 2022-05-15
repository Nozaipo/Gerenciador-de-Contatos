import sys, os, time

limpar = 'clear' if sys.platform == 'linux' else 'cls'

class Contatos:
  def __init__(self):
    self.contatos = {}

  def cadastroContato(self):
    print(f"{'ADICIONAR CONTANTO':{'-'}^20}\n")

    nome = input("Qual o nome do contato: ")
    telefone = input("Qual o número do contato: ")
    self.contatos[nome] = telefone

  def pesquisarContato(self):
    print(f"{'PESQUISAR CONTANTO':{'-'}^20}\n")
    nome = input("Qual o nome do contato que deseja procurar?\n")

    os.system(limpar)
    
    if nome in self.contatos.keys():
      print(f"Contato {list(self.contatos.keys()).index(nome) + 1}")
      print(f"Nome: {nome}")
      print(f"Telefone: {self.contatos[nome]}")
    else:
      print("Contato inexistente.")

    time.sleep(1.5)

  def listarContatos(self):
    print(f"{'LISTAR CONTANTOS':{'-'}^20}\n")

    if self.contatos == {}:
      print("Ainda não existem contatos na agenda.")
      time.sleep(1.5)
      return None

    for n, i in enumerate(self.contatos.keys()):
      print(f"Contato {n+1}")
      print(f"{'Nome:'} {i}")
      print(f"Telefone: {self.contatos[i]}")
      print()
    time.sleep(2)

  def alterarContato(self):
    print(f"{'ALTERAR CONTANTO':{'-'}^20}\n")

    if self.contatos == {}:
      print("Ainda não existem contatos na agenda.")
      time.sleep(1.5)
      return None

    print("Deixe em branco para sair.\n")
    nome = input("Qual nome do contato que você deseja alterar?\n--> ")

    if nome == '':
      return None

    if nome not in self.contatos:
      print("Cliente não encontrado.")
      time.sleep(1)
      os.system(limpar)
      
      while True:
        sub = int(input("Deseja pesquisar novamente?\n1 - Sim\n2 - Não\n--> "))

        if sub == 1:
          os.system(limpar)
          self.alterarContato()

    while True:
      os.system(limpar)
      sub = int(input("1 - Alterar Nome\n2 - Alterar Contato\n--> "))
      if sub == 1:
        novoNome = input("Qual o novo nome do cliente?\n")
        self.contatos[novoNome] = self.contatos[nome]
        self.contatos.pop(nome)
        break
      if sub == 2:
        novoTelefone = int(input("Qual o novo número do cliente?\n--> "))
        self.contatos[nome] = novoTelefone
        break

  def deletarContato(self):
    print(f"{'DELETAR CONTANTO':{'-'}^20}\n")

    nome = input("Qual nome do contato que você deseja deletar?\n--> ")
    self.contatos.pop(nome)

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
    print(f"{'MENU':{'-'}^20}")
    print(f"1 - Cadastrar um cliente")
    print(f"2 - Pesquisar um cliente")
    print(f"3 - Listar clientes")
    print(f"4 - Alterar um cliente")
    print(f"5 - Deletar um cliente")
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