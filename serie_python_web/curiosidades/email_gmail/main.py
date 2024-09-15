import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def enviar_email():
    meu_email = 'remetente@gmail.com'
    senha = 'senhaapp'
    # https://support.google.com/mail/?p=BadCredentials
    # para ter a senha de app do gmail sigas passos do link acima

    # Criando a mensagem
    msg = MIMEMultipart()
    msg['From'] = meu_email
    msg['To'] = 'destinatario@provedor.com'
    msg['Subject'] = 'Assunto do Email'

    # Corpo do email
    corpo = 'Olá, este é um e-mail enviado por um script Python!'
    msg.attach(MIMEText(corpo, 'plain'))

    # Conexão ao servidor SMTP do Gmail
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Segurança
        server.login(meu_email, senha)  # Login
        texto = msg.as_string()
        server.sendmail(meu_email, 'destinatario@gmail.com', texto)  # Enviando email
        server.quit()  # Fechando conexão
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')
    pass


if __name__ == '__main__':
    enviar_email()
