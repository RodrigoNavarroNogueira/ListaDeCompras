import smtplib
import email.message
from src.utils.settings import EMAIL, PASSWORD


def receber_email(x):
    if x == 'Esta lista está vazia!':
        option = 2
        return option
    else:
        option = 0
        while option == 0 or option not in [1, 2]:
             option = int(input('\nDeseja receber a lista no e-mail? (1) SIM (2) NÃO:\n\n'))
    return option


def enviar_email(x): 
    corpo_email = f"""
    <p>Segue sua lista escolhida no aplicativo:</p>
    <p>{x}</p>
    <p>{'Boas compras!' if 'Produto' in x else 'Tente novamente após adicionar produtos na sua lista.'}</p>
    """


    msg = email.message.Message()
    msg['Subject'] = "Sua lista de compras"
    msg['From'] = EMAIL
    msg['To'] = EMAIL
    password = PASSWORD
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
