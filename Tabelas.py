class Tabelas:

    def __init__(self):

        self.__tabelas = []

    def criaTabela(self, nomeTabela: str):

        novaTabela = Tabela(nomeTabela=nomeTabela)

        self.__tabelas.append(novaTabela)

    def adicionaColuna(self, nomeTabela: str, nomeColuna: str, tipoDado: str, tamanho: int, nulo: bool, autoIncrement: bool,
                       primaryKey: bool, foreignKey: bool, references: str, composto: bool, multiValor: bool):
        for tabela in self.__tabelas:
            if tabela.getNomeTabela() == nomeTabela:
                tabela.criaColuna(nomeColuna=nomeColuna, tipoDado=tipoDado, tamanho=tamanho, nulo=nulo,
                                  autoIncrement=autoIncrement, primaryKey=primaryKey, foreignKey=foreignKey,
                                  references=references, composto=composto, multiValor=multiValor)

    def editaColuna(self,nometabela: str, nomecoluna: str, opcao: str, novaConfiguracao):
        for tabela in self.__tabelas:
            if tabela.getNomeTabela() == nometabela:
                tabela.editaColuna(nomecoluna=nomecoluna, opcao=opcao, novaConfiguracao=novaConfiguracao)

    def excluiColuna(self,nometabela: str, nomecoluna: str):
        for tabela in self.__tabelas:
            if tabela.getNomeTabela() == nometabela:
                tabela.excluiColuna(nomeColuna=nomecoluna)

    def excluiTabela(self, nometabela: str):
        i = 0
        for tabela in self.__tabelas:
            if tabela.getNomeTabela() == nometabela:
                self.__tabelas.pop(i)
            else:
                i += 1

    def getTabela(self, nometabela:str):
        for tabela in self.__tabelas:
            if tabela.getNomeTabela() == nometabela:
                return tabela.getTabela()

    def getNomeTabelas(self):
        nomes = []
        for tabela in self.__tabelas:
            nomes.append(tabela.getNomeTabela())
        return nomes

    def getPK(self, nomeTabela: str):
        for tabela in self.__tabelas:
            if tabela.getNomeTabela() == nomeTabela:
                return tabela.getPK()

    def getFK(self, nomeTabela: str):
        for tabela in self.__tabelas:
            if tabela.getNomeTabela() == nomeTabela:
                return tabela.getFK()

    def getCompostos(self):
        for tabela in self.__tabelas:
            return tabela.getComposto()

    def getMultiValor(self):
        for tabela in self.__tabelas:
            return tabela.getMultiValor()

    def getNomeColunas(self, nomeTabela: str):
        for tabela in self.__tabelas:
            if tabela.getNomeTabela() == nomeTabela:
                return tabela.getNomeColunas()

    def getColuna(self, nomecoluna: str):
        for tabela in self.__tabelas:
            return tabela.getColuna(nomecoluna=nomecoluna)

    def setNomeTabela(self, nometabela: str, novonometabela: str):
        for tabela in self.__tabelas:
            if tabela.getNomeTabela() == nometabela:
                tabela.setNomeTabela(nometabela=novonometabela)

    def getTabelas(self):
        return self.__tabelas


class Tabela:
    def __init__(self, nomeTabela: str):
        self.__colunas = Colunas()
        self.__nomeTabela = nomeTabela
        self.__tabela = {'nomeTabela': self.__nomeTabela, 'colunas': self.__colunas.getColunas()}

    def criaColuna(self, nomeColuna: str, tipoDado: str, tamanho: int, nulo: bool, autoIncrement: bool,
                   primaryKey: bool, foreignKey: bool, references: str, composto: bool, multiValor: bool):

        self.__colunas.adicionaColuna(nomeColuna=nomeColuna, tipoDado=tipoDado, tamanho=tamanho, nulo=nulo,
                                      autoIncrement=autoIncrement, primaryKey=primaryKey, foreignKey=foreignKey,
                                      references=references, composto=composto, multiValor=multiValor)

    def editaColuna(self, nomecoluna: str, opcao: str, novaConfiguracao):
        self.__colunas.editaColuna(nomecoluna=nomecoluna, opcao=opcao, novaConfiguracao=novaConfiguracao)

    def excluiColuna(self, nomeColuna: str):
        self.__colunas.excluiColuna(nomecoluna=nomeColuna)

    def getTabela(self):
        return self.__tabela['colunas']

    def getNomeTabela(self):
        return self.__tabela['nomeTabela']

    def setNomeTabela(self, nometabela: str):
        self.__nomeTabela = nometabela
        self.__tabela['nomeTabela'] = nometabela

    def getComposto(self):
        return self.__colunas.getCompostos()

    def getPK(self):
        return self.__colunas.getPK()

    def getFK(self):
        return self.__colunas.getFK()

    def getMultiValor(self):
        return self.__colunas.getMultiValor()

    def getNomeColunas(self):
        return self.__colunas.getNomeColunas()

    def getColuna(self, nomecoluna: str):
        return self.__colunas.getColuna(nomecoluna=nomecoluna)

class Colunas:
    def __init__(self):
        self.__colunas = []

    def adicionaColuna(self, nomeColuna: str, tipoDado: str, tamanho: int, nulo: bool, autoIncrement: bool,
                       primaryKey: bool, foreignKey: bool, references: str, composto: bool, multiValor: bool):

        coluna = Coluna(nomeColuna=nomeColuna, tipoDado=tipoDado, tamanho=tamanho, nulo=nulo,
                        autoIncrement=autoIncrement, primaryKey=primaryKey, foreignKey=foreignKey,
                        references=references, composto=composto, multiValor=multiValor)

        self.__colunas.append(coluna)

    def editaColuna(self, nomecoluna: str, opcao: str, novaConfiguracao):
        for coluna in self.__colunas:
            if coluna.getNomeColuna() == nomecoluna:
                if opcao == 'nomeColuna':
                    coluna.setNomeColuna(novaConfiguracao)
                elif opcao == 'tipoDado':
                    coluna.setTipoDado(novaConfiguracao)
                elif opcao == 'tamanho':
                    coluna.setTamano(novaConfiguracao)
                elif opcao == 'nulo':
                    coluna.setNulo(novaConfiguracao)
                elif opcao == 'autoIncrement':
                    coluna.setAutoIncrement(novaConfiguracao)
                elif opcao == 'primarKey':
                    coluna.setPrimaryKey(novaConfiguracao)
                elif opcao == 'foreignKey':
                    coluna.setForeignKey(novaConfiguracao)
                elif opcao == 'references':
                    coluna.setReferences(novaConfiguracao)

    def excluiColuna(self, nomecoluna: str):
        i = 0
        for coluna in self.__colunas:
            if not (coluna.getNomeColuna() == nomecoluna):
                i += 1
            else:
                self.__colunas.pop(i)

    def getColunas(self):
        return self.__colunas

    def getNomeColunas(self):
        nomeColunas = []
        for coluna in self.__colunas:
            nomeColunas.append(coluna.getNomeColuna())
        return nomeColunas

    def getCompostos(self):
        compostos = []
        for coluna in self.__colunas:
            if coluna.getComposto():
                compostos.append(coluna.getNomeColuna())
        return compostos

    def getPK(self):
        pk = []
        for coluna in self.__colunas:
            if coluna.getPrimaryKey():
                pk.append(coluna.getNomeColuna())
        return pk

    def getFK(self):
        fk = []
        for coluna in self.__colunas:
            if coluna.getForeignKey():
                fk.append(coluna.getNomeColuna())
        return fk

    def getMultiValor(self):
        multivalores = []
        for coluna in self.__colunas:
            if coluna.getMultiValor():
                multivalores.append(coluna.getNomeColuna())
        return multivalores

    def getColuna(self, nomecoluna: str):
        for coluna in self.__colunas:
            if coluna.getNomeColuna() == nomecoluna:
                return coluna


class Coluna:
    def __init__(self, nomeColuna: str, tipoDado: str, tamanho: int, nulo: bool, autoIncrement: bool,
                       primaryKey: bool, foreignKey: bool, references: str, composto: bool, multiValor: bool):
        self.__nomeColuna = nomeColuna
        self.__tipoDado = tipoDado
        self.__tamanho = tamanho
        self.__nulo = nulo
        self.__autoIncrement = autoIncrement
        self.__primaryKey = primaryKey
        self.__foreignKey = foreignKey
        self.__references = references
        self.__composto = composto
        self.__multiValor = multiValor

        self.__coluna = {'nomeColuna': self.__nomeColuna, 'tipoDado': self.__tipoDado, 'tamanho': self.__tamanho,
                         'nulo': self.__nulo, 'autoIncrement': self.__autoIncrement, 'primaryKey': self.__primaryKey,
                         'foreignKey': self.__foreignKey, 'references': self.__references, 'composto': self.__composto,
                         'multiValorado': self.__multiValor}

    def getNomeColuna(self):
        return self.__nomeColuna

    def setNomeColuna(self, novoNome: str):
        self.__nomeColuna = novoNome

    def getTipoDado(self):
        return self.__tipoDado

    def setTipoDado(self, novoTipo: str):
        self.__tipoDado = novoTipo

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, novoTamanho: int):
        self.__tamanho = novoTamanho

    def getNulo(self):
        return self.__nulo

    def setNulo(self, novoNulo: bool):
        self.__nulo = novoNulo

    def getAutoIncrement(self):
        return self.__autoIncrement

    def setAutoIncrement(self, novoAutoIncrement: bool):
        self.__autoIncrement = novoAutoIncrement

    def getPrimaryKey(self):
        return self.__primaryKey

    def setPrimaryKey(self, novoPrimaryKey: bool):
        self.__primaryKey = novoPrimaryKey

    def getForeignKey(self):
        return self.__foreignKey

    def setForeignKey(self, novoForeignKey: bool):
        self.__foreignKey = novoForeignKey

    def getReferences(self):
        return self.__references

    def setReferences(self, novoReferences: str):
        self.__references = novoReferences

    def getColunas(self):
        return self.__coluna

    def getComposto(self):
        return self.__composto

    def setComposto(self, novoComposto: str):
        self.__composto = novoComposto

    def getMultiValor(self):
        return self.__multiValor

    def setMultiValor(self, novoMultiValor: str):
        self.__multiValor = novoMultiValor