import requests
import smtplib

from email.mime.text import MIMEText

with open(r'D:\University Bacău\MAP\cheie_api.txt') as fisier:
    API_KEY = fisier.read().strip()
    fisier.close()

with open(r'D:\University Bacău\MAP\parala_google.txt') as fisier_google:
    parola_google = fisier_google.read().strip()
    fisier_google.close()

#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
URL_API = "https://api.openweathermap.org/data/2.5/weather"
oras = input("Introdu numele orasului: ")
units = "metric"

email = "eleftherioskaram@gmail.com"
email_destinator = "eleftherioskaram@gmail.com"

request_url = f"{URL_API}?q={oras}&appid={API_KEY}&units={units}"


def starea_vremi ():
    raspuns = requests.get(request_url)
    if raspuns.status_code == 200:
        data = raspuns.json()
        temperatura = data["main"]["temp"]
        umiditate = data["main"]["humidity"]
        status_vreme = data["weather"][0]["description"]
        return temperatura,umiditate, status_vreme
    else:
        print("Eroare pentru Request-ul tau !!!")


def trimitere_email(temp, umid, sts_vreme):
    msg = MIMEText(f"Vreme:{sts_vreme}\nTemperatura: {temp}\nUmiditate:{umid}")
    msg['Subject'] = "Starea vremi de azi."
    msg["From"] = "Starea vremi de astazi"
    msg['To'] = email_destinator

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smpt_server:
        smpt_server.login(email,parola_google)
        smpt_server.sendmail(email,email_destinator,msg.as_string())
    print("Mesajul a fost trimis")

temp, umid, sts_vreme = starea_vremi()
trimitere_email(temp, umid, sts_vreme)
print(f"Temperatura pentru orasul {oras} : {temp}\nUmiditate: {umid}%\nDescriere vreme: {sts_vreme}")        
#print(API_KEY)
