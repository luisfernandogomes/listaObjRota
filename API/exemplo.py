import requests
def exemplo():
    cep = '16702177'
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)


    if response.status_code == 200:
        dados = response.json()
        print(f"Logradouro: {dados['logradouro']}")
        print(f'bairro: {dados["bairro"]}')
        print(f'localidade: {dados["localidade"]}')
        print(f'uf: {dados["uf"]}')
        print(f'ibge: {dados["ibge"]}')
        print(f'gia: {dados["gia"]}')
        print(f'cep: {dados["cep"]}')
        print(f'complemento: {dados["complemento"]}')
        print(f'ddd: {dados["ddd"]}')
        print(f'siafi: {dados["siafi"]}')
        print(f'Regiao: {dados["regiao"]}')
        print(f'Unidade: {dados["unidade"]}')
        print(f'Estado: {dados["estado"]}')

    else:
        print('Erro ao acessar o servidor')

def exemplo_get(id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        dados_post = response.json()
        # for chave, valor in dados_post.items():
        #     print(f'{chave}: {valor}')
        print(f"titulo: {dados_post['title']}")
        print(f"body: {dados_post['body']}")
        # for post in dados_post:
        #     print(f"{post['title']}\n")

# exemplo_get(1)
def exemplo_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    novaPostagem = {
        "title": "novo titulo",
        "body": "novo conteudo",
        "userId": 1
    }
    response = requests.post(url, json=novaPostagem)
    if response.status_code == 201:
        dados_post = response.json()
        print("Postagem criada com sucesso")
        print(f"id: {dados_post['id']}")
        print(f"titulo: {dados_post['title']}")
        print(f"body: {dados_post['body']}")
    else:
        print("Erro ao criar a postagem")
# exemplo_post()
def exemplo_put(id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"

    novaPostagem = {
        "id": id,
        "title": "novo titulo",
        "body": "novo conteudo",
        "userId": 1
    }
    antes = requests.get(url)
    response = requests.put(url, json=novaPostagem)
    if response.status_code == 200:
        if antes.status_code == 200:
            dados_antes = antes.json()
            print(f"id: {dados_antes['id']}")
            print(f"titulo: {dados_antes['title']}")
            print(f"body: {dados_antes['body']}")
        dadospost = response.json()
        print(dadospost['title'])
        print(dadospost['body'])
        print("Postagem atualizada com sucesso")
    else:
        print(f"Erro ao atualizar a postagem{response.status_code}")
exemplo_put(1)
