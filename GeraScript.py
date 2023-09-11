import mysql.connector
import mysql.connector.cursor
from Tabelas import Tabelas


class MySQLManagement:

    def __init__(self):
        self.__conn: mysql.connector = None
        self.__cursor: mysql.connector.cursor = None

    def __connect_server(self, host, user, password) -> None:
        self.__conn = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password)

    def __connect_DB(self, host, user, password, bd) -> None:
        self.__conn = mysql.connector.connect(host=host,
                                              database=bd,
                                              user=user,
                                              password=password)

    def __get_cursor(self) -> mysql.connector.cursor:
        cursor = self.__cursor = self.__conn.cursor()
        return cursor

    def __close_conn(self) -> None:
        conn = self.__conn
        cursor = self.__cursor

        if conn.is_connected():
            if cursor is not None:
                cursor.close()
            conn.close()

    def __commit(self) -> None:
        self.__conn.commit()

    def cria_database(self, host, user, password, database):
        self.__connect_server(host, user, password)

        cur = self.__get_cursor()

        cur.execute(f'CREATE DATABASE IF NOT EXISTS {database}')

        self.__commit()

        self.__close_conn()

    def cria_tabelas(self, host, user, password, database, scripts):
        self.__connect_DB(host, user, password, database)

        cur = self.__get_cursor()

        for script in scripts:

            cur.execute(script)
            self.__commit()

        self.__close_conn()


class Script:
    def __init__(self, tabelas: Tabelas):
        self.__tabelas = tabelas
        self.__script = ''
        self.__scripts = []
        self.__db = MySQLManagement()
        self.__ip = None
        self.__user = None
        self.__pwd = None
        self.__nome = None

    def geraScript(self):
        for tabela in self.__tabelas.getTabelas():
            self.__script += f'CREATE TABLE IF NOT EXISTS {tabela.getNomeTabela()}(\n'
            for coluna in self.__tabelas.getTabela(nometabela=tabela.getNomeTabela()):
                if not coluna.getNulo():
                    nulo = 'NOT NULL'
                else:
                    nulo = ''
                if coluna.getAutoIncrement():
                    increment = 'AUTO_INCREMENT'
                else:
                    increment = ''
                if coluna.getTipoDado().upper() == 'VARCHAR' or coluna.getTipoDado().upper() == 'CHAR':
                    self.__script += f'\t{coluna.getNomeColuna()} {coluna.getTipoDado().upper()}({coluna.getTamanho()}) {nulo} {increment},\n'
                else:
                    self.__script += f'\t{coluna.getNomeColuna()} {coluna.getTipoDado().upper()} {nulo} {increment},\n'

            self.__script += f'\n\tPRIMARY KEY('
            for pk in tabela.getPK():
                self.__script += f'{pk},'
            self.__script = f'{self.__script[0:len(self.__script) - 1]})\n);\n\n'
            self.__scripts.append(self.__script)
            self.__script = ''


        for tabela in self.__tabelas.getTabelas():
            if tabela.getFK():
                for fk in tabela.getFK():
                    for coluna in tabela.getTabela():
                        if coluna.getNomeColuna() == fk:
                            self.__script += f'ALTER TABLE {tabela.getNomeTabela()}\n\tADD FOREIGN KEY(' \
                                             f'{coluna.getNomeColuna()}) REFERENCES {coluna.getReferences()}(' \
                                             f'{coluna.getNomeColuna()});\n\n'
            self.__scripts.append(self.__script)
            self.__script = ''

    def getScript(self):
        return self.__scripts

    def criadb(self, ip, user, password, nome):
        self.__ip = ip
        self.__user = user
        self.__pwd = password
        self.__nome = nome
        self.__db.cria_database(host=self.__ip, user=self.__user, password=self.__pwd, database=self.__nome)

    def criatabelas(self):
        self.__db.cria_tabelas(host=self.__ip, user=self.__user, password=self.__pwd, database=self.__nome,
                               scripts=self.__scripts)