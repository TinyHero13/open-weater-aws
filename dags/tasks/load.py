import boto3
from airflow.models import Variable
import io

bucket_name = Variable.get('AWS_BUCKET_NAME')
AWS_ACCESS_KEY_ID = Variable.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = Variable.get("AWS_SECRET_ACCESS_KEY")

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

s3 = session.client('s3')

def create_bucket():
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


def load(task_id, **kwargs):
    create_bucket()
    
    try:
        ti = kwargs['ti']
        df = ti.xcom_pull(task_ids=task_id)
    except Exception as e:
        print(f"Erro ao transformar os dados: {e}")
        return

    object_key = 'weather_data/weather.csv'

    upload_to_s3(df, bucket_name, object_key)
