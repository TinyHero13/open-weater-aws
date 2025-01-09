import boto3
from src.transform import transform
from dotenv import load_dotenv
import os
import io

load_dotenv()

def create_bucket():
    s3 = boto3.client('s3')
    bucket_name = os.getenv('AWS_BUCKET_NAME')

    if not bucket_name:
        print("Erro: A variável de ambiente 'AWS_BUCKET_NAME' não está definida.")
        return

    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' criado com sucesso.")
    except s3.exceptions.BucketAlreadyExists:
        print(f"O bucket '{bucket_name}' já existe.")
    except s3.exceptions.BucketAlreadyOwnedByYou:
        print(f"O bucket '{bucket_name}' já pertence a você.")
    except Exception as e:
        print(f"Erro ao criar o bucket: {e}")


def upload_to_s3(df, bucket_name, object_key):
    s3 = boto3.client('s3')

    with io.StringIO() as csv_buffer:
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        try:
            s3.put_object(
                Bucket=bucket_name,
                Key=object_key,
                Body=csv_buffer.getvalue(),
                ContentType='text/csv'
            )
            print(f"Arquivo '{object_key}' carregado com sucesso no bucket '{bucket_name}'.")
        except Exception as e:
            print(f"Erro ao carregar o arquivo para o bucket S3: {e}")


def load():
    try:
        df = transform()
    except Exception as e:
        print(f"Erro ao transformar os dados: {e}")
        return

    bucket_name = os.getenv('AWS_BUCKET_NAME')

    object_key = 'weather_data/weather.csv'

    upload_to_s3(df, bucket_name, object_key)

if __name__ == "__main__":
    create_bucket()
    load()