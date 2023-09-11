import PySimpleGUI as sg
from Tabelas import Tabelas
from Dependencias import Dependencias
from collections import OrderedDict
from GeraScript import Script


class Telas:

    def __init__(self):
        sg.theme('DarkTeal10')
        self.__fonte = ("Courier", 11)
        self.__tamanho = (15, 1)
        self.__dist = (5, 5)
        self.__tabela = Tabelas()
        self.__dependencias = Dependencias(tabela=self.__tabela)
        self.__tabelaInicial = None
        self.__script = None

    def arrumaTamanho(self, text: str, tamanho: int):
        try:
            if len(text) == tamanho:
                return text
            elif len(text) < tamanho:
                diferenca = tamanho - len(text) - 1
                for _ in range(diferenca):
                    text = text + " "
                return text + " "
            else:
                return text[0:tamanho]
        except TypeError:
            for _ in range(tamanho):
                text = text + " "
            return text

    def janelaCriaColuna(self):

        frame_cabecalho = [
            [
                sg.B(key='Novo', tooltip='Novo Formulário', size=(10, 2), pad=(5, 5),
                     image_data='iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAACc1BMVEUAAAAAAQEAAAACAQATDgAAAAAAAAAAAAAgGAEODAIAAAAAAAAuJAEGBQEAAAAuIwEBAQAAAAAAAAA8MwwAAAAAAAAUEQQAAAAAAAAAAAAAAABSPwIAAAAAAADBkgQABAYADxYUHRYAAAAAJTUALkIALUIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL0QAAAAAAACUbwHBkgYtFgAAAAAoGwA2KQEAAAAAAAAAAAAEEiIAAAACDhgAAAAAAAAAAAAAAAACCxYAAAAAAAACCRIABAYAAQIZEwAZEAAOBwC6jQXVogbUoQbUogbUiAN4PAATEQTqswf/wwj/wgj/xAj/pQSQRgBRRRB8ahnpsQf/wQj+wQj+wgj+owSPRgBVSRHwzjFlVhT+pASRRwBTRxH81zPpxzBOQxCSSAD/3DXdvS3+pgSYSwBCOA3PsSrTtCvWtiygiSH/uQfSjARDMwMyKAU0KgU1JgUVDAH9wAfstAfdqAbeqQbciANqNQD+nQN6PQD8nAN5PADxuAf9wAjgqgb0ugcgHw9nTwTzuQcBiMUDg8YKS40dHRHbpgUBpu8FoO8PXasbHhXZpAUBpO0Fnu0PXKobHRUFnuwPW6nYowX8wAcBpe0EoO4NaLMKFBdNOQBbRAFaQwFZQwF8XgPqsgd6PAAAM0kBY48BYYwBfbUBqPMCqPQCoOkBb6IAX44AYI8AXo4FQncFEyOnfgP/xQh4OwABXYYCrvwCq/gCq/YCqfQBqfQCq/cCqvcPedAGIUB1WQNyRQEHIUABb6EBYIwIRHUQXKgQXKkQXaoEhMUNTIsADxYADxcBCBD///+y4TtoAAAASHRSTlMAAAyj/e9SMe3XNDjzxiPzsRaZ+4EG9FuQkSjeECGtuuLzT/v8/AECUyuVpqWjwv6OnOzw/Gl1SIhkD/xX9rKkghTmJiXk06yD7oweAAAAAWJLR0TQDtbPnAAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+YLBg84Hri++lcAAAFzSURBVDjLY2CAASZmFg8Y8PRiZWNAB+wc3j6+EODnHxDIyYWugJsnKDgEAkLDwiMiefnQFfBHRcdAQGxcfEJikoAgbgXJKalp6RlCTLgVZKamZWULi4jiUpCTm5dfUFgkJo5DQUxxSWlZeXlFpQQOBVUxsdU1NbV19ZK4TACCkJDghkZ8CoCgqZneCqSkW0Ja8SiQkZVra49pxalAVl5BsaOzC7cJSsrdPb19/SE4FbCpTJg4afIUPApUp06bPgOHAjV1dQYN1akzZ82YHT1nTizcpTAFmlraOrp6+nPnzV+wcNHiJUuXwYKjaTlEgcGKlatWrVq9Zu269Rs2btq8Zeu2YAho2A6ObkbDHTt37dq1e8/evft27dp/4KCR8SEIOGxiik3BETNzCyiwtEKz4uiqVceOW9ugZwiEI23t7HW0HRwx8hTMmyecnBnU1dUYsAJQQJ10cmHACUBBfQqfAmBknT7jyodbgYvb2XPn3ZkwJQDVIushbKsntwAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAyMi0xMS0wNlQxNTo1NjozMCswMDowMLE+9AsAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMjItMTEtMDZUMTU6NTY6MzArMDA6MDDAY0y3AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAABJRU5ErkJggg=='),
                sg.B(key='Normalizacao', tooltip='Normalizar Formulário', size=(10, 2), pad=(5, 5), enable_events=True,
                     image_data='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'),
                sg.B(key='Fechar', tooltip='Fechar Formulário', size=(9, 2), pad=(5, 5),
                     image_data='iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABoVBMVEUAAADiTEv/f37LOzrnT07QPz7RQD/TQUDSQD/bR0bWQ0LLPDvkTEvNPTzVQkHkTUzMPDvVQ0LPPj3YREPSQUDiTEviTEviTEviTEviTEviTEviTEviTEviTEviTEviTEviTEviTEviTEviTEviTEvhS0rcSEfiTEviTEveSUjUQkHYRUTQPz7iTEvSQUDQPz7iTEviTEvQPz7RQD/iTEviTEvRQD/RPz7QPz7iTEvQPz7RQD/QPz7RQD/RQD/RQD/iTEvRQD/RQD/RQD/RQD/RQD/RQD/RQD/SQD/RQD/WQ0LRQD/SQD/RQD/hS0rRQD/SQUDdSEfRQD/SQD/YRUTRQD/SQD/QPz7SQUDRQD/SQD/QPz7QPz7RQD/RQD/RQD/QPz7QPz7QPz7RQD/SQD/UQkHRQD/RQD/TQUDiTEvhS0riS0reSUjhSkniTUzXREPocXD0v7/xqKjkWFjcR0b0v77////+/f30vb3kWFffSknTQUD+/v7VQ0L0vbzjV1bYRUTQPz70wMDZRUTSQUDRQD/WREPSQD/iSknUQkHhTEt6vSJhAAAAaXRSTlMAAAAAAAAAAAAAAAAAAAAAAAAAAAAEKmyt2vP9N5fg/BqK6jbDwzhC2dxH3TzCyB8DiZEEOOntPZ3f4i78cbHc8vT+26/8buArmAPqOYvCwhs42Tfe2kI7ycM2HpLu6wWe4/2ZOATd9QSmaa7UAAAAAWJLR0R2MWPJQQAAAAlwSFlzAAAPkgAAD5IBBKh+oAAAAAd0SU1FB+YLBhADComsJV8AAAHsSURBVDjLfVPpX9NAEN1FG1QOQegBpVAOkVNQ5L7lBkEERRQU8d5t0kAb2pKeW1iuv5rdHDQFmvch+WXfmzeT2RkADECny+2pqfV6a2s8bpcTgnxAZ52vvgEZaKj31eVJIPQ3NqE8NDX6IczxzS3oDp63Fj0w+Rdt6B60dzx0GPH38gh3djkELvB3888AxhYOB9hTfNnDBLD3lXYmBXMKjIMSf8mv+wQA3/TzeOngMBSWdF4Khw4PJOahDAwKoNenxQSPItHYsaaQjmPRyFGQ+anxoT7gGtZNQwlDofGJEE+IkyOjwK33D4fZMVdofDQWxloRY+PAYxSmE6l0OhW9SYYyZALc9EBXZLMWHp2QSTCFcgoWnGClpEyeOUwDb649UjobYcimTR7J5K2tACeZwC6FespS2BWpUDJj95v4jNBZu0aJ52RuvnCrA1gmZGGx8GXxCujScsHrvhDjhKy8EwoNzIV6SShdXS7mI7d2Z+QCSLwkhL5ff8Rn8vGHdgunWyjMn2xsCk/4WJeUdnwUrRIsyqw++mmrrFxfjJKnn7dlRcVXGqsqZ+csnH75WlFprtYzx87ut3hSzpxk5OQp5fT31XVHlWU7hb3BH/s/iQ46t/Dr95/iW/st7I2OT/z9R+n05Oz84v9q8/wavpxddWrqxfYAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjItMTEtMDZUMTY6MDM6MTArMDA6MDDZr/i+AAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIyLTExLTA2VDE2OjAzOjEwKzAwOjAwqPJAAgAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAASUVORK5CYII=')

            ]
        ]

        frame_nomeTabela = [
            [
                sg.In(size=self.__tamanho, font=self.__fonte, pad=self.__dist, enable_events=True, key='nomeTabela')
            ]
        ]

        frame_opcoes = [
            [
                sg.B(key='Adicionar', tooltip='Adicionar Atributo', size=(9, 1), pad=(5, 5), font=("Courier", 7),
                     image_data='iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAARbSURBVFiFzVdbiFVlGF3r2+egRhOZghNIIaMhhDHlkKYjKjVlXpqYSXvICKIbQQjTUw/BEPQQlBW+FEHQ5UFTnCYxafBSYzNOKSWZ5i1TfFDKCrWHcTz7Wz3sc/beZ5/LzFhQ/8u/93/51vrWXvvb/wb+48bxLJ574N381AuT7zT4AgC3kn6TQTkQf5Dhz4H73k/vf+I7kPpXCdy7fettRjxP+FpSUwgHKRCKegqWjJ0l1eOhv977wJNn/xGBJT09N1qer5B6jlA+AfUMeGYsuh8GsCGnkVc3tz17cdwElmzf3gz3LaQ3lQcWSgpYlbGEWEzoZN7Dhza1Pf1TNRyrNtjas2OJhxiQ2CQRApHtofQYKtck62YWLBhYvfv9xWNSYGFvXwsR7ibUkMkk7uPnXe2RpBSw8rE/cyrM33TfM8drKrCwt7dB0kaJDcVt1TOvMafUHCrnJhcY9D72+cc31CQQ+nWvSWyqDx7Lfc6dTaBmCTw/Cnhp3+zhCVdeqkrg7s++miHxqbFm7uC+nSs7T32xbM1Jdw7WBy/zxbqOPe9Nr1TgqncJzEt1wMvNFSZOslAaBTwhOMk892I5gW6Zg53KZCmgMmiaWMbPZXLX8YULHZAYE2iZs/ceiTdXANQDVyLeNZjyls6dHzbHBFxsTplrVPDIA+VWGucbAacWAUCumMFsgIAAEoAAMZKfxDkJ+wiEIgEJNAIIh2IFQg4xMKhIiyJEBBAWEGgsxUIxdrGfGRMIZQ1R0QCULABIFByt+zvbTqFO27WqfX218ba+LbPo4fFSrBQ4ZJocE4CQB5kBj1jncla1XI+l5a8W6GZxrHRsip4iYL8KykoUKRBq77ytuwZpComovAIA6UNftz+4HgAWb9vWZcB80BFAgDkoDwrUQgKRrGkFAFC8EBNw6BcDM+BA0ReNTnSYR4SiTkiXEIHzHVptIjzKrjivGuCAjKdjAmJuSCpkwBXLxpQpkyDpQ48B8uKaksYoe5Sl+/g21ABKaRw+0nJA4O/ZsolapTUqxQm+Zz7HNWpCqlj9dnnC9B9iAuimS/ZReZWrX1iUegQ+PnBI/ODLpUsLCQEAFnKDxHBM4FGQIPaAMxgzODgC6Z3S3rKCfvvGb98itY6ofcgoXRt03oKri8IwZzkL+0lNq7bPsoca6c2+FY90pdyTtMKkkZclnKmbeeKLRg9zJ4w6JnFatS8oErVKcycCDnenMcsIHGtvvRxasEripUrjoWZdr/8Riw36lwkdO5avvVSTAAAcXdNyCLSHK0hcE3jp2i7KuKxvZcePWbyqZfbwoy17QgtaJZ4umfKawZ3H3X3pnuXtA9Wwatb5o2taDsGunwPZ26W3Y3RwpOdG3Llh4sT8Xf3t7d/XwhnTr9kdn3wzQ/IXSH+cwNSy43j8ZyQQDprOm3wzvPDGYOeKM6PFHtfPKbplzbMH58o0z0wzAE0JoCuEhkUdyQU6OHSwfz+6u330YP+T9jfRS7E8s8wCmAAAAABJRU5ErkJggg=='),
                sg.B(key='Editar', tooltip='Editar Atributo', size=(9, 1), pad=(5, 5), font=("Courier", 7),
                     image_data='iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAjdQTFRF//////8A/////////6pV/0BAzJlm/6pV/99g1dXq/5VA/9VVyEk3yNvtzN3dz8/f/5Y8/8xZ/85Yvb3G01hG09Plztbmz9fn8FU+95s+8FdC1dXj67d2+ZhDZmxs/9Ne8FNA+plB/9Fb0tbi0tfj95dC4bGF0Nfm/9Bd3ayGQFdl/9Fc8FVAvMHN+plA0tXl1pxq+JdCPlVj71VA/9BcWWx541FA+ZhB/9Fc71RA+ZhA0dfl/9Bb/9Bc95pF99N3+ZhByZ551E49/9Fb0m5kxLm3+ZdB4bCG47KFyJ9671RA2Li++ZhB/9Bcfnt1+ZlB/89c8cJw0k8+1E89+ZhBx555/9Bc2tLJ/9Bd7MGMub3J0dbk27+t0dbk71RA+ZhB0dbk6tObo6+90tXh+ZhBuZZ2/Lxf/9Bc+rRb+7FZ+7Ja/Lpe/Lpf/Lxe0dbi+q9X+7ZdWGx60dbk7lpI+ZhB+7le/L9d/9Bcx5546HJm71RA+6xU+7de/cFe6bJ871Q/71ZC8rVu+7df/cNepZF73oF4+ZhB+qhQ+qpR+7he+7lf/9BcP1VjQVtrRVhju7fCvcLOxMnW0NXj0dXj0dbk0qN40qV+1aiA1cfR1k8+2KqB21A+26qs3KyD35iW36+F4rGG47KF5a187VRA71RA8LVw9ZpK97tt+ZhB+ZlC+ZtE+ZxF+Z1G+Z9H+aFM+qJK+qZO+stj+7hf/MNe/cdd/cte/she/sld/std/s1c/85c/89c/9BcqwI83QAAAIx0Uk5TAAEBAgMEBQYIDAwMDg4PEBEUGhsdHR8gISEjJCcqLS40Nzg+P0JFRkdKTFNUW19hamxvb3J4eH5/gIuRkZ6foaqrs7vBwsXGx8nLzc/T19vc3d/g4+Xm7O3u7+/v8PLy8/T19fb3+Pj5+fn5+fn6+vr7+/v7+/v7/Pz8/Pz8/f39/f39/v7+/v7+/v6nfTuYAAABe0lEQVQYGX3B9zuVcRgH4E9ypKVSnKK0l9VQaaC9pxGFIxpWQ0pLGhQlmb0qaXzlxXMa0lNpeP64Xr+c63Jdz+u+oZizK2OTB+6mZXb32oei4GpPV69t2wXxcJHQWm+PerAIqtm57dbb67YjCaq9bR2W9fqObVfPhWZdf77lePH+4RZoFpynz6fPWY7DHigmHSEq44EcyyqMhmYr0RNmHi66sgaa5Q30tY75nsh2aGZmkb+U+eKIZM+CZgfRXebGP9K0CppEom/M/EMkBZp5Z+jTVebLIkdDoQjeR1TBfOOvlCyEJploiJl/imyAZnEVfalhvimyewIUU46Tv5z50j85FQ5NGtFT5me/ReKgWdv5cZCZH4mkQrXzpbnfx8UjcmIqVAdfGWNqf8mtJdCdfGMcPd83Qxdy+50ZlR4MXcyFD8ZxYD5cxLY8Nmb/Crha/7z52GqMY2PlWZ9v5TbfWHlLERDh9XonTvaOFRmEgOkzFGEIiL5maZbB8R+GYqXo6gEqqgAAAABJRU5ErkJggg=='),
                sg.B(key='Excluir', tooltip='Excluir Atributo', size=(9, 1), pad=(5, 5), font=("Courier", 7),
                     image_data='iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAOmSURBVFiFtZfdTxxlFMZ/Z3ZhYWcWTC1NTdRak3qjoX4BaYzJAtJYiDeaWG/k0gsT45VRb9CojcWkif+BetFqTPTK0lQKbEzIgqQftFEvmhSN2hLrYoEZlgVmjhd8zcLszLC0z9057znned6vM/MKMVE41taQKmmPCh0Ch1EeQbgPAOUOwu+qcgVheHExebZpdHQ+Tl2JCpjrbH3MgHeB14B0TL0LwNeuIf2Ng+PXqxKgR47UO2nvY9C3gWRM4q1YBj433XSf5HKLsQXMdrUdSrj6PcITVRKXQWHMSLovm+cv3ooU4Lzw7FPqGecRmu4GuQ9/gfRYQ+NXKwpYm/loJXJpaATTCqdxbHRutrIIV1us3MT0NgGazdY5iYUx4HAg+d4m0l99B6lUuIDSIgu9r6CFf4PHhYumk3he8vki+A6Xkyh+Uol8vbA3fRPZszeUXwu3oVQKCeAZO73yHvDBqh42rtovVH/adwQBW109ZOUmppMAa/c8kDzZ1Y1x4GBVRN4fU6wMDmzzK1hiSB/wphSOtTWklvQWFZpM+tsBZM/9VQnQmQILr3ZXGnaKizUPGKmS9lQiB1DHrop8NTe0G5t1dUvdhgodoVXszSKlUydYGRncsJdPf8HymS837JWRQUqnTvhyI8V3JCXs5APqE+BNXkIyGWjvAsD99RoANevj13/Dm7y0mTs/F8EvzQYQesJ0PtZHLTjXDs8VeNQAGkKLhO/jrgQAjUZklV2sQJxcAwjdqBizqJwbvXqzBjB1zwRErIDCDUNVroRG7UJAjNxJA2E4LOJe3gKUIaPo1v8AOJWLRN3lkPrh4p2ilz5n7MvlbOCbygJ83UyEsn8YkTXfhqPMDmvjqnJmXy5nJwFcQ/oTnvay2dQ24VuB2jfeQh4+sGHXHH+9jDD54kskHm8OzN2CpRrDO4l/OnZn62fAO9tCxcD8cRQkumWUQT2co8+BegFjctIaHn8fVvsAAKab7lMYCyqk/83sjBxWcwLIFfJmqvDhul32U2pnW/aTkJ+Bh/x+yTSAldmZAns+4GOkNw1NtqaH838HCgCwO9uaQc8CD+6MMRJ/Ioke60L+mt+5bWOtofGrWrv8NPDT3WJWyONq61byQAEAmXOXb5u1M0cV/YiQHhEDS6CfWrUz7f63gB+Rj1M727JfDOlToRcwYxI7ip6uEfrrLkzcCAuMFLCOf7JZqz7h9IC0i/AkykFYe57DHYQphcugI8UVc2CtwUXif8gpb9cx33AXAAAAAElFTkSuQmCC')

            ]
        ]

        frame_conteudo = [
            [
                sg.T('Nome do Campo', size=self.__tamanho, pad=self.__dist, font=self.__fonte),
                sg.In(size=self.__tamanho, font=self.__fonte, pad=self.__dist, enable_events=True, key='nomeCampo')
            ],
            [
                sg.T('Composto', size=self.__tamanho, pad=self.__dist, font=self.__fonte),
                sg.CBox('', key='composto', enable_events=True),
            ],
            [
                sg.T('Chave Primária', size=self.__tamanho, pad=self.__dist, font=self.__fonte),
                sg.CBox('', key='chavePrimaria', enable_events=True)
            ],
            [
                sg.T('Tipo do Campo', size=self.__tamanho, pad=self.__dist, font=self.__fonte),
                sg.Combo(['VARCHAR',  'CHAR', 'INT', 'FLOAT', 'DECIMAL', 'DATE', 'DATETIME'], enable_events=True,
                         font=self.__fonte, size=self.__tamanho, key='tipoCampo')
            ],
            [
                sg.T('Tamanho', size=self.__tamanho, pad=self.__dist, font=self.__fonte),
                sg.In(size=self.__tamanho, font=self.__fonte, pad=self.__dist, enable_events=True, key='tamanhoCampo')
            ],
            [
                sg.T('Permitir Nulo', size=self.__tamanho, pad=self.__dist, font=self.__fonte),
                sg.CBox('', key='permitirNull', enable_events=True)
            ],
            [
                sg.T('Auto-Incremento', size=self.__tamanho, pad=self.__dist, font=self.__fonte),
                sg.CBox('', key='autoIncrement', enable_events=True)
            ],
            [
                sg.T('Multivalorado', size=self.__tamanho, pad=self.__dist, font=self.__fonte),
                sg.CBox('', key='multiValor', enable_events=True)
            ]
        ]

        frame_esquerda = [
            [
                sg.Fr('Nome da Tabela', layout=frame_nomeTabela, font=self.__fonte, pad=self.__dist),
                sg.Fr('Opções', layout=frame_opcoes, font=self.__fonte, pad=self.__dist)
            ],
            [
                sg.Fr('Campos do Formulário', layout=frame_conteudo, font=self.__fonte, pad=self.__dist)
            ],
        ]

        frame_visualizacao = [
            [
                sg.LB([], size=(107, 21), pad=self.__dist, font=self.__fonte, key='visualizacaoColuna', enable_events=True)
            ]
        ]

        layout = [
            [
                sg.Fr('', layout=frame_cabecalho, border_width=0, pad=(0, 5))
            ],
            [
                sg.Fr('', layout=frame_esquerda, border_width=0),
                sg.Fr('Visualização', layout=frame_visualizacao)
            ]
        ]

        return sg.Window('Inicio', layout=layout, finalize=True)

    def janelaChvComposta(self):

        frame_atributo = [
            [
                sg.Combo(values=self.__tabela.getCompostos(), enable_events=True, font=self.__fonte,
                         size=self.__tamanho, key='escolhaAtributos')
            ]
        ]

        frame_opcoes = [
            [
                sg.B(key='Adicionar', tooltip='Adicionar Atributo', size=(9, 1), pad=(5, 5), enable_events=True,
                     image_data='iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAARbSURBVFiFzVdbiFVlGF3r2+egRhOZghNIIaMhhDHlkKYjKjVlXpqYSXvICKIbQQjTUw/BEPQQlBW+FEHQ5UFTnCYxafBSYzNOKSWZ5i1TfFDKCrWHcTz7Wz3sc/beZ5/LzFhQ/8u/93/51vrWXvvb/wb+48bxLJ574N381AuT7zT4AgC3kn6TQTkQf5Dhz4H73k/vf+I7kPpXCdy7fettRjxP+FpSUwgHKRCKegqWjJ0l1eOhv977wJNn/xGBJT09N1qer5B6jlA+AfUMeGYsuh8GsCGnkVc3tz17cdwElmzf3gz3LaQ3lQcWSgpYlbGEWEzoZN7Dhza1Pf1TNRyrNtjas2OJhxiQ2CQRApHtofQYKtck62YWLBhYvfv9xWNSYGFvXwsR7ibUkMkk7uPnXe2RpBSw8rE/cyrM33TfM8drKrCwt7dB0kaJDcVt1TOvMafUHCrnJhcY9D72+cc31CQQ+nWvSWyqDx7Lfc6dTaBmCTw/Cnhp3+zhCVdeqkrg7s++miHxqbFm7uC+nSs7T32xbM1Jdw7WBy/zxbqOPe9Nr1TgqncJzEt1wMvNFSZOslAaBTwhOMk892I5gW6Zg53KZCmgMmiaWMbPZXLX8YULHZAYE2iZs/ceiTdXANQDVyLeNZjyls6dHzbHBFxsTplrVPDIA+VWGucbAacWAUCumMFsgIAAEoAAMZKfxDkJ+wiEIgEJNAIIh2IFQg4xMKhIiyJEBBAWEGgsxUIxdrGfGRMIZQ1R0QCULABIFByt+zvbTqFO27WqfX218ba+LbPo4fFSrBQ4ZJocE4CQB5kBj1jncla1XI+l5a8W6GZxrHRsip4iYL8KykoUKRBq77ytuwZpComovAIA6UNftz+4HgAWb9vWZcB80BFAgDkoDwrUQgKRrGkFAFC8EBNw6BcDM+BA0ReNTnSYR4SiTkiXEIHzHVptIjzKrjivGuCAjKdjAmJuSCpkwBXLxpQpkyDpQ48B8uKaksYoe5Sl+/g21ABKaRw+0nJA4O/ZsolapTUqxQm+Zz7HNWpCqlj9dnnC9B9iAuimS/ZReZWrX1iUegQ+PnBI/ODLpUsLCQEAFnKDxHBM4FGQIPaAMxgzODgC6Z3S3rKCfvvGb98itY6ofcgoXRt03oKri8IwZzkL+0lNq7bPsoca6c2+FY90pdyTtMKkkZclnKmbeeKLRg9zJ4w6JnFatS8oErVKcycCDnenMcsIHGtvvRxasEripUrjoWZdr/8Riw36lwkdO5avvVSTAAAcXdNyCLSHK0hcE3jp2i7KuKxvZcePWbyqZfbwoy17QgtaJZ4umfKawZ3H3X3pnuXtA9Wwatb5o2taDsGunwPZ26W3Y3RwpOdG3Llh4sT8Xf3t7d/XwhnTr9kdn3wzQ/IXSH+cwNSy43j8ZyQQDprOm3wzvPDGYOeKM6PFHtfPKbplzbMH58o0z0wzAE0JoCuEhkUdyQU6OHSwfz+6u330YP+T9jfRS7E8s8wCmAAAAABJRU5ErkJggg=='),
                sg.B(key='Editar', tooltip='Editar Atributo', size=(9, 1), pad=(5, 5),
                     image_data='iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAjdQTFRF//////8A/////////6pV/0BAzJlm/6pV/99g1dXq/5VA/9VVyEk3yNvtzN3dz8/f/5Y8/8xZ/85Yvb3G01hG09Plztbmz9fn8FU+95s+8FdC1dXj67d2+ZhDZmxs/9Ne8FNA+plB/9Fb0tbi0tfj95dC4bGF0Nfm/9Bd3ayGQFdl/9Fc8FVAvMHN+plA0tXl1pxq+JdCPlVj71VA/9BcWWx541FA+ZhB/9Fc71RA+ZhA0dfl/9Bb/9Bc95pF99N3+ZhByZ551E49/9Fb0m5kxLm3+ZdB4bCG47KFyJ9671RA2Li++ZhB/9Bcfnt1+ZlB/89c8cJw0k8+1E89+ZhBx555/9Bc2tLJ/9Bd7MGMub3J0dbk27+t0dbk71RA+ZhB0dbk6tObo6+90tXh+ZhBuZZ2/Lxf/9Bc+rRb+7FZ+7Ja/Lpe/Lpf/Lxe0dbi+q9X+7ZdWGx60dbk7lpI+ZhB+7le/L9d/9Bcx5546HJm71RA+6xU+7de/cFe6bJ871Q/71ZC8rVu+7df/cNepZF73oF4+ZhB+qhQ+qpR+7he+7lf/9BcP1VjQVtrRVhju7fCvcLOxMnW0NXj0dXj0dbk0qN40qV+1aiA1cfR1k8+2KqB21A+26qs3KyD35iW36+F4rGG47KF5a187VRA71RA8LVw9ZpK97tt+ZhB+ZlC+ZtE+ZxF+Z1G+Z9H+aFM+qJK+qZO+stj+7hf/MNe/cdd/cte/she/sld/std/s1c/85c/89c/9BcqwI83QAAAIx0Uk5TAAEBAgMEBQYIDAwMDg4PEBEUGhsdHR8gISEjJCcqLS40Nzg+P0JFRkdKTFNUW19hamxvb3J4eH5/gIuRkZ6foaqrs7vBwsXGx8nLzc/T19vc3d/g4+Xm7O3u7+/v8PLy8/T19fb3+Pj5+fn5+fn6+vr7+/v7+/v7/Pz8/Pz8/f39/f39/v7+/v7+/v6nfTuYAAABe0lEQVQYGX3B9zuVcRgH4E9ypKVSnKK0l9VQaaC9pxGFIxpWQ0pLGhQlmb0qaXzlxXMa0lNpeP64Xr+c63Jdz+u+oZizK2OTB+6mZXb32oei4GpPV69t2wXxcJHQWm+PerAIqtm57dbb67YjCaq9bR2W9fqObVfPhWZdf77lePH+4RZoFpynz6fPWY7DHigmHSEq44EcyyqMhmYr0RNmHi66sgaa5Q30tY75nsh2aGZmkb+U+eKIZM+CZgfRXebGP9K0CppEom/M/EMkBZp5Z+jTVebLIkdDoQjeR1TBfOOvlCyEJploiJl/imyAZnEVfalhvimyewIUU46Tv5z50j85FQ5NGtFT5me/ReKgWdv5cZCZH4mkQrXzpbnfx8UjcmIqVAdfGWNqf8mtJdCdfGMcPd83Qxdy+50ZlR4MXcyFD8ZxYD5cxLY8Nmb/Crha/7z52GqMY2PlWZ9v5TbfWHlLERDh9XonTvaOFRmEgOkzFGEIiL5maZbB8R+GYqXo6gEqqgAAAABJRU5ErkJggg=='),
                sg.B(key='Remover', tooltip='Remover Atributo', size=(9, 1), pad=(5, 5), enable_events=True,
                     image_data='iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAOmSURBVFiFtZfdTxxlFMZ/Z3ZhYWcWTC1NTdRak3qjoX4BaYzJAtJYiDeaWG/k0gsT45VRb9CojcWkif+BetFqTPTK0lQKbEzIgqQftFEvmhSN2hLrYoEZlgVmjhd8zcLszLC0z9057znned6vM/MKMVE41taQKmmPCh0Ch1EeQbgPAOUOwu+qcgVheHExebZpdHQ+Tl2JCpjrbH3MgHeB14B0TL0LwNeuIf2Ng+PXqxKgR47UO2nvY9C3gWRM4q1YBj433XSf5HKLsQXMdrUdSrj6PcITVRKXQWHMSLovm+cv3ooU4Lzw7FPqGecRmu4GuQ9/gfRYQ+NXKwpYm/loJXJpaATTCqdxbHRutrIIV1us3MT0NgGazdY5iYUx4HAg+d4m0l99B6lUuIDSIgu9r6CFf4PHhYumk3he8vki+A6Xkyh+Uol8vbA3fRPZszeUXwu3oVQKCeAZO73yHvDBqh42rtovVH/adwQBW109ZOUmppMAa/c8kDzZ1Y1x4GBVRN4fU6wMDmzzK1hiSB/wphSOtTWklvQWFZpM+tsBZM/9VQnQmQILr3ZXGnaKizUPGKmS9lQiB1DHrop8NTe0G5t1dUvdhgodoVXszSKlUydYGRncsJdPf8HymS837JWRQUqnTvhyI8V3JCXs5APqE+BNXkIyGWjvAsD99RoANevj13/Dm7y0mTs/F8EvzQYQesJ0PtZHLTjXDs8VeNQAGkKLhO/jrgQAjUZklV2sQJxcAwjdqBizqJwbvXqzBjB1zwRErIDCDUNVroRG7UJAjNxJA2E4LOJe3gKUIaPo1v8AOJWLRN3lkPrh4p2ilz5n7MvlbOCbygJ83UyEsn8YkTXfhqPMDmvjqnJmXy5nJwFcQ/oTnvay2dQ24VuB2jfeQh4+sGHXHH+9jDD54kskHm8OzN2CpRrDO4l/OnZn62fAO9tCxcD8cRQkumWUQT2co8+BegFjctIaHn8fVvsAAKab7lMYCyqk/83sjBxWcwLIFfJmqvDhul32U2pnW/aTkJ+Bh/x+yTSAldmZAns+4GOkNw1NtqaH838HCgCwO9uaQc8CD+6MMRJ/Ioke60L+mt+5bWOtofGrWrv8NPDT3WJWyONq61byQAEAmXOXb5u1M0cV/YiQHhEDS6CfWrUz7f63gB+Rj1M727JfDOlToRcwYxI7ip6uEfrrLkzcCAuMFLCOf7JZqz7h9IC0i/AkykFYe57DHYQphcugI8UVc2CtwUXif8gpb9cx33AXAAAAAElFTkSuQmCC'),
                sg.B(key='Finalizar', tooltip='Finalizar', size=(9, 1), pad=(5, 5), enable_events=True,
                     image_data='iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAANwSURBVFiFxZddTFxFFMd/Zy67XflYsInWPlgBm9Y0KSUampiQ2KKRsMVd3XZjosYXNb77Ym1TNCgUTFt91gffmkhtkd0AsYkkRaVU/EhNfWj8IGETW1KjKEL2697jw7LYLh97WVj8P93JnDm/f2bmzpwRXCo4EKzKOKbdqLY4yD7BqQWpyfbqDMgkcBV0xLIYjIais27ySqGA1vPh7ZbYHQIvAuUu/c4LnDWW9kZD0Z+LMhDpi9w170m+gSOvIVS4BOcrDZxxfKk3hwPDSdcGggPBnbYtF4C9RYLvlDJmlWk4GopOFzQQ6H+60ah+pnDvhsAXPRAXTGAw3H9tRQPBgeBOx5avNhp+G23KMrr/9pkwuY8DHx3w2bacKxkcQNlh29LfNtS2ZYmBihr/MaCxZPD/9KiV8L6Vawhkf7Uy7J/WsdvXqpQjsmf4mU9/MQCW2B2bCAfwGtXXAaRtqM1vEt4buD9kCkoQjuwKY8Tw8fVzywcpc+W2974ySW45BLqh8FcaXiL4YDvzmXn6rn+CossFVsx50gFjVFtKAc84GU5NvLc8PBfvOI8bB9lXCnj3lV6+vjmx+hiRBiNo3f8BX1C9AfyrJX7/4GlOPdZLlbeqIDztpHlnvNstHIVqUyjIYzw8tHU3Xc2dS0zkw7vGT/LN9Heu4DkZ4O+VHSrHv+xgajZOfXUd3c1v4/f6l8AzToaTV95dM1zgL6PZSmZFzSRnOPbFCaZm49RV19LV3Inf6y92zfP1q7Xr2d1NwCOrRSXsBJd/G6dpexMP+HfwZO0TNNyzd3HaJ6a/LQYOMGhAR9xE/pH4k6Ojx5majVPlrSp62u+Ufi6RvkjlfFnqBlDpZshW3928sOd5LsVHuXrrh3Wws0exALRfCH2o8HLx2YoxoB8MHo6+agCMpb1kC8jNUtJ4tAcWCpKF0vnMJho4HQvGJhcNANy8te0EMFpytDLm+FKduWZ+UbotY8uEwP0lga9WlAJEQ9FpwQQU4qWAG9sJ5L8NltwFg+H+a5bHeVjRSxsGV8Yso/tjR2I/5nctexnFnor9rr50q0APkFoHOgV0l9veg8u9isDF4/TQ+cP1SOYoynNrKFz/QfWs8WhPbrevpIIGcor0RSrnPOmAqLagNIpQp1CzkGRGlUkVvhd0JF2RGLrYenHOTd5/AbNNa+7OUGbqAAAAAElFTkSuQmCC')

            ]
        ]

        frame_campos = [
            [
                sg.T('Nome do Atributo', size=self.__tamanho, pad=self.__dist, font=self.__fonte),
                sg.In(size=self.__tamanho, font=self.__fonte, pad=self.__dist, enable_events=True, key='nomeAtributo')
            ],
            [
                sg.T('Chave Primária', size=self.__tamanho, pad=self.__dist, font=self.__fonte),
                sg.CBox('', enable_events=True, key='chavePrimaria')
            ],
            [
                sg.T('Tipo do Campo', size=self.__tamanho, pad=self.__dist, font=self.__fonte),
                sg.Combo(['VARCHAR',  'CHAR', 'INT', 'FLOAT', 'DECIMAL', 'DATE', 'DATETIME'], enable_events=True,
                         font=self.__fonte, size=self.__tamanho, key='tipoCampo')
            ],
            [
                sg.T('Tamanho', size=self.__tamanho, pad=self.__dist, font=self.__fonte),
                sg.In(size=self.__tamanho, font=self.__fonte, pad=self.__dist, enable_events=True, key='tamanhoCampo')
            ],
            [
                sg.T('Permitir Nulo', size=self.__tamanho, pad=self.__dist, font=self.__fonte),
                sg.CBox('', key='permitirNull', enable_events=True)
            ],
            [
                sg.T('Auto-Incremento', size=self.__tamanho, pad=self.__dist, font=self.__fonte),
                sg.CBox('', key='autoIncrement', enable_events=True)
            ]
        ]
        frame_visualizacao = [
            [
                sg.LB([], size=(107, 16), pad=self.__dist, font=self.__fonte, key='visualizacaoChvComposta', enable_events=True)
            ]
        ]

        frame_esquerda = [
            [
                sg.Fr('Atributo', layout=frame_atributo),
                sg.Fr('Opções', layout=frame_opcoes)
            ],
            [
                sg.Fr('Campo da Tabela', layout=frame_campos)
            ]
        ]

        layout = [
            [
                sg.Fr('', layout=frame_esquerda, border_width=0),
                sg.Fr('Visualização', layout=frame_visualizacao)
            ]
        ]

        return sg.Window('AtributoComposto', layout=layout, finalize=True)

    def janelaCriaTabela(self):

        frame_opcoes = [
            [
                sg.B('Adicionar', size=(9, 1), pad=(5, 5), font=("Arial", 7)),
                sg.B('Excluir', size=(9, 1), pad=(5, 5), font=("Arial", 7))
            ]
        ]

        frame_nomeTabela = [
            [
                sg.T('Nome da Tabela', size=self.__tamanho, font=self.__fonte, pad=self.__dist),
                sg.In(size=self.__tamanho, font=self.__fonte, pad=self.__dist, enable_events=True, key='nomeTabela')
            ]
        ]

        frame_escolheTabela = [
            [
                sg.Combo(self.__tabela.getNomeTabelas(), enable_events=True, font=self.__fonte, size=self.__tamanho,
                         key='escolheTabela'),
                sg.Multiline("", size=(107, 16), pad=self.__dist, key='visualizacaoTabela', font=self.__fonte,
                             do_not_clear=False)
            ]
        ]

        frame_esquerda = [
            [
                sg.Fr('', layout=frame_nomeTabela, border_width=0)
            ],
            [
                sg.Fr('', layout=frame_opcoes, border_width=0)
            ]
        ]

        layout = [
            [
                sg.Fr('Criaçao de Tabelas', layout=frame_esquerda),
                sg.Fr('Visualização', layout=frame_escolheTabela)
            ]
        ]

        return sg.Window('CriaTabela', layout=layout, finalize=True)

    def janelaNormalizacao(self):
        frame_visualizacao = [
            [
                sg.Combo(values=self.__tabela.getNomeTabelas(), enable_events=True, font=self.__fonte,
                         size=self.__tamanho, key='escolheTabela')
            ],
            [
                sg.LB([], size=(107, 16), pad=self.__dist, key='visualizacaoNormalizacao', font=self.__fonte, enable_events=True)
            ]
        ]

        frame_opcoes = [
            [
                sg.B('1ª FN', enable_events=True, size=self.__tamanho, pad=self.__dist, font=self.__fonte,
                     key='primeira'),
                sg.B('2ª/3ª FN', enable_events=True, size=self.__tamanho, pad=self.__dist, font=self.__fonte,
                     key='segunda', disabled=True),
                sg.B('Gerar Script', enable_events=True, size=self.__tamanho, pad=self.__dist, font=self.__fonte,
                     key='Script', disabled=True),
                sg.B('Visualizar Script', enable_events=True, size=self.__tamanho, pad=self.__dist, font=self.__fonte,
                     key='Visualizar', disabled=True)
            ]
        ]

        layout = [
            [
                sg.Fr('Visualização', layout=frame_visualizacao)
            ],
            [
                sg.Fr('Opções', layout=frame_opcoes)
            ]
        ]

        return sg.Window('Normalização', layout=layout, finalize=True)

    def janelaDependencias(self):
        frame_visualizacao = [
            [
                sg.LB([], size=(107, 16), pad=self.__dist, key='visualizacaoDependencias', font=self.__fonte, enable_events=True)
            ]
        ]

        frame_determinantes = [
            [
                sg.LB(values=self.__tabela.getNomeColunas(nomeTabela=self.__tabelaInicial), select_mode='multiple',
                      enable_events=True, size=(25, 7), key='determinantes')
            ]
        ]

        frame_dependentes = [
            [
                sg.LB(values=self.__tabela.getNomeColunas(nomeTabela=self.__tabelaInicial), select_mode='multiple',
                      enable_events=True, size=(25, 7), key='dependentes')
            ]
        ]

        frame_seleciona = [
            [
                sg.T(' ', size=(15, 2))
            ],
            [
                sg.T(' ', size=(13, 3)),
                sg.Image(source=r'.\\right-arrow.png'),
                sg.T(' ', size=(13, 3)),
            ],
            [
                sg.T(' ', size=(15, 3)),
                sg.B(
                    image_data='iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAARbSURBVFiFzVdbiFVlGF3r2+egRhOZghNIIaMhhDHlkKYjKjVlXpqYSXvICKIbQQjTUw/BEPQQlBW+FEHQ5UFTnCYxafBSYzNOKSWZ5i1TfFDKCrWHcTz7Wz3sc/beZ5/LzFhQ/8u/93/51vrWXvvb/wb+48bxLJ574N381AuT7zT4AgC3kn6TQTkQf5Dhz4H73k/vf+I7kPpXCdy7fettRjxP+FpSUwgHKRCKegqWjJ0l1eOhv977wJNn/xGBJT09N1qer5B6jlA+AfUMeGYsuh8GsCGnkVc3tz17cdwElmzf3gz3LaQ3lQcWSgpYlbGEWEzoZN7Dhza1Pf1TNRyrNtjas2OJhxiQ2CQRApHtofQYKtck62YWLBhYvfv9xWNSYGFvXwsR7ibUkMkk7uPnXe2RpBSw8rE/cyrM33TfM8drKrCwt7dB0kaJDcVt1TOvMafUHCrnJhcY9D72+cc31CQQ+nWvSWyqDx7Lfc6dTaBmCTw/Cnhp3+zhCVdeqkrg7s++miHxqbFm7uC+nSs7T32xbM1Jdw7WBy/zxbqOPe9Nr1TgqncJzEt1wMvNFSZOslAaBTwhOMk892I5gW6Zg53KZCmgMmiaWMbPZXLX8YULHZAYE2iZs/ceiTdXANQDVyLeNZjyls6dHzbHBFxsTplrVPDIA+VWGucbAacWAUCumMFsgIAAEoAAMZKfxDkJ+wiEIgEJNAIIh2IFQg4xMKhIiyJEBBAWEGgsxUIxdrGfGRMIZQ1R0QCULABIFByt+zvbTqFO27WqfX218ba+LbPo4fFSrBQ4ZJocE4CQB5kBj1jncla1XI+l5a8W6GZxrHRsip4iYL8KykoUKRBq77ytuwZpComovAIA6UNftz+4HgAWb9vWZcB80BFAgDkoDwrUQgKRrGkFAFC8EBNw6BcDM+BA0ReNTnSYR4SiTkiXEIHzHVptIjzKrjivGuCAjKdjAmJuSCpkwBXLxpQpkyDpQ48B8uKaksYoe5Sl+/g21ABKaRw+0nJA4O/ZsolapTUqxQm+Zz7HNWpCqlj9dnnC9B9iAuimS/ZReZWrX1iUegQ+PnBI/ODLpUsLCQEAFnKDxHBM4FGQIPaAMxgzODgC6Z3S3rKCfvvGb98itY6ofcgoXRt03oKri8IwZzkL+0lNq7bPsoca6c2+FY90pdyTtMKkkZclnKmbeeKLRg9zJ4w6JnFatS8oErVKcycCDnenMcsIHGtvvRxasEripUrjoWZdr/8Riw36lwkdO5avvVSTAAAcXdNyCLSHK0hcE3jp2i7KuKxvZcePWbyqZfbwoy17QgtaJZ4umfKawZ3H3X3pnuXtA9Wwatb5o2taDsGunwPZ26W3Y3RwpOdG3Llh4sT8Xf3t7d/XwhnTr9kdn3wzQ/IXSH+cwNSy43j8ZyQQDprOm3wzvPDGYOeKM6PFHtfPKbplzbMH58o0z0wzAE0JoCuEhkUdyQU6OHSwfz+6u330YP+T9jfRS7E8s8wCmAAAAABJRU5ErkJggg==',
                    size=self.__tamanho, font=self.__fonte, pad=self.__dist, enable_events=True,
                    key='Adicionar', tooltip="Adicionar Dependência Funcional"),
                sg.T(' ', size=(15, 3))
            ]
        ]

        frame_opcoes = [
            [
                sg.B(size=self.__tamanho, font=self.__fonte, pad=self.__dist, enable_events=True,
                     key='Excluir',
                     image_data='iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAOmSURBVFiFtZfdTxxlFMZ/Z3ZhYWcWTC1NTdRak3qjoX4BaYzJAtJYiDeaWG/k0gsT45VRb9CojcWkif+BetFqTPTK0lQKbEzIgqQftFEvmhSN2hLrYoEZlgVmjhd8zcLszLC0z9057znned6vM/MKMVE41taQKmmPCh0Ch1EeQbgPAOUOwu+qcgVheHExebZpdHQ+Tl2JCpjrbH3MgHeB14B0TL0LwNeuIf2Ng+PXqxKgR47UO2nvY9C3gWRM4q1YBj433XSf5HKLsQXMdrUdSrj6PcITVRKXQWHMSLovm+cv3ooU4Lzw7FPqGecRmu4GuQ9/gfRYQ+NXKwpYm/loJXJpaATTCqdxbHRutrIIV1us3MT0NgGazdY5iYUx4HAg+d4m0l99B6lUuIDSIgu9r6CFf4PHhYumk3he8vki+A6Xkyh+Uol8vbA3fRPZszeUXwu3oVQKCeAZO73yHvDBqh42rtovVH/adwQBW109ZOUmppMAa/c8kDzZ1Y1x4GBVRN4fU6wMDmzzK1hiSB/wphSOtTWklvQWFZpM+tsBZM/9VQnQmQILr3ZXGnaKizUPGKmS9lQiB1DHrop8NTe0G5t1dUvdhgodoVXszSKlUydYGRncsJdPf8HymS837JWRQUqnTvhyI8V3JCXs5APqE+BNXkIyGWjvAsD99RoANevj13/Dm7y0mTs/F8EvzQYQesJ0PtZHLTjXDs8VeNQAGkKLhO/jrgQAjUZklV2sQJxcAwjdqBizqJwbvXqzBjB1zwRErIDCDUNVroRG7UJAjNxJA2E4LOJe3gKUIaPo1v8AOJWLRN3lkPrh4p2ilz5n7MvlbOCbygJ83UyEsn8YkTXfhqPMDmvjqnJmXy5nJwFcQ/oTnvay2dQ24VuB2jfeQh4+sGHXHH+9jDD54kskHm8OzN2CpRrDO4l/OnZn62fAO9tCxcD8cRQkumWUQT2co8+BegFjctIaHn8fVvsAAKab7lMYCyqk/83sjBxWcwLIFfJmqvDhul32U2pnW/aTkJ+Bh/x+yTSAldmZAns+4GOkNw1NtqaH838HCgCwO9uaQc8CD+6MMRJ/Ioke60L+mt+5bWOtofGrWrv8NPDT3WJWyONq61byQAEAmXOXb5u1M0cV/YiQHhEDS6CfWrUz7f63gB+Rj1M727JfDOlToRcwYxI7ip6uEfrrLkzcCAuMFLCOf7JZqz7h9IC0i/AkykFYe57DHYQphcugI8UVc2CtwUXif8gpb9cx33AXAAAAAElFTkSuQmCC')
            ],
            [
                sg.B(size=self.__tamanho, font=self.__fonte, pad=self.__dist, enable_events=True,
                     key='Normalizar',
                     image_data='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')
            ],
            [
                sg.B(size=self.__tamanho, font=self.__fonte, pad=self.__dist, enable_events=True,
                     key='Continuar',
                     image_data='iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAANwSURBVFiFxZddTFxFFMd/Zy67XflYsInWPlgBm9Y0KSUampiQ2KKRsMVd3XZjosYXNb77Ym1TNCgUTFt91gffmkhtkd0AsYkkRaVU/EhNfWj8IGETW1KjKEL2697jw7LYLh97WVj8P93JnDm/f2bmzpwRXCo4EKzKOKbdqLY4yD7BqQWpyfbqDMgkcBV0xLIYjIais27ySqGA1vPh7ZbYHQIvAuUu/c4LnDWW9kZD0Z+LMhDpi9w170m+gSOvIVS4BOcrDZxxfKk3hwPDSdcGggPBnbYtF4C9RYLvlDJmlWk4GopOFzQQ6H+60ah+pnDvhsAXPRAXTGAw3H9tRQPBgeBOx5avNhp+G23KMrr/9pkwuY8DHx3w2bacKxkcQNlh29LfNtS2ZYmBihr/MaCxZPD/9KiV8L6Vawhkf7Uy7J/WsdvXqpQjsmf4mU9/MQCW2B2bCAfwGtXXAaRtqM1vEt4buD9kCkoQjuwKY8Tw8fVzywcpc+W2974ySW45BLqh8FcaXiL4YDvzmXn6rn+CossFVsx50gFjVFtKAc84GU5NvLc8PBfvOI8bB9lXCnj3lV6+vjmx+hiRBiNo3f8BX1C9AfyrJX7/4GlOPdZLlbeqIDztpHlnvNstHIVqUyjIYzw8tHU3Xc2dS0zkw7vGT/LN9Heu4DkZ4O+VHSrHv+xgajZOfXUd3c1v4/f6l8AzToaTV95dM1zgL6PZSmZFzSRnOPbFCaZm49RV19LV3Inf6y92zfP1q7Xr2d1NwCOrRSXsBJd/G6dpexMP+HfwZO0TNNyzd3HaJ6a/LQYOMGhAR9xE/pH4k6Ojx5majVPlrSp62u+Ufi6RvkjlfFnqBlDpZshW3928sOd5LsVHuXrrh3Wws0exALRfCH2o8HLx2YoxoB8MHo6+agCMpb1kC8jNUtJ4tAcWCpKF0vnMJho4HQvGJhcNANy8te0EMFpytDLm+FKduWZ+UbotY8uEwP0lga9WlAJEQ9FpwQQU4qWAG9sJ5L8NltwFg+H+a5bHeVjRSxsGV8Yso/tjR2I/5nctexnFnor9rr50q0APkFoHOgV0l9veg8u9isDF4/TQ+cP1SOYoynNrKFz/QfWs8WhPbrevpIIGcor0RSrnPOmAqLagNIpQp1CzkGRGlUkVvhd0JF2RGLrYenHOTd5/AbNNa+7OUGbqAAAAAElFTkSuQmCC')
            ]
        ]

        frame_baixo = [
            [
                sg.Fr('Determinantes', layout=frame_determinantes),
                sg.Fr('', border_width=0, layout=frame_seleciona),
                sg.Fr('Dependentes', layout=frame_dependentes)
            ]
        ]

        layout = [
            [
                sg.Fr('Visualização', layout=frame_visualizacao)
            ],
            [
                sg.Fr('Selecione as dependencias', layout=frame_baixo),
                sg.Fr('Opções', layout=frame_opcoes)
            ]
        ]

        return sg.Window('Dependencias', layout=layout, finalize=True)

    def janelaConexao(self):

        frame_local = [
            [
                sg.T('', size=(10, 1)),
                sg.Check('local', size=self.__tamanho, font=self.__fonte, enable_events=True, key='local')
            ]
        ]

        frame_ip = [
            [

                sg.T('IP: ', size=self.__tamanho, font=self.__fonte),
                sg.T('', size=(8, 1)),
                sg.I('', font=self.__fonte, size=self.__tamanho,enable_events=True, key='ip')
            ]
        ]

        frame_user = [
            [
                sg.T('User:', size=self.__tamanho, font=self.__fonte),
                sg.T('', size=(8, 1)),
                sg.I('', size=self.__tamanho, font=self.__fonte, enable_events=True, key='user')
            ]
        ]

        frame_pass = [
            [
                sg.T('Password:', size=self.__tamanho, font=self.__fonte),
                sg.T('', size=(8, 1)),
                sg.I('', size=self.__tamanho, font=self.__fonte, enable_events=True, key='pass')
            ]
        ]

        frame_nome = [
            [
                sg.T('Nome:', size=self.__tamanho, font=self.__fonte),
                sg.T('', size=(8, 1)),
                sg.I('', size=self.__tamanho, font=self.__fonte, enable_events=True, key='nome')
            ]
        ]

        frame_opcoes = [
            [
                sg.B('Conectar', size=self.__tamanho, font=self.__fonte, enable_events=True, key='Conectar'),
                sg.T('', size=(6, 1)),
                sg.B('Fechar', size=self.__tamanho, font=self.__fonte, enable_events=True, key='Fechar')
            ]
        ]

        layout = [
            [
                sg.Fr('', layout=frame_local, border_width=0)
            ],
            [
                sg.Fr('', layout=frame_ip, border_width=0)
            ],
            [
                sg.Fr('', layout=frame_user, border_width=0)
            ],
            [
                sg.Fr('', layout=frame_pass, border_width=0)
            ],
            [
                sg.Fr('', layout=frame_nome, border_width=0)
            ],
            [
                sg.Fr('', layout=frame_opcoes)
            ]
        ]

        return sg.Window('Conexão com SGBD', layout=layout, finalize=True)

    def janelaVisualizaScript(self):
        frame_visualizacao = [
            [
                sg.ML('', size=(70, 25), font=self.__fonte, key='visualizacaoscript')
            ]
        ]

        frame_opcoes = [
            [
                sg.B('Conectar', size=self.__tamanho, font=self.__fonte, enable_events=True, key='Conectar'),
                sg.B('Salvar', size=self.__tamanho, font=self.__fonte, enable_events=True, key='Salvar'),
                sg.B('Voltar', size=self.__tamanho, font=self.__fonte, enable_events=True, key='Voltar')
            ]
        ]

        layout = [
            [
                sg.Fr('Visualização', layout=frame_visualizacao)
            ],
            [
                sg.Fr('Opções', layout=frame_opcoes)
            ]
        ]

        return sg.Window('Script', layout=layout, finalize=True)

    def janelaAlteraNome(self):

        frame_visualizacao = [
            [
                sg.Combo(values=self.__tabela.getNomeTabelas(), enable_events=True, font=self.__fonte,
                         size=self.__tamanho, key='escolheTabela')
            ],
            [
                sg.LB([], size=(107, 16), pad=self.__dist, key='visualizacaoRelacoes', font=self.__fonte, enable_events=True)
            ]
        ]

        frame_opcoes = [
            [
                sg.I('', size=self.__tamanho, font=self.__fonte, pad=self.__dist, enable_events=True, key='NomeTabela'),
                sg.B('Alterar', size=self.__tamanho, font=self.__fonte, pad=self.__dist, enable_events=True,
                     key='Alterar')
            ]
        ]

        frame_continuar = [
            [
                sg.T('', size=(40, 1)),
                sg.B('Continuar', size=self.__tamanho, font=self.__fonte, pad=self.__dist, enable_events=True,
                     key='Continuar')
            ]
        ]

        layout = [
            [
                sg.Fr('Visualização', layout=frame_visualizacao)
            ],
            [
                sg.Fr('Nome da Tabela', layout=frame_opcoes),
                sg.Fr('', layout=frame_continuar, border_width=0)
            ]
        ]

        return sg.Window('Alterar nomes das tabelas', layout=layout, finalize=True)

    def manter(self):
        nomeTabela = ''
        nomeColuna = ''
        pk = False
        tipoCampo = 'Varchar'
        tamanho = 255
        null = False
        increment = False
        composto = False
        multiValor = False
        nomeNovaTabela = None
        ip = None
        user = None
        password = None
        nome = None
        determinantes = []
        dependentes = []

        janelaNormalizacao = None
        janelaChvComposta = None
        janelaAlteraNome = None
        janelaDependencias = None
        janelaConexao = None
        janelaVisualizaScript = None
        janelaCriaColuna = self.janelaCriaColuna()

        while True:
            window, event, values = sg.read_all_windows()

            if window ==  janelaCriaColuna and event == 'Novo':
                if sg.PopupYesNo('Todos os dados da tabela atual serão excluídos.\n Concorda com isso?') == 'Yes':
                    self.__tabela = Tabelas()
                    window['nomeTabela'].update(disabled=False)
                    nomeTabela = None
                    self.__tabelaInicial = None
                    nomeColuna = ''
                    pk = False
                    tipoCampo = 'Varchar'
                    tamanho = 255
                    null = False
                    increment = False
                    composto = False
                    multiValor = False
                    window['visualizacaoColuna'].update(values=[])
                    window['nomeTabela'].update(value='')
                    window['nomeCampo'].update(value='')
                    window['chavePrimaria'].update(value=False)
                    window['tipoCampo'].update(value='')
                    window['tamanhoCampo'].update(value='')
                    window['permitirNull'].update(value=False)
                    window['autoIncrement'].update(value=False)
                    window['multiValor'].update(value=False, disabled=False)
                    window['composto'].update(value=False, disabled=False)

            if window == janelaCriaColuna and event == 'Normalizacao':
                if not self.__tabela.getPK(nomeTabela=self.__tabelaInicial):
                    res = sg.PopupYesNo('Não foi encontrado nenhuma primary key, \nDeseja criar uma manualmente?', title='Chave primária')
                    if res == 'No':
                        self.__tabela.adicionaColuna(nomeTabela=self.__tabelaInicial,
                                                     nomeColuna=f'Id_{self.__tabelaInicial}', tipoDado='Int',
                                                     tamanho=0, nulo=False, autoIncrement=True, primaryKey=True,
                                                     foreignKey=False, references=' ', composto=False,
                                                     multiValor=False)
                        janelaNormalizacao = self.janelaNormalizacao()
                        window.hide()
                        janelaNormalizacao['escolheTabela'].update(value=self.__tabela.getNomeTabelas()[0],
                                                                   values=self.__tabela.getNomeTabelas())
                        tabela = self.__tabela.getTabela(nometabela=self.__tabelaInicial)
                        visualizacaotabela = ['Nome da Coluna | Tipo de Dado | Tamanho | Nulo? | Auto-Incremento? | '
                                              'PrimaryKey? | ForeignKey? | Referencia']
                        for col in tabela:
                            visualizacaotabela.append(f"{self.arrumaTamanho(col.getNomeColuna(), 14)} | "
                                                      f"{self.arrumaTamanho(col.getTipoDado(), 12)} | "
                                                      f"{self.arrumaTamanho(str(col.getTamanho()), 7)} | "
                                                      f"{self.arrumaTamanho(str(col.getNulo()), 5)} | "
                                                      f"{self.arrumaTamanho(str(col.getAutoIncrement()), 16)} | "
                                                      f"{self.arrumaTamanho(str(col.getPrimaryKey()), 11)} | "
                                                      f"{self.arrumaTamanho(str(col.getForeignKey()), 11)} | "
                                                      f"{self.arrumaTamanho(col.getReferences(), 10)}")
                        janelaNormalizacao['visualizacaoNormalizacao'].update(values=visualizacaotabela)
                else:
                    janelaNormalizacao = self.janelaNormalizacao()
                    window.hide()
                    janelaNormalizacao['escolheTabela'].update(value=self.__tabela.getNomeTabelas()[0],
                                                               values=self.__tabela.getNomeTabelas())
                    tabela = self.__tabela.getTabela(nometabela=self.__tabelaInicial)
                    visualizacaotabela = ['Nome da Coluna | Tipo de Dado | Tamanho | Nulo? | Auto-Incremento? | '
                                          'PrimaryKey? | ForeignKey? | Referencia']
                    for col in tabela:
                        visualizacaotabela.append(f"{self.arrumaTamanho(col.getNomeColuna(), 14)} | "
                                                  f"{self.arrumaTamanho(col.getTipoDado(), 12)} | "
                                                  f"{self.arrumaTamanho(str(col.getTamanho()), 7)} | "
                                                  f"{self.arrumaTamanho(str(col.getNulo()), 5)} | "
                                                  f"{self.arrumaTamanho(str(col.getAutoIncrement()), 16)} | "
                                                  f"{self.arrumaTamanho(str(col.getPrimaryKey()), 11)} | "
                                                  f"{self.arrumaTamanho(str(col.getForeignKey()), 11)} | "
                                                  f"{self.arrumaTamanho(col.getReferences(), 10)}")
                    janelaNormalizacao['visualizacaoNormalizacao'].update(values=visualizacaotabela)

            if window == janelaCriaColuna and event == 'nomeTabela':
                nomeTabela = values[event]
                self.__tabelaInicial = values[event]

            if window == janelaCriaColuna and event == 'nomeCampo':
                nomeColuna = values[event]

            if window == janelaCriaColuna and event == 'chavePrimaria':
                pk = values[event]
                if pk:
                    window['multiValor'].update(disabled=True)
                else:
                    window['multiValor'].update(disabled=False)

            if window == janelaCriaColuna and event == 'tipoCampo':
                tipoCampo = values[event]

            if window == janelaCriaColuna and event == 'tamanhoCampo':
                tamanho = values[event]

            if window == janelaCriaColuna and event == 'permitirNull':
                null = values[event]

            if window == janelaCriaColuna and event == 'autoIncrement':
                increment = values[event]

            if window == janelaCriaColuna and event == 'multiValor':
                multiValor = values[event]
                if multiValor:
                    window['composto'].update(disabled=True)
                    window['chavePrimaria'].update(disabled=True)
                else:
                    window['composto'].update(disabled=False)
                    window['chavePrimaria'].update(disabled=False)

            if window == janelaCriaColuna and event == 'composto':
                composto = values[event]
                if composto:
                    window['multiValor'].update(disabled=True)
                else:
                    window['multiValor'].update(disabled=False)

            if window == janelaCriaColuna and event == 'Adicionar':

                if not self.__tabela.getNomeTabelas():
                    self.__tabela.criaTabela(nomeTabela=self.__tabelaInicial)
                    window['nomeTabela'].update(disabled=True)

                if not self.__tabela.getNomeColunas(nomeTabela=self.__tabelaInicial):
                    self.__tabela.adicionaColuna(nomeTabela=self.__tabelaInicial, nomeColuna=nomeColuna, tipoDado=tipoCampo,
                                                 tamanho=tamanho, nulo=null, autoIncrement=increment, primaryKey=pk,
                                                 foreignKey=False, references=' ', composto=composto,
                                                 multiValor=multiValor)
                else:
                    colunas = self.__tabela.getNomeColunas(nomeTabela=self.__tabelaInicial)
                    existe = False
                    for coluna in colunas:
                        if nomeColuna == coluna:
                            existe = True
                    if existe:
                        self.__tabela.excluiColuna(nometabela=self.__tabelaInicial, nomecoluna=nomeColuna)
                        self.__tabela.adicionaColuna(nomeTabela=nomeTabela, nomeColuna=nomeColuna, tipoDado=tipoCampo,
                                                     tamanho=tamanho, nulo=null, autoIncrement=increment, primaryKey=pk,
                                                     foreignKey=False, references=' ', composto=composto,
                                                     multiValor=multiValor)
                    else:
                        self.__tabela.adicionaColuna(nomeTabela=self.__tabelaInicial, nomeColuna=nomeColuna, tipoDado=tipoCampo,
                                                     tamanho=tamanho, nulo=null, autoIncrement=increment, primaryKey=pk,
                                                     foreignKey=False, references=' ', composto=composto,
                                                     multiValor=multiValor)
                visualizacaotabela = ['Nome da Coluna | Tipo de Dado | Tamanho | Nulo? | Auto-Incremento? | '
                                      'PrimaryKey? | ForeignKey? | Referencia']
                for col in self.__tabela.getTabela(self.__tabelaInicial):
                    visualizacaotabela.append(f"{self.arrumaTamanho(col.getNomeColuna(), 14)} | "
                                              f"{self.arrumaTamanho(col.getTipoDado(), 12)} | "
                                              f"{self.arrumaTamanho(str(col.getTamanho()), 7)} | "
                                              f"{self.arrumaTamanho(str(col.getNulo()), 5)} | "
                                              f"{self.arrumaTamanho(str(col.getAutoIncrement()), 16)} | "
                                              f"{self.arrumaTamanho(str(col.getPrimaryKey()), 11)} | "
                                              f"{self.arrumaTamanho(str(col.getForeignKey()), 11)} | "
                                              f"{self.arrumaTamanho(col.getReferences(), 10)}")
                window['visualizacaoColuna'].update(values=visualizacaotabela)

                nomeColuna = ''
                pk = False
                tipoCampo = 'Varchar'
                tamanho = 255
                null = False
                increment = False
                composto = False
                multiValor = False
                window['nomeCampo'].update(value='')
                window['chavePrimaria'].update(value=False)
                window['tipoCampo'].update(value='')
                window['tamanhoCampo'].update(value='')
                window['permitirNull'].update(value=False)
                window['autoIncrement'].update(value=False)
                window['multiValor'].update(value=False, disabled=False)
                window['composto'].update(value=False, disabled=False)

            if window == janelaCriaColuna and event == 'Excluir':
                try:
                    atual = window['visualizacaoColuna'].Widget.curselection()
                    nomes = self.__tabela.getNomeColunas(nomeTabela=self.__tabelaInicial)
                    self.__tabela.excluiColuna(nometabela=self.__tabelaInicial, nomecoluna=nomes[atual[0] - 1])
                    visualizacaotabela = ['Nome da Coluna | Tipo de Dado | Tamanho | Nulo? | Auto-Incremento? | '
                                          'PrimaryKey? | ForeignKey? | Referencia']
                    tabela = self.__tabela.getTabela(nometabela=self.__tabelaInicial)
                    for col in tabela:
                        visualizacaotabela.append(f"{self.arrumaTamanho(col.getNomeColuna(), 14)} | "
                                                  f"{self.arrumaTamanho(col.getTipoDado(), 12)} | "
                                                  f"{self.arrumaTamanho(str(col.getTamanho()), 7)} | "
                                                  f"{self.arrumaTamanho(str(col.getNulo()), 5)} | "
                                                  f"{self.arrumaTamanho(str(col.getAutoIncrement()), 16)} | "
                                                  f"{self.arrumaTamanho(str(col.getPrimaryKey()), 11)} | "
                                                  f"{self.arrumaTamanho(str(col.getForeignKey()), 11)} | "
                                                  f"{self.arrumaTamanho(col.getReferences(), 10)}")
                    window['visualizacaoColuna'].update(values=visualizacaotabela)
                except IndexError:
                    sg.PopupOK('Alerta', 'Selecione um atributo da tabela')

            if window == janelaCriaColuna and event == 'Editar':
                try:
                    atual = window['visualizacaoColuna'].Widget.curselection()
                    nomes = self.__tabela.getNomeColunas(nomeTabela=self.__tabelaInicial)
                    coluna = self.__tabela.getColuna(nomecoluna=nomes[atual[0] - 1])
                    window['nomeCampo'].update(value=coluna.getNomeColuna())
                    window['chavePrimaria'].update(value=coluna.getPrimaryKey())
                    window['tipoCampo'].update(value=coluna.getTipoDado())
                    window['tamanhoCampo'].update(value=coluna.getTamanho())
                    window['permitirNull'].update(value=coluna.getNulo())
                    window['autoIncrement'].update(value=coluna.getAutoIncrement())
                    window['multiValor'].update(value=coluna.getMultiValor())
                    window['composto'].update(value=coluna.getComposto())
                    nomeColuna = coluna.getNomeColuna()
                    pk = coluna.getPrimaryKey()
                    tipoCampo = coluna.getTipoDado()
                    tamanho = coluna.getTamanho()
                    null = coluna.getNulo()
                    increment = coluna.getAutoIncrement()
                    composto = coluna.getComposto()
                    multiValor = coluna.getMultiValor()
                except IndexError:
                    sg.PopupOK('Alerta', 'Selecione um atributo da tabela')


            if window == janelaNormalizacao and event == 'primeira':
                window['segunda'].update(disabled=False)
                window['primeira'].update(disabled=True)
                temcomposto = False
                for coluna in self.__tabela.getTabela(nometabela=self.__tabelaInicial):
                    if coluna.getComposto():
                        temcomposto = True

                if temcomposto:

                    window.hide()
                    ok = sg.PopupOK('Alerta', 'Foi encontrado pelo menos um atributo composto, para normalizar sua tabela '
                                              'será necessário decompor todos.')
                    if ok:
                        janelaChvComposta = self.janelaChvComposta()
                        tabela = self.__tabela.getTabela(nometabela=self.__tabelaInicial)
                        visualizacaotabela = ['Nome da Coluna | Tipo de Dado | Tamanho | Nulo? | Auto-Incremento? | '
                                              'PrimaryKey? | ForeignKey? | Referencia']
                        for col in tabela:
                            visualizacaotabela.append(f"{self.arrumaTamanho(col.getNomeColuna(), 14)} | "
                                                      f"{self.arrumaTamanho(col.getTipoDado(), 12)} | "
                                                      f"{self.arrumaTamanho(str(col.getTamanho()), 7)} | "
                                                      f"{self.arrumaTamanho(str(col.getNulo()), 5)} | "
                                                      f"{self.arrumaTamanho(str(col.getAutoIncrement()), 16)} | "
                                                      f"{self.arrumaTamanho(str(col.getPrimaryKey()), 11)} | "
                                                      f"{self.arrumaTamanho(str(col.getForeignKey()), 11)} | "
                                                      f"{self.arrumaTamanho(col.getReferences(), 10)}")
                        janelaChvComposta['visualizacaoChvComposta'].update(values=visualizacaotabela)
                else:

                    sg.PopupOK('Alerta', 'Nenhum atributo composto encontrado.')
                    temmulti = False
                    for coluna in self.__tabela.getTabela(nometabela=self.__tabelaInicial):
                        if coluna.getMultiValor():
                            temmulti = True

                    if temmulti:
                        ok = sg.PopupOK('Alerta', 'Foi encontrado pelo menos um atributo multivalorado, para normalizar '
                                                  'sua tabela será feita a separação de forma automática')

                        if ok:
                            atributosMulti = self.__tabela.getMultiValor()
                            print(atributosMulti)
                            for atributo in atributosMulti:
                                self.__tabela.criaTabela(nomeTabela=atributo)
                                tabela = self.__tabela.getTabela(nometabela=self.__tabelaInicial)
                                self.__tabela.adicionaColuna(nomeTabela=atributo, nomeColuna='ID_' + atributo, tipoDado='Int',
                                                             tamanho=0, nulo=False, autoIncrement=True, primaryKey=True,
                                                             foreignKey=False, references=' ', composto=False, multiValor=False)
                                for col in tabela:
                                    if col.getPrimaryKey():
                                        self.__tabela.adicionaColuna(nomeTabela=atributo, nomeColuna=col.getNomeColuna(),
                                                                     tipoDado=col.getTipoDado(), tamanho=col.getTamanho(),
                                                                     nulo=col.getNulo(), autoIncrement=col.getAutoIncrement(),
                                                                     primaryKey=col.getPrimaryKey(), foreignKey=True,
                                                                     references=self.__tabelaInicial, composto=False, multiValor=False)
                                    if col.getNomeColuna() == atributo:
                                        self.__tabela.adicionaColuna(nomeTabela=atributo, nomeColuna=col.getNomeColuna(),
                                                                     tipoDado=col.getTipoDado(), tamanho=col.getTamanho(),
                                                                     nulo=col.getNulo(), autoIncrement=col.getAutoIncrement(),
                                                                     primaryKey=col.getPrimaryKey(), foreignKey=False,
                                                                     references=col.getReferences(), composto=False,
                                                                     multiValor=False)

                                self.__tabela.excluiColuna(nometabela=self.__tabelaInicial, nomecoluna=atributo)

            if window == janelaNormalizacao and event == 'segunda':
                janelaNormalizacao.hide()
                janelaDependencias = self.janelaDependencias()
                window['Script'].update(disabled=False)
                window['segunda'].update(disabled=True)
                window['escolheTabela'].update(value=[])
                window['escolheTabela'].update(value=self.__tabela.getNomeTabelas()[0],
                                               values=self.__tabela.getNomeTabelas())

            if window == janelaNormalizacao and event == 'Script':
                self.__script = Script(tabelas=self.__tabela)
                self.__script.geraScript()
                sg.popup_ok('Script gerado com sucesso')
                window['Visualizar'].update(disabled=False)
                window['Script'].update(disabled=True)

            if window == janelaNormalizacao and event == 'Visualizar':
                janelaVisualizaScript = self.janelaVisualizaScript()
                janelaVisualizaScript['visualizacaoscript'].update('')
                for script in self.__script.getScript():
                    janelaVisualizaScript['visualizacaoscript'].print(script)
                window.hide()

            if window == janelaNormalizacao and event == 'escolheTabela':
                nomeTabela = values[event]
                window['escolheTabela'].update(value=values[event], values=self.__tabela.getNomeTabelas())
                tabela = self.__tabela.getTabela(nometabela=nomeTabela)
                visualizacaotabela = ['Nome da Coluna | Tipo de Dado | Tamanho | Nulo? | Auto-Incremento? | '
                                      'PrimaryKey? | ForeignKey? | Referencia']
                for col in tabela:
                    visualizacaotabela.append(f"{self.arrumaTamanho(col.getNomeColuna(), 14)} | "
                                              f"{self.arrumaTamanho(col.getTipoDado(), 12)} | "
                                              f"{self.arrumaTamanho(str(col.getTamanho()), 7)} | "
                                              f"{self.arrumaTamanho(str(col.getNulo()), 5)} | "
                                              f"{self.arrumaTamanho(str(col.getAutoIncrement()), 16)} | "
                                              f"{self.arrumaTamanho(str(col.getPrimaryKey()), 11)} | "
                                              f"{self.arrumaTamanho(str(col.getForeignKey()), 11)} | "
                                              f"{self.arrumaTamanho(col.getReferences(), 10)}")
                window['visualizacaoNormalizacao'].update(values=visualizacaotabela)

            if window == janelaChvComposta and event == 'nomeAtributo':
                nomeColuna = values[event]

            if window == janelaChvComposta and event == 'chavePrimaria':
                pk = values[event]

            if window == janelaChvComposta and event == 'tipoCampo':
                tipoCampo = values[event]

            if window == janelaChvComposta and event == 'tamanhoCampo':
                tamanho = values[event]

            if window == janelaChvComposta and event == 'permitirNull':
                null = values[event]

            if window == janelaChvComposta and event == 'autoIncrement':
                increment = values[event]

            if window == janelaChvComposta and event == 'Adicionar':
                colunas = self.__tabela.getNomeColunas(nomeTabela=self.__tabelaInicial)
                existe = False
                for coluna in colunas:
                    if nomeColuna == coluna:
                        existe = True
                if existe:
                    self.__tabela.excluiColuna(nometabela=self.__tabelaInicial, nomecoluna=nomeColuna)
                    self.__tabela.adicionaColuna(nomeTabela=self.__tabelaInicial, nomeColuna=nomeColuna, tipoDado=tipoCampo,
                                                 tamanho=tamanho, nulo=null, autoIncrement=increment, primaryKey=pk,
                                                 foreignKey=False, references=' ', composto=False, multiValor=False)
                else:
                    self.__tabela.adicionaColuna(nomeTabela=self.__tabelaInicial, nomeColuna=nomeColuna, tipoDado=tipoCampo,
                                                 tamanho=tamanho, nulo=null, autoIncrement=increment, primaryKey=pk,
                                                 foreignKey=False, references=' ', composto=False, multiValor=False)
                tabela = self.__tabela.getTabela(nometabela=self.__tabelaInicial)
                visualizacaotabela = ['Nome da Coluna | Tipo de Dado | Tamanho | Nulo? | Auto-Incremento? | '
                                      'PrimaryKey? | ForeignKey? | Referencia']
                for col in tabela:
                    visualizacaotabela.append(f"{self.arrumaTamanho(col.getNomeColuna(), 14)} | "
                                              f"{self.arrumaTamanho(col.getTipoDado(), 12)} | "
                                              f"{self.arrumaTamanho(str(col.getTamanho()), 7)} | "
                                              f"{self.arrumaTamanho(str(col.getNulo()), 5)} | "
                                              f"{self.arrumaTamanho(str(col.getAutoIncrement()), 16)} | "
                                              f"{self.arrumaTamanho(str(col.getPrimaryKey()), 11)} | "
                                              f"{self.arrumaTamanho(str(col.getForeignKey()), 11)} | "
                                              f"{self.arrumaTamanho(col.getReferences(), 10)}")
                window['visualizacaoChvComposta'].update(values=visualizacaotabela)

                nomeColuna = ''
                pk = False
                tipoCampo = 'Varchar'
                tamanho = 255
                null = False
                increment = False
                window['nomeAtributo'].update(value='')
                window['chavePrimaria'].update(value=False)
                window['tipoCampo'].update(value='')
                window['tamanhoCampo'].update(value='')
                window['permitirNull'].update(value=False)
                window['autoIncrement'].update(value=False)


            if window == janelaChvComposta and event == 'Finalizar':
                janelaNormalizacao.un_hide()
                for coluna in self.__tabela.getCompostos():
                    self.__tabela.excluiColuna(nometabela=self.__tabelaInicial, nomecoluna=self.__tabela.getColuna(nomecoluna=coluna).getNomeColuna())

                temmulti = False
                for coluna in self.__tabela.getTabela(nometabela=self.__tabelaInicial):
                    if coluna.getMultiValor():
                        temmulti = True

                if temmulti:
                    ok = sg.PopupOK('Alerta', 'Foi encontrado pelo menos um atributo multivalorado, para normalizar '
                                              'sua tabela será feita a separação de forma automática')
                    if ok:
                        for atributo in self.__tabela.getMultiValor():
                            self.__tabela.criaTabela(nomeTabela=atributo)
                            self.__tabela.adicionaColuna(nomeTabela=atributo, nomeColuna='ID_' + atributo, tipoDado='Int',
                                                         tamanho=0, nulo=False, autoIncrement=True, primaryKey=True,
                                                         foreignKey=False, references=' ', composto=False, multiValor=False)
                            for col in self.__tabela.getTabela(nometabela=self.__tabelaInicial):
                                if col.getPrimaryKey():
                                    self.__tabela.adicionaColuna(nomeTabela=atributo, nomeColuna=col.getNomeColuna(),
                                                                 tipoDado=col.getTipoDado(), tamanho=col.getTamanho(),
                                                                 nulo=col.getNulo(), autoIncrement=col.getAutoIncrement(),
                                                                 primaryKey=col.getPrimaryKey(), foreignKey=True,
                                                                 references=self.__tabelaInicial, composto=False, multiValor=False)
                                if col.getNomeColuna() == atributo:
                                    self.__tabela.adicionaColuna(nomeTabela=atributo, nomeColuna=col.getNomeColuna(),
                                                                 tipoDado=col.getTipoDado(), tamanho=col.getTamanho(),
                                                                 nulo=col.getNulo(), autoIncrement=col.getAutoIncrement(),
                                                                 primaryKey=col.getPrimaryKey(), foreignKey=False,
                                                                 references=col.getReferences(), composto=False, multiValor=False)

                            self.__tabela.excluiColuna(nometabela=self.__tabelaInicial, nomecoluna=atributo)
                window.close()

            if window == janelaChvComposta and event == 'Excluir':
                atual = window['visualizacaoColuna'].Widget.curselection()
                nomes = self.__tabela.getNomeColunas(nomeTabela=self.__tabelaInicial)
                self.__tabela.excluiColuna(nometabela=self.__tabelaInicial, nomecoluna=nomes[atual[0] - 1])
                visualizacaotabela = ['Nome da Coluna | Tipo de Dado | Tamanho | Nulo? | Auto-Incremento? | '
                                      'PrimaryKey? | ForeignKey? | Referencia']
                tabela = self.__tabela.getTabela(self.__tabelaInicial)
                for col in tabela:
                    visualizacaotabela.append(f"{self.arrumaTamanho(col.getNomeColuna(), 14)} | "
                                              f"{self.arrumaTamanho(col.getTipoDado(), 12)} | "
                                              f"{self.arrumaTamanho(str(col.getTamanho()), 7)} | "
                                              f"{self.arrumaTamanho(str(col.getNulo()), 5)} | "
                                              f"{self.arrumaTamanho(str(col.getAutoIncrement()), 16)} | "
                                              f"{self.arrumaTamanho(str(col.getPrimaryKey()), 11)} | "
                                              f"{self.arrumaTamanho(str(col.getForeignKey()), 11)} | "
                                              f"{self.arrumaTamanho(col.getReferences(), 10)}")
                window['visualizacaoChvComposta'].update(values=visualizacaotabela)

            if window == janelaChvComposta and event == 'Editar':
                atual = window['visualizacaoColuna'].Widget.curselection()
                nomes = self.__tabela.getNomeColunas(nomeTabela=self.__tabelaInicial)
                coluna = self.__tabela.getColuna(nomecoluna=nomes[atual[0] - 1])
                window['nomeAtributo'].update(value=coluna.getNomeColuna())
                window['chavePrimaria'].update(value=coluna.getPrimaryKey())
                window['tipoCampo'].update(value=coluna.getTipoDado())
                window['tamanhoCampo'].update(value=coluna.getTamanho())
                window['permitirNull'].update(value=coluna.getNulo())
                window['autoIncrement'].update(value=coluna.getAutoIncrement())
                nomeColuna = coluna.getNomeColuna()
                pk = coluna.getPrimaryKey()
                tipoCampo = coluna.getTipoDado()
                tamanho = coluna.getTamanho()
                null = coluna.getNulo()
                increment = coluna.getAutoIncrement()

            if window == janelaDependencias and event == 'determinantes':
                determinantes = values[event]

            if window == janelaDependencias and event == 'dependentes':
                dependentes = values[event]

            if window == janelaDependencias and event == 'Adicionar':

                criado = False
                if not self.__dependencias.getDependencias():
                    self.__dependencias.criaDependencia(esquerda=determinantes, direita=dependentes)
                else:
                    for dependencie in self.__dependencias.getDependencias():
                        esq = dependencie.getEsquerda()
                        if determinantes == esq:
                            drt = dependencie.getDireita()
                            novaDireita = list(OrderedDict.fromkeys(drt + dependentes))
                            dependencie.setDireita(novaDireita=novaDireita)
                            criado = True

                    if not criado:
                        self.__dependencias.criaDependencia(esquerda=determinantes, direita=dependentes)

                deps = self.__dependencias.getDependencias()
                visualizacaotabela = []
                for dep in deps:
                    stri = ''
                    for esq in dep.getEsquerda():
                        stri = stri + esq + ','
                    stri = stri[0:len(stri) - 1] + ' --> '
                    for drt in dep.getDireita():
                        stri = stri + drt + ','
                    visualizacaotabela.append(stri[0:len(stri) - 1])
                window['visualizacaoDependencias'].update(values=visualizacaotabela)

            if window == janelaDependencias and event == 'Normalizar':
                self.__dependencias.Normalizar()
                deps = self.__dependencias.getDependencias()
                visualizacaotabela = []
                for dep in deps:
                    stri = ''
                    for esq in dep.getEsquerda():
                        stri = stri + esq + ','
                    stri = stri[0:len(stri) - 1] + ' --> '
                    for drt in dep.getDireita():
                        stri = stri + drt + ','
                    visualizacaotabela.append(stri[0:len(stri) - 1])
                window['visualizacaoDependencias'].update(values=visualizacaotabela)

            if window == janelaDependencias and event == 'Excluir':
                self.__dependencias.excluiDependencia(window['visualizacaoDependencias'].Widget.curselection()[0])
                deps = self.__dependencias.getDependencias()
                visualizacaotabela = []
                for dep in deps:
                    stri = ''
                    for esq in dep.getEsquerda():
                        stri = stri + esq + ','
                    stri = stri[0:len(stri) - 1] + ' --> '
                    for drt in dep.getDireita():
                        stri = stri + drt + ','
                    visualizacaotabela.append(stri[0:len(stri) - 1])
                window['visualizacaoDependencias'].update(values=visualizacaotabela)

            if window == janelaDependencias and event == 'Continuar':

                ok = False
                for coluna in self.__tabela.getNomeColunas(nomeTabela=self.__tabelaInicial):
                    if not ok:
                        existe = False
                        for dep in self.__dependencias.getDependencias():
                            for esq in dep.getEsquerda():
                                if esq == coluna:
                                    existe = True
                            for drt in dep.getDireita():
                                if drt == coluna:
                                    existe = True
                        if not existe:
                            ok = sg.PopupOK('Alerta', 'Ainda existem atributos fora de dependencia, \nPor favor '
                                                      'adicione todos atributos em pelo menos uma dependencia')

                if not ok:
                    window.close()
                    self.__dependencias.checkRepete()
                    self.__tabela = self.__dependencias.getTabela()
                    janelaAlteraNome = self.janelaAlteraNome()
                    janelaAlteraNome['escolheTabela'].update(value=self.__tabela.getNomeTabelas()[0],
                                                             values=self.__tabela.getNomeTabelas())
                    tabela = self.__tabela.getTabela(nometabela=self.__tabela.getNomeTabelas()[0])
                    visualizacaotabela = ['Nome da Coluna | Tipo de Dado | Tamanho | Nulo? | Auto-Incremento? | '
                                          'PrimaryKey? | ForeignKey? | Referencia']
                    for col in tabela:
                        visualizacaotabela.append(f"{self.arrumaTamanho(col.getNomeColuna(), 14)} | "
                                                  f"{self.arrumaTamanho(col.getTipoDado(), 12)} | "
                                                  f"{self.arrumaTamanho(str(col.getTamanho()), 7)} | "
                                                  f"{self.arrumaTamanho(str(col.getNulo()), 5)} | "
                                                  f"{self.arrumaTamanho(str(col.getAutoIncrement()), 16)} | "
                                                  f"{self.arrumaTamanho(str(col.getPrimaryKey()), 11)} | "
                                                  f"{self.arrumaTamanho(str(col.getForeignKey()), 11)} | "
                                                  f"{self.arrumaTamanho(col.getReferences(), 10)}")
                    janelaAlteraNome['visualizacaoRelacoes'].update(values=visualizacaotabela)
                    sg.PopupOK('Foi encontrado mais de uma dependencia,\n A tabela atual será dividida em outras')

            if window == janelaAlteraNome and event == 'escolheTabela':
                nomeTabela = values[event]
                window['escolheTabela'].update(value=values[event],
                                               values=self.__tabela.getNomeTabelas())
                tabela = self.__tabela.getTabela(nometabela=nomeTabela)
                visualizacaotabela = ['Nome da Coluna | Tipo de Dado | Tamanho | Nulo? | Auto-Incremento? | '
                                      'PrimaryKey? | ForeignKey? | Referencia']
                for col in tabela:
                    visualizacaotabela.append(f"{self.arrumaTamanho(col.getNomeColuna(), 14)} | "
                                              f"{self.arrumaTamanho(col.getTipoDado(), 12)} | "
                                              f"{self.arrumaTamanho(str(col.getTamanho()), 7)} | "
                                              f"{self.arrumaTamanho(str(col.getNulo()), 5)} | "
                                              f"{self.arrumaTamanho(str(col.getAutoIncrement()), 16)} | "
                                              f"{self.arrumaTamanho(str(col.getPrimaryKey()), 11)} | "
                                              f"{self.arrumaTamanho(str(col.getForeignKey()), 11)} | "
                                              f"{self.arrumaTamanho(col.getReferences(), 10)}")
                janelaAlteraNome['visualizacaoRelacoes'].update(values=visualizacaotabela)

            if window == janelaAlteraNome and event == 'NomeTabela':
                nomeNovaTabela = values[event]

            if window == janelaAlteraNome and event == 'Alterar':
                for tabela in self.__tabela.getTabelas():
                    for coluna in tabela.getTabela():
                        if coluna.getReferences() == nomeTabela:
                            coluna.setReferences(novoReferences=nomeNovaTabela)
                self.__tabela.setNomeTabela(nometabela=nomeTabela, novonometabela=nomeNovaTabela)
                tabela = self.__tabela.getTabela(nometabela=nomeNovaTabela)
                visualizacaotabela = ['Nome da Coluna | Tipo de Dado | Tamanho | Nulo? | Auto-Incremento? | '
                                      'PrimaryKey? | ForeignKey? | Referencia']
                for col in tabela:
                    visualizacaotabela.append(f"{self.arrumaTamanho(col.getNomeColuna(), 14)} | "
                                              f"{self.arrumaTamanho(col.getTipoDado(), 12)} | "
                                              f"{self.arrumaTamanho(str(col.getTamanho()), 7)} | "
                                              f"{self.arrumaTamanho(str(col.getNulo()), 5)} | "
                                              f"{self.arrumaTamanho(str(col.getAutoIncrement()), 16)} | "
                                              f"{self.arrumaTamanho(str(col.getPrimaryKey()), 11)} | "
                                              f"{self.arrumaTamanho(str(col.getForeignKey()), 11)} | "
                                              f"{self.arrumaTamanho(col.getReferences(), 10)}")
                janelaAlteraNome['visualizacaoRelacoes'].update(values=visualizacaotabela)
                window['escolheTabela'].update(value=nomeNovaTabela,
                                               values=self.__tabela.getNomeTabelas())

            if window == janelaAlteraNome and event == 'Continuar':
                janelaNormalizacao['escolheTabela'].update(value=self.__tabela.getNomeTabelas()[0], values=self.__tabela.getNomeTabelas())
                tabela = self.__tabela.getTabela(nometabela=self.__tabela.getNomeTabelas()[0])
                visualizacaotabela = ['Nome da Coluna | Tipo de Dado | Tamanho | Nulo? | Auto-Incremento? | '
                                      'PrimaryKey? | ForeignKey? | Referencia']
                for col in tabela:
                    visualizacaotabela.append(f"{self.arrumaTamanho(col.getNomeColuna(), 14)} | "
                                              f"{self.arrumaTamanho(col.getTipoDado(), 12)} | "
                                              f"{self.arrumaTamanho(str(col.getTamanho()), 7)} | "
                                              f"{self.arrumaTamanho(str(col.getNulo()), 5)} | "
                                              f"{self.arrumaTamanho(str(col.getAutoIncrement()), 16)} | "
                                              f"{self.arrumaTamanho(str(col.getPrimaryKey()), 11)} | "
                                              f"{self.arrumaTamanho(str(col.getForeignKey()), 11)} | "
                                              f"{self.arrumaTamanho(col.getReferences(), 10)}")
                janelaNormalizacao['visualizacaoNormalizacao'].update(values=visualizacaotabela)
                window.close()
                janelaNormalizacao.un_hide()

            if window == janelaConexao and event == 'local':
                local = values[event]
                if local:
                    window['ip'].update(disabled=True)
                    ip = 'localhost'
                else:
                    window['ip'].update(disabled=False)

            if window == janelaConexao and event == 'nome':
                nome = values[event]

            if window == janelaConexao and event == 'ip':
                ip = values[event]

            if window == janelaConexao and event == 'pass':
                password = values[event]

            if window == janelaConexao and event == 'user':
                user = values[event]

            if window == janelaConexao and event == 'Conectar':
                self.__script.criadb(ip=ip, user=user, password=password, nome=nome)
                self.__script.criatabelas()
                sg.popup_ok('Banco de dados criado com sucesso')

            if window == janelaConexao and event == 'Fechar':
                window.close()
                janelaVisualizaScript.un_hide()

            if window == janelaVisualizaScript and event == 'Conectar':
                janelaConexao = self.janelaConexao()
                window.hide()

            if window == janelaVisualizaScript and event == 'Voltar':
                window.close()
                janelaNormalizacao.un_hide()

            if window == janelaVisualizaScript and event == 'Salvar':
                f = open('script.txt', 'w')
                for script in self.__script.getScript():
                    f.write(script)
                f.close()

            if window == janelaChvComposta and event == sg.WIN_CLOSED:
                window.close()
                break

            if window == janelaDependencias and event == sg.WIN_CLOSED:
                window.close()
                break

            if window == janelaCriaColuna and event == sg.WIN_CLOSED:
                window.close()
                break

            if window == janelaNormalizacao and event == sg.WIN_CLOSED:
                window.close()
                break

            if window == janelaAlteraNome and event == sg.WIN_CLOSED:
                window.close()
                break

            if window == janelaConexao and event == sg.WIN_CLOSED:
                window.close()
                janelaVisualizaScript.un_hide()

            if window == janelaVisualizaScript and event == sg.WIN_CLOSED:
                window.close()
                janelaNormalizacao.un_hide()


tela = Telas()
tela.manter()
