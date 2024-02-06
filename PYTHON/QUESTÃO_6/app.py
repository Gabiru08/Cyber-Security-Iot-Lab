from datetime import datetime

class Pessoa:
    def __init__(self,nome,idade,altura):
        self.nome=nome
        self.idade=idade
        self.altura=altura


    def get_nome(self):
        return self.nome
    
    def set_nome(self,novo_nome):
        self.nome=novo_nome

    def get_idade(self):
        return self.idade
    
    def set_idade(self,nova_idade):
        self.idade=nova_idade
        
    def get_altura(self):
        return self.altura
    
    def set_altura(self,nova_altura):
        self.altura=nova_altura

    def calcular_ano_nascimento(self):
        from datetime import date
        ano_atual = date.today().year
        return ano_atual - self.idade
    


class PessoacomDoc(Pessoa):
   def __init__(self,nome,idade,altura,rg,cpf):
      super().__init__(nome,idade,altura)
      self.rg = rg
      self.cpf = cpf

   def getrg(self):
        return self.rg
   
   def setrg(self,rg):
        self.rg=rg

   def getcpf(self):
        return self.cpf
   
   def setcpf(self,cpf):
        self.cpf=cpf


pessoa1 = PessoacomDoc("Evandro", 30, 1.75, "123456", "789012345")


print("Nome:", pessoa1.get_nome())
print("Idade:", pessoa1.get_idade())
print("Altura:", pessoa1.get_altura())
print("RG:", pessoa1.getrg())
print("CPF:", pessoa1.getcpf())
print("Ano de Nascimento:", pessoa1.calcular_ano_nascimento())
