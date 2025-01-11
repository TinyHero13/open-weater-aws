# Open Weather Data Pipeline
Este projeto consiste em um script Python que extrai dados meteorológicos da API Open Weather, processa essas informações e armazena o resultado em um arquivo CSV dentro de um bucket Amazon S3. A orquestração de todo o processo é realizada com Apache Airflow.

## Arquitetura do projeto
![arquitetura do projeto](/imgs/architecture.png)

## Funcionalidades
- Conexão com a API Open Weather para obtenção de dados meteorológicos.
- Tratamento e transformação dos dados em um formato estruturado usando Pandas.
- Geração de um arquivo CSV com as informações tratadas.
- Criação do bucket no Amazon S3.
- upload do arquivo CSV para o bucket no Amazon S3.

## Tecnologias Utilizadas
- **Python**
- **Pandas**: Biblioteca para manipulação e transformação de dados.
- **Boto3**: Biblioteca para interação com a AWS, permitindo a criação do bucket e o upload do arquivo CSV para o Amazon S3.
- **Apache Airflow**: Framework de orquestração para a execução e agendamento de tarefas ETL.
- **Astro CLI**: Ferramenta para facilitar a execução e desenvolvimento do Airflow localmente.

## Como Rodar o Projeto

### 1. Instalação do Astro CLI

O **Astro CLI** é utilizado para facilitar a configuração e execução do Apache Airflow localmente. Para instalá-lo, execute o seguinte comando:

```bash
pip install astro-cli
```

### 2. Inicializando o Airflow
Após a instalação do Astro CLI, inicialize o Airflow com o comando:

```bash
astro dev init
```

Este comando criará a estrutura necessária para rodar o Airflow no ambiente local.

### 3. Iniciando o Airflow
Para iniciar o Airflow, use o comando:

```bash
astro dev start
```

Esse comando irá iniciar o ambiente de desenvolvimento local do Airflow, incluindo as DAGs configuradas.

### 4. Acessando a Interface do Airflow
A partir deste momento, você pode acessar a interface web do Airflow através de http://localhost:8080. Dentro dessa interface, você poderá visualizar a DAG do projeto, que estará automaticamente carregada.
![UI do airflow](/imgs/img-1.png)

### 5. Monitorando a Execução
Para monitorar a execução das tarefas, você pode acessar a aba Graph View no Airflow. Nela, você visualizará o fluxo de execução de cada uma das etapas do pipeline.
![Execuções no airflow](/imgs/img-2.png)


### 6. Verificando a Saída
Após a execução das tarefas, a resposta de saída pode ser visualizada na interface do Airflow, incluindo detalhes do processo de upload para o Amazon S3.
![Log airflow](/imgs/img-3.png)


### 7. Acessando o Bucket no AWS S3
Após a execução do pipeline, o arquivo CSV será enviado automaticamente para um bucket S3 previamente configurado. Para verificar o conteúdo, basta acessar o Amazon S3.
![UI S3](/imgs/img-4.png)
![UI S3](/imgs/img-5.png)


### Estrutura do Projeto
O projeto segue a seguinte estrutura de diretórios:

```
open-weather-data-pipeline/
│
├── dags/
│   └── open_weather_dag.py  
│   └──tasks/
├── requirements.txt              
└── README.md                 
```

### Pré-requisitos
- Python 3.7 ou superior
- AWS Account com permissões para criar e interagir com buckets S3
- API Key do Open Weather (disponível em OpenWeatherMap)