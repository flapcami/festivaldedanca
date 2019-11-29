import os
from peewee import *
db = SqliteDatabase ("FestivalDeDanca.db")

class BaseModel(Model):
    class Meta:
        database = db

class Categoria(BaseModel):
    nome = CharField()
    variacao_idade = CharField()

    def __str__(self):
        return(self.nome + '\n' + 'Variação da idade: ' + self.variacao_idade + '\n')

class Estilo(BaseModel):
    nome = CharField()
    pais_de_origem = CharField()

    def __str__(self):
        return(self.nome + '\n' + 'Pais de origem: ' + self.pais_de_origem + '\n')


class Local(BaseModel):
    nome = CharField()
    endereco = CharField()
    palco = CharField()
    estilo = ForeignKeyField(Estilo)

    def __str__(self):
        return('Local: ' + self.nome + '\n' + 'Endereço: ' + self.endereco + '\n' + 'Palco: ' + self.palco + '\n' + 'Estilo: ' + str(self.estilo)+ '\n' )


class Cadeira(BaseModel):
    numero = CharField()
    fileira = CharField()


    def __str__(self):
        return('\n' + "Numero da cadeira: " + self.numero + '\n' + 'Numero da fileira: ' + self.fileira+ '\n')
        
class Bailarino(BaseModel):
    nome = CharField()
    data_nascimento = CharField()
    cadeira = ForeignKeyField(Cadeira)

    def __str__(self):
        return('\n' + 'Nome: ' + self.nome + '\n' + "Data de nascimento: "  + self.data_nascimento + '\n' + 'Cadeira: ' + str(self.cadeira)  + '\n')

class Coreografo(BaseModel): 
    nome = CharField()
    data_nascimento = CharField()
    cadeira = ForeignKeyField(Cadeira)

    def __str__(self):
        return('\n' + 'Nome: ' +  self.nome  + '\n' + 'data_nascimento: ' + self.data_nascimento  + '\n' + "Cadeira: " + str(self.cadeira)  + '\n')


class Grupo(BaseModel):
    nome = CharField()
    coreografo = ForeignKeyField(Coreografo)
    estilo = ForeignKeyField(Estilo)
    categoria = ForeignKeyField(Categoria)

    def __str__(self):
        return('\n' + 'Nome: ' +  self.nome  + '\n' + 'Coreografo: ' + str(self.coreografo)   + '\n' + 'Estilo: ' + str(self.estilo)  + '\n' + 'Categoria: ' + str(self.categoria)  + '\n')

class BailarinoDoGrupo(BaseModel):
    bailarino = ForeignKeyField(Bailarino)
    grupo = ForeignKeyField(Grupo)

    def __str__(self):
        return('Bailarino: ' + str(self.bailarino)  + '\n' + 'Grupo: ' + str(self.grupo)  + '\n')

class Coreografia(BaseModel):
    nome = CharField()
    duracao = CharField()
    grupo = ForeignKeyField(Grupo)

    def __str__(self):
        return('Nome: ' + self.nome + '\n' + 'Duracao: ' + self.duracao  + '\n' + 'Grupo: ' + str(self.grupo) + '\n' )


class Jurado(BaseModel):
    nome = CharField()
    data_nascimento = CharField()
    estilo = ForeignKeyField(Estilo)

    def __str__(self):
        return('Nome: ' + self.nome + '\n' + 'Data de nascimento: ' + self.data_nascimento + '\n' + 'Estilo: ' + str(self.estilo) + '\n')






if __name__ == "__main__":
    if os.path.exists("CampeonatoFutebol.db"):
        os.remove("CampeonatoFutebol.db")

    db.connect()
    db.create_tables([Categoria, Estilo, Local, Cadeira, Bailarino, Coreografo, Grupo, BailarinoDoGrupo, Coreografia, Jurado])



    senior = Categoria.create(nome = 'Senior', variacao_idade = '16-18 anos')
    hiphop = Estilo.create(nome = 'HipHop', pais_de_origem = 'Estados Unidos')
    teatro_positivo = Local.create(nome = 'Teatro Positivo', endereco = 'Curitiba', palco = 'palco 1', estilo = hiphop)
    a11 = Cadeira.create(numero = '11', fileira = 'a')
    a12 = Cadeira.create(numero = '12', fileira = 'a')
    camila = Bailarino.create(nome = 'Camila Dalcanale', data_nascimento = '21/11/2001', cadeira = a11)
    dedeia = Coreografo.create(nome = 'Andreia Mendes', data_nascimento = "15/10/1975", cadeira = a12)
    amfamily = Grupo.create(nome = 'Grupo de Dança Andreia Mendes', coreografo = dedeia, estilo = hiphop, categoria = senior)
    bailarina_camila = BailarinoDoGrupo(bailarino = camila, grupo = amfamily)
    namata = Coreografia.create(nome = 'Na Mata', duracao = '10 minuros', grupo = amfamily)
    jocardoso = Jurado.create(nome = 'Jonatas Cardoso', data_nascimento = '05/12/77', estilo = hiphop)


print(bailarina_camila)


