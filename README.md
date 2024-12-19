# ETLProjectAPI

## Descrição
Este projeto é uma aplicação de ETL (Extract, Transform, Load) que utiliza a biblioteca `requests` do Python para extrair dados de uma API, transformá-los conforme necessário e carregá-los em um banco de dados.

## Estrutura do Projeto
- `extract.py`: Contém funções para extrair dados da API.
- `transform.py`: Contém funções para transformar os dados extraídos.
- `load.py`: Contém funções para carregar os dados transformados em um banco de dados.
- `main.py`: Script principal que orquestra o processo de ETL.

## Requisitos
- Python 3.6+
- Bibliotecas Python: `requests`, `pandas`, `sqlalchemy`

## Instalação
1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/ETLProjectAPI.git
    cd ETLProjectAPI
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso
1. Configure as variáveis de ambiente necessárias no arquivo `.env`.

2. Execute o script principal:
    ```sh
    python main.py
    ```

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
