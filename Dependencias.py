from Tabelas import Tabelas

class Dependencias:
    def __init__(self, tabela: Tabelas):
        self.__dependencias = []
        self.__tabelas = tabela

    def criaDependencia(self, esquerda: [], direita: []):
        dependencia = Dependencia(esquerda=esquerda, direita=direita)
        self.__dependencias.append(dependencia)

    def excluiDependencia(self, posicao: int):
        self.__dependencias.pop(posicao)

    def getQttEsq(self, determinante: str):
        qtt = []
        for dependencia in self.__dependencias:
            if dependencia.getEsquerda() == determinante:
                qtt.append(dependencia.getQtdEsquerda())
        return qtt

    def getQttDir(self, determinante: str):
        qtt = []
        for dependencia in self.__dependencias:
            if dependencia.getEsquerda() == determinante:
                qtt.append(dependencia.getQtdDireita())
        return qtt

    def verificaDependentes(self, dependente: str):
        possui = []
        for dependencia in self.__dependencias:
            for dep in dependencia.getDireita():
                if dep == dependente:
                    possui.append(dependencia.getEsquerda())
        return possui

    def getDependencias(self):
        return self.__dependencias

    def setDireita(self, esquerda: str, novaDireita: []):
        for dependencia in self.__dependencias:
            if dependencia.getEsquerda() == esquerda:
                dependencia.setDireita(novaDireita=novaDireita)

    def getDireita(self, esquerda: str):
        for dependencia in self.__dependencias:
            if dependencia.getEsquerda() == esquerda:
                return dependencia.getDireita()

    def getPrimDep(self):
        for dependencia in self.__dependencias:
            return dependencia

    def Normalizar(self):
        for col in self.__tabelas.getNomeColunas(nomeTabela=self.__tabelas.getNomeTabelas()[0]):
            possui = self.verificaDependentes(dependente=col)
            if len(possui) > 1:
                qtd = []
                qtdoriginal = []
                for det in possui:
                    qtd.append(self.getQttEsq(determinante=det))
                    qtdoriginal.append(self.getQttEsq(determinante=det))
                qtd.sort(reverse=True)
                for i in range(0, len(qtd) - 1):
                    if qtd[i] > qtd[i + 1]:
                        for j in range(0, len(qtdoriginal)):
                            if qtdoriginal[j] == qtd[i]:
                                depende = self.getDireita(esquerda=possui[j])
                                novaDir = []
                                for atributo in depende:
                                    if atributo != col:
                                        novaDir.append(atributo)
                                self.setDireita(esquerda=possui[j], novaDireita=novaDir)
        for col in self.__tabelas.getNomeColunas(nomeTabela=self.__tabelas.getNomeTabelas()[0]):
            possui = self.verificaDependentes(dependente=col)
            if len(possui) > 1:
                qtd = []
                qtdoriginal = []
                for det in possui:
                    qtd.append(self.getQttDir(determinante=det))
                    qtdoriginal.append(self.getQttDir(determinante=det))
                qtd.sort(reverse=True)
                for i in range(0, len(qtd) - 1):
                    if qtd[i] > qtd[i + 1]:
                        for j in range(0, len(qtdoriginal)):
                            if qtdoriginal[j] == qtd[i]:
                                depende = self.getDireita(esquerda=possui[j])
                                novaDir = []
                                for atributo in depende:
                                    if atributo != col:
                                        novaDir.append(atributo)
                                self.setDireita(esquerda=possui[j], novaDireita=novaDir)

    def criaTabelas(self, repete_esq, tamanho_esq, tamanho_dir, posicao_esq):

        j = 0
        primaryKeys = []
        posicaoPK = []
        for j in range(len(repete_esq)):
            if len(repete_esq[j]) <= 1:
                primaryKeys.append(repete_esq[j][0])
                posicaoPK.append(posicao_esq[j][0])
            else:
                k = 1
                pos_esq = None
                copiatamanho_esq = []
                for at in tamanho_esq[j]:
                    copiatamanho_esq.append(at)
                copiatamanho_esq.sort()
                if copiatamanho_esq[0] == copiatamanho_esq[1]:
                    for k in range(len(repete_esq[j])):
                        menor_esq = tamanho_esq[j][0]
                        pos_esq = 0
                        if tamanho_esq[j][k] < menor_esq:
                            menor_esq = tamanho_esq[j][k]
                            pos_esq = k
                        elif tamanho_esq[j][k] == menor_esq:
                            if tamanho_dir[j][k] < tamanho_dir[j][pos_esq]:
                                primaryKeys.append(repete_esq[j][k])
                                posicaoPK.append(posicao_esq[j][k])
                            elif tamanho_dir[j][pos_esq] < tamanho_dir[j][k]:
                                primaryKeys.append(repete_esq[j][pos_esq])
                                posicaoPK.append(repete_esq[j][pos_esq])
                            else:
                                primaryKeys.append(repete_esq[j][pos_esq])
                                posicaoPK.append(repete_esq[j][pos_esq])
                else:
                    for k in range(len(repete_esq[j])):
                        menor_esq = tamanho_esq[j][0]
                        pos_esq = 0
                        if tamanho_esq[j][k] < menor_esq:
                            menor_esq = tamanho_esq[j][k]
                            pos_esq = k

                    primaryKeys.append(repete_esq[j][pos_esq])
                    posicaoPK.append(posicao_esq[j][pos_esq])

        if len(self.__tabelas.getNomeTabelas()) > 1:
            for tabela in self.__tabelas.getTabelas():
                if not tabela == self.__tabelas.getTabelas()[0]:
                    for coluna in tabela.getTabela():
                        if coluna.getForeignKey():
                            k = 0
                            for pk in primaryKeys:
                                if pk == coluna.getNomeColuna():
                                    coluna.setReferences(novoReferences=f'Tabela{k + 1}')
                                k += 1
        i = 1
        j = 0
        for dependencia in self.__dependencias:
            self.__tabelas.criaTabela(nomeTabela=f'Tabela{i}')
            for atributo in dependencia.getEsquerda():
                primaryKey = False
                foreignKey = False
                references = ''
                k = 0
                for pk in primaryKeys:
                    if (pk == atributo) and (posicaoPK[k] == j):
                        primaryKey = True
                    elif pk == atributo and not (posicaoPK[k] == j):
                        primaryKey = True
                        foreignKey = True
                        references = f'Tabela{k + 1}'
                    k += 1
                coluna = self.__tabelas.getColuna(nomecoluna=atributo)
                self.__tabelas.adicionaColuna(nomeTabela=f'Tabela{i}', nomeColuna=coluna.getNomeColuna(),
                                              tipoDado=coluna.getTipoDado(), tamanho=coluna.getTamanho(),
                                              nulo=coluna.getNulo(), composto=coluna.getComposto(),
                                              autoIncrement=coluna.getAutoIncrement(), primaryKey=primaryKey,
                                              foreignKey=foreignKey, references=references, multiValor=False)
            for atributo in dependencia.getDireita():
                foreignKey = False
                references = ''
                k = 0
                for pk in primaryKeys:
                    if pk == atributo and not (posicaoPK[k] == j):
                        foreignKey = True
                        references = f'Tabela{k + 1}'
                    k += 1
                coluna = self.__tabelas.getColuna(nomecoluna=atributo)
                self.__tabelas.adicionaColuna(nomeTabela=f'Tabela{i}', nomeColuna=coluna.getNomeColuna(),
                                              tipoDado=coluna.getTipoDado(), tamanho=coluna.getTamanho(),
                                              nulo=coluna.getNulo(), composto=coluna.getComposto(),
                                              autoIncrement=coluna.getAutoIncrement(), primaryKey=False,
                                              foreignKey=foreignKey, references=references, multiValor=False)
            j += 1
            i += 1
        self.__tabelas.excluiTabela(nometabela=self.__tabelas.getNomeTabelas()[0])

    def checkRepete(self):
        repete_esq = []
        tamanho_esq = []
        tamanho_dir = []
        posicao_esq = []
        for coluna in self.__tabelas.getNomeColunas(nomeTabela=self.__tabelas.getNomeTabelas()[0]):
            i = 0
            atributos = []
            posicoes = []
            tamanhos = []
            for dependencia in self.__dependencias:
                for atributo in dependencia.getEsquerda():
                    if atributo == coluna:
                        atributos.append(atributo)
                        posicoes.append(i)
                        tamanhos.append(len(dependencia.getEsquerda()))

                i += 1

            if atributos:
                repete_esq.append(atributos)
                tamanho_esq.append(tamanhos)
                posicao_esq.append(posicoes)

            atributos = []
            posicoes = []
            tamanhos = []
            i = 0

            for dependencia in self.__dependencias:

                for atributo in dependencia.getDireita():
                    if atributo == coluna:
                        tamanhos.append(len(dependencia.getDireita()))

                i += 1

            if atributos:
                tamanho_dir.append(tamanhos)
            tamanhos = []
        self.criaTabelas(repete_esq, tamanho_esq, tamanho_dir, posicao_esq)

    def getTabela(self):
        return self.__tabelas


class Dependencia:
    def __init__(self, esquerda: [], direita: []):
        self.__esquerda = esquerda
        self.__direita = direita
        self.__qtddireita = len(direita)
        self.__qtdesquerda = len(esquerda)
        self.__dependencia = {'esquerda': self.__esquerda, 'direita': self.__direita}

    def getEsquerda(self):
        return self.__esquerda

    def getDireita(self):
        return self.__direita

    def setEsquerda(self, novaEsquerda: []):
        self.__esquerda = novaEsquerda

    def setDireita(self, novaDireita: []):
        self.__direita = novaDireita

    def getDependencia(self):
        return self.__dependencia

    def getQtdEsquerda(self):
        return self.__qtdesquerda

    def getQtdDireita(self):
        return self.__qtddireita