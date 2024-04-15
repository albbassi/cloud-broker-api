from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Cliente

class ClienteSchema(BaseModel):
    
    """ 
        Formato dos dados recebidos pela API para inserção de um cliente na base.
    """

    nome: str ="Pontifícia Universidade Católica do Rio de Janeiro"
    cnpj: str ="33555921000170"
    localizacao: str ="Rua Marquês de São Vicente, 225 – Gávea CEP: 22451-900 RJ"


class ClienteViewSchema(BaseModel):
    
    """ 
        Formato do dado retornado pela API com as informações relativas a um cliente cadsatrado na base.
    """
    
    nome: str ="Pontifícia Universidade Católica do Rio de Janeiro"
    cnpj: str ="33555921000170"
    localizacao: str ="Rua Marquês de São Vicente, 225 – Gávea CEP: 22451-900 RJ"


def ClientesApresentacao(clientes: List[Cliente]):

    """ 
        Formato dos dados retornados pela API com todos os registros existentes na tabela cli_cliente. Segue o schema definido em
        ClienteViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
        "nome":cliente.nome,
        "cnpj":cliente.cnpj,
        "localizacao":cliente.localizacao
        })

    return {"clientes": result}

def ClienteApresenta(cliente:Cliente):
    
    """ 
        Formato do dado retornado pela API de um registro da tabela cli_cliente. Segue o schema definido em
        ClienteViewSchema.
    """
    return {
        "nome":cliente.nome,
        "cnpj": cliente.cnpj,
        "localizacao": cliente.localizacao
    }

class ClienteBuscaSchema(BaseModel):
    """ 
        Formato do dado recebido pela API para busca na base através do campo CNPJ.
    """
    cnpj: str = "33555921000170"


class ClientesListagemSchema(BaseModel):
    
    """ 
        Formato do dado retornado pela API com todos os clientes da base.
    """
    clientes:List[ClienteSchema]