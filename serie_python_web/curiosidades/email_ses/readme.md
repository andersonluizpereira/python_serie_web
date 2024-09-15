# Enviando E-mails com Python, Amazon SES e LocalStack

Este projeto demonstra como enviar e-mails utilizando o serviço **Amazon SES** (Simple Email Service) com a biblioteca **boto3** e **LocalStack**, que simula os serviços da AWS localmente. O LocalStack é uma ferramenta útil para testar seus scripts que utilizam serviços da AWS sem custos de infraestrutura.

# Leia aqui antes de começar a codar
https://medium.com/@andy2903-alp/rodando-ambiente-aws-s3-em-ambiente-local-df504f491b37
https://programadriano.medium.com/aws-ses-node-js-localstack-367c2bed60d2

## Pré-requisitos

1. **Python 3.x** instalado.
2. **boto3** para interagir com os serviços da AWS.
3. **LocalStack** para simular o SES localmente.
4. Docker para rodar o LocalStack.

### Instalando Dependências

Primeiro, instale as bibliotecas necessárias:

```bash
pip install boto3 localstack
```

Executando o LocalStack
Inicie o LocalStack no seu ambiente:

```bash
localstack start

#subindo recurso local
aws --endpoint-url=http://localhost:4566 ses verify-email-identity --email-address andy2903.alp@python.com.br --region us-east-1
```
Isso irá iniciar o LocalStack localmente, com o endpoint configurado por padrão em http://localhost:4566. O LocalStack simula vários serviços da AWS, incluindo o SES, que usaremos para enviar e-mails.

Configuração do Projeto
Você pode ajustar os seguintes parâmetros no script:

SENDER: O endereço de e-mail do remetente.
RECIPIENT: O endereço de e-mail do destinatário.
SUBJECT: O assunto do e-mail.
BODY_TEXT: O corpo do e-mail em formato de texto.
BODY_HTML: O corpo do e-mail em formato HTML.

## Exemplo de configuração no código:
```
SENDER = "sender@example.com"  # Remetente
RECIPIENT = "recipient@example.com"  # Destinatário
SUBJECT = "Assunto do E-mail LocalStack SES"
BODY_TEXT = "Olá, este é um e-mail enviado localmente com SES e LocalStack!"
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Olá!</h1>
  <p>Este é um e-mail enviado localmente com <b>SES e LocalStack</b>.</p>
</body>
</html>"""
```
# Código do Script
## Aqui está o código principal que envia e-mails utilizando o SES simulado pelo LocalStack:
```
import boto3
from botocore.exceptions import ClientError

# Configurações do SES LocalStack
localstack_endpoint_url = "http://localhost:4566"  # URL do LocalStack
AWS_REGION = "us-east-1"  # Região AWS (simulada pelo LocalStack)
SENDER = "sender@example.com"  # Endereço do remetente
RECIPIENT = "recipient@example.com"  # Endereço do destinatário
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
    aws_access_key_id="fake_access_key",  # Fake key para o LocalStack
    aws_secret_access_key="fake_secret_key",  # Fake secret para o LocalStack
)

# Função para enviar o e-mail
def enviar_email():
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

# Chamando a função para enviar o e-mail
enviar_email()
```
# Executando o Script
## Com o LocalStack em execução, execute o script Python para enviar o e-mail:
```commandline
python enviar_email.py
```
## Se o e-mail for enviado com sucesso, você verá a mensagem no terminal:
```commandline
E-mail enviado com sucesso! ID da mensagem: xxxxxx
```
# Caso ocorra algum erro, a exceção será capturada e uma mensagem de erro será exibida.
```commandline
Erro ao enviar e-mail: 'Error' 'Message'
```
#Verificando os Logs
## Para verificar o e-mail enviado no LocalStack, você pode verificar os logs usando o seguinte comando:
```commandline
docker logs localstack_main
```
Isso permitirá que você veja as atividades simuladas pelo LocalStack, incluindo o envio do e-mail.

Conclusão
Este projeto demonstra como enviar e-mails utilizando o Amazon SES com boto3 e simular o ambiente localmente usando o LocalStack. Essa abordagem é útil para testar funcionalidades sem depender dos custos e limitações dos serviços reais da AWS durante o desenvolvimento.

Licença
Este projeto é de uso livre, sinta-se à vontade para modificar e usar conforme sua necessidade.