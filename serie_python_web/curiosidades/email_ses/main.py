import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def enviar_email_ses():
    # Configurações do SES LocalStack
    localstack_endpoint_url = "http://localhost:4566"  # URL do LocalStack
    AWS_REGION = "us-east-1"  # Região AWS (simulada pelo LocalStack)
    SENDER = "andy2903.alp@python.com.br"  # Endereço do remetente
    RECIPIENT = "andy2903.alp@gmail.com"  # Endereço do destinatário
    SUBJECT = "Assunto do E-mail LocalStack SES"
    BODY_TEXT = "Olá, este é um e-mail enviado localmente com SES e LocalStack!"
    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1>Olá!</h1>
      <p>Este é um e-mail enviado localmente com <b>SES e LocalStack</b>.</p>
    </body>
    </html>"""

    # Definindo o formato da mensagem
    CHARSET = "UTF-8"

    # Criando o cliente SES utilizando LocalStack
    ses_client = boto3.client(
        'ses',
        region_name=AWS_REGION,
        endpoint_url=localstack_endpoint_url,
        aws_access_key_id="asdf",  # Fake key para o LocalStack
        aws_secret_access_key="asdf",  # Fake secret para o LocalStack
    )
    try:
        # Envio do e-mail usando SES
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
        print(f"E-mail enviado com sucesso! ID da mensagem: {response['MessageId']}")
    except ClientError as e:
        print(f"Erro ao enviar e-mail: {e.response['Error']['Message']}")


pass

if __name__ == '__main__':
    enviar_email_ses()
