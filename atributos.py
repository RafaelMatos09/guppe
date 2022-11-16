"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos nós conseguimos
representar computacionalmente os estados de um objeto.


Em Python, dividimos os atributo em 3  grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos Dinámicos;

# Atributos de instância: São atributos declarados dentro do método construtor.

# OBS: Método construtor: Ê um método especial utilizadopara a construção do objeto.

# Em Java, uma classe lâmpda, incluido seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }

}

Em Python, por convenção, ficou estabelecido que, todo  atríbuto de uma classe é público
Ou seja, pode ser acesso em todo o projeto.
Caso queíramos demostrar que determinado atríbuto deve ser tratado como privado, ou seja
que deve ser acessado/utilizado somente dentro da propria classe onde está declarado,
utiliza-se __ duplo underscore no inicio de seu nome.

Isso é conhecido também como Name Mangling.
"""


# Classes com Atributo de instância Público
class Lampada:

    def __init__(self, voltagem, cor):  # metodo __init__ construtor , nele fazemos a declaração dos atributos
        self.voltagem = voltagem  # private -> __
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Públicos e Atributos Privados


class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo


user = Acesso('user@gmail.com', '123456')

print(user.email)
#print(user.__senha)  # AtributeError

print(dir(user))
print(user._Acesso__senha)  # Temos acesso. Mas não deveriamos fazer este acesso. (Name Mangling)
user.mostra_senha()
user.mostra_email()

# O que significa atributos de instância?

# Significa, que ao criarmos instâncias/objetos de uma classe, todas as instâncias
# terão estes atributos

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '123456')

user1.mostra_email()
user2.mostra_email()

# Atributos de Classe

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox 5', 'Video Game', 4500)

# Atributos de classe, são atributos, claro, que são declarados diretamente na classe,
# ou seja fora doconstrutor. Geralmente já inicializamos um valor, e este valor é compartilhado entre
# todas as instâncias da classe, Ou seja, ao invés de cada instância da classe ter seus próprios
# valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias
# terão o mesmo valor para este atributo.

# Refatorar a classe Produto


class Produto:
    # Atributo de classe
    imposto = 1.05  # 0.05 de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)

# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será execlusivo da instância que o criou

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg'    # Note que na classe Produto não existe o atributo peso

print(f'Produto {p2.nome}, Decrição: {p2.descricao}, valor: {p2.valor}, Peso: {p2.peso}')
#print(f'Produto {p1.nome}, Decrição: {p1.descricao}, valor: {p1.valor}, Peso: {p1.peso}')

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

# print(Produto.__dict__)

del p2.peso

print(p1.__dict__)
print(p2.__dict__)