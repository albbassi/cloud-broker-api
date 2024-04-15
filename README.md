# API Gestão de Contratos - Multinuvem

Esta aplicação é o ponta pé inicial de um projeto para criação de uma sistema de gestão de contrato de multinuvem (broker). O sistema será dividido em módulos que farão a gestão de: Clientes, Contratos, Itens de contrato, Faturamento, Demandas, Usuários, Gestores e Billing. A implementação em forma de API, visa facilitar a integração com as ferramentas corporativas já em produção e ferrramentas de parceiros.  


# Atenção

Como o projeto está na fase de MVP, foi utlizada uma base Sqlite3 e esta precisa ser configurada para permitir "delete cascade" (1).além disso, foi criado um trigger para automatizar o cálculo do valor total dos produtos (2)

1. No arquivo **models/__init__.py** foi criado um evento para habilitar o suporte nativo à foreignKey permitindo assim a execução de deletes cascade nas tabelas.

    @event.listens_for(engine, "connect") \
        def set_sqlite_pragma(dbapi_connection, connection_record):\
            cursor = dbapi_connection.cursor()\
            cursor.execute("PRAGMA foreign_keys=ON")\
            cursor.close()\

        
2. Criação de um trigger para que na tabela item de contrato o valor total fosse calculado a partir dos dados inserido nas colunas valor unitário e quantidade preenchendo automaticamente a coluna valor total.

    Criação do trigger\
    def calcular_produto(mapper, connection, target):\
        target.valor_total = target.quantidade * target.valor_unitario\

    Adicionar o trigger ao evento before_insert\
        event.listen(ItemContrato, 'before_insert', calcular_produto)\

#### Documentação SQLITE: [https://www.sqlite.org/lang_createtrigger.html]


---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.

Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando os parâmetro reload e debug, que reiniciará o servidor e ajudará com o debug
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload --debug
```


Abra o [http://localhost:5000/](http://localhost:5000/) no navegador para escolher o mode de apresentação da Dcumentação da API em execução.

