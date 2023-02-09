import smtplib
import email.message


def enviar_email(x): 
    corpo_email = f"""
    <p>Segue sua lista escolhida no aplicativo: </p>
    <p>{x}</p>
    """


    msg = email.message.Message()
    msg['Subject'] = "Teste"
    msg['From'] = 'rodrigo.navarro36@gmail.com'
    msg['To'] = 'rodrigo.navarro36@gmail.com'
    password = 'dzdfbkmnlmcmkyik'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
