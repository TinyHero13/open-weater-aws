# Open Weather Data Pipeline
Este projeto consiste em um script em Python que extrai dados meteorológicos da API Open Weather, realiza o tratamento dessas informações e armazena o resultado em formato CSV em um bucket do Amazon S3.

# 📋 Funcionalidades
- Conexão com a API Open Weather para obtenção de dados meteorológicos.
- Tratamento e transformação dos dados em um formato estruturado usando Pandas.
- Geração de um arquivo CSV com as informações tratadas.
- Criação do bucket no Amazon S3.
- upload do arquivo CSV para o bucket no Amazon S3.

# 🛠️ Tecnologias Utilizadas
- Python
- Pandas: Para manipulação e transformação dos dados.
- Boto3: Para interação com o Amazon S3.
- dotenv: Para gerenciar variáveis de ambiente e proteger as credenciais.
