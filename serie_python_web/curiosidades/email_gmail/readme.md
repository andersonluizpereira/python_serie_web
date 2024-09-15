# Envio de E-mail com Python usando SMTP

Este é um script simples em Python para enviar e-mails usando o servidor SMTP do Gmail. Ele utiliza as bibliotecas `smtplib` e `email.mime` para criar e enviar mensagens de e-mail com segurança.

## Pré-requisitos

Antes de executar o script, você precisará:

1. **Python 3.x** instalado no seu sistema.
2. Uma conta do **Gmail** para ser usada como remetente.
3. Ter a opção "Acesso a apps menos seguros" ativada na conta do Gmail. [Saiba mais](https://myaccount.google.com/lesssecureapps) ou configure uma senha de app se a verificação em duas etapas estiver ativada [aqui](https://myaccount.google.com/apppasswords).

## Instalação

Clone ou baixe este repositório e certifique-se de que as bibliotecas necessárias estão instaladas:

```bash
pip install secure-smtplib

Configuração
No script, você deve alterar as variáveis abaixo com suas próprias informações:

python
Copy code
meu_email = 'seuemail@gmail.com'    # Substitua pelo seu e-mail
senha = 'suasenha'                  # Substitua pela sua senha

Uso
Depois de configurar o script com as suas informações, você pode executá-lo diretamente no terminal:

bash
Copy code
python enviar_email.py
Se tudo estiver correto, o e-mail será enviado com sucesso e você verá a mensagem:

mathematica
Copy code
E-mail enviado com sucesso!
Caso ocorra algum erro, o script irá exibir uma mensagem de erro correspondente.
```
### Funcionalidades
Conexão segura com o servidor SMTP do Gmail.
Envio de e-mails personalizados com assunto e corpo de mensagem.
Tratamento de erros com exceções.

# Licença
Este projeto é de uso livre, sinta-se à vontade para modificar e usar conforme sua necessidade.


Esse `README.md` fornece uma visão geral clara de como configurar e executar o script, bem como detalha os pré-requisitos e personalizações necessárias.