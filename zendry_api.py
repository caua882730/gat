import requests

class ZendryAPI:
    BASE_URL = "https://api.zendry.com"
    API_KEY = "sua-chave-aqui"

    @staticmethod
    def criar_pedido(dados_pedido):
        url = f"{ZendryAPI.BASE_URL}/checkout/create"
        headers = {"Authorization": f"Bearer {ZendryAPI.API_KEY}", "Content-Type": "application/json"}
        response = requests.post(url, json=dados_pedido, headers=headers)
        return response.json()

    @staticmethod
    def processar_pagamento(pedido_id, dados_pagamento):
        url = f"{ZendryAPI.BASE_URL}/checkout/{pedido_id}/process"
        headers = {"Authorization": f"Bearer {ZendryAPI.API_KEY}", "Content-Type": "application/json"}
        response = requests.post(url, json=dados_pagamento, headers=headers)
        return response.json()

    @staticmethod
    def confirmar_pagamento(pedido_id):
        url = f"{ZendryAPI.BASE_URL}/checkout/{pedido_id}/confirm"
        headers = {"Authorization": f"Bearer {ZendryAPI.API_KEY}", "Content-Type": "application/json"}
        response = requests.get(url, headers=headers)
        return response.json()

# Exemplo de uso
if __name__ == "__main__":
    pedido = {"valor": 100.00, "moeda": "BRL", "descricao": "Compra online"}
    resposta_pedido = ZendryAPI.criar_pedido(pedido)
    pedido_id = resposta_pedido.get("id")
    
    pagamento = {"metodo": "cartao", "numero": "4111111111111111", "cvv": "123", "validade": "12/25"}
    resposta_pagamento = ZendryAPI.processar_pagamento(pedido_id, pagamento)
    
    confirmacao = ZendryAPI.confirmar_pagamento(pedido_id)
    print(confirmacao)
