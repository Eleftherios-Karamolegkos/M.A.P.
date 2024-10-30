import requests
from bs4 import BeautifulSoup
import smtplib

with open(r'D:\University Bacău\MAP\parala_google.txt', 'r') as fishier:
    parola_google = fishier.read().strip()
##print(parola_google)

to_addr_list = ['eleftherioskaram@gmail.com']
cc_addr_list = ['']
sender = 'eleftherioskaram@gmail.com'
subject = 'A acajut pretul la produsul dorit'

def sendemail(sender, message, subject, to_addr_list, cc_addr_list=[]):
    try:
        smtpserver = 'smtp.gmail.com:587'
        header = 'From %s\n' % sender
        header+= 'To: %s\n' % ','.join(to_addr_list)
        header+= 'Cc: %s\n' % ','.join(cc_addr_list)
        header+= 'Subject: %s\n\n' % subject
        message = header + message
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(sender,parola_google)
        problems=server.sendmail(sender,to_addr_list,message)
        server.quit()
        return True
    except Exception as e:
        print("A aparut o eroare in trimiterea emai-ului")
        return False
    

def scrape_simplu():
    url = "https://www.emag.ro/telefon-mobil-apple-iphone-16-pro-max-256gb-5g-desert-titanium-mywx3zd-a/pd/DW367LYBM/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    print(soup.find_all('p'))  # p.product-new-price

def data_scraping():
    req = requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-16-pro-max-256gb-5g-desert-titanium-mywx3zd-a/pd/DW367LYBM/")
    soup = BeautifulSoup(req.text, 'html.parser')
    pret = soup.find('p', attrs={'class': 'product-new-price'}).text


    titlou_produsului = data_nume()
    ratingul_produsului = rating_produs()

    pret = pret[0:5]
    pret = pret.replace(".", "")
    pret = int(pret)
    pret_de_referinta = 7200
    ##print(titlou_produsului)
    if pret < pret_de_referinta:
        print("Pretul este mai mic de cat pretul de referinta")
        mesaj= f"Pretul actual: {pret} RON\n"
        mesaj+= f"Pretul de referinta: {pret_de_referinta} RON\n"
        mesaj+= f"A titlul pretul: {titlou_produsului}\n"
        mesaj+= f"Retingul produsului: {ratingul_produsului}\n"
        sendemail(sender, mesaj, subject, to_addr_list, cc_addr_list=[])
    else:
        print("pretul este mai mare de cat pretul de referinta")
    print(pret)
    ##print(ratingul_produsului)


def data_nume():
    req = requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-16-pro-max-256gb-5g-desert-titanium-mywx3zd-a/pd/DW367LYBM/")
    soup = BeautifulSoup(req.text, "html.parser")
    nume_produs = soup.find('h1', attrs={'class': 'page-title'}).text
    return nume_produs

def rating_produs():
    req = requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-16-pro-max-256gb-5g-desert-titanium-mywx3zd-a/pd/DW367LYBM/")
    soup = BeautifulSoup(req.text, "html.parser")
    rating = soup.find('p', attrs={'class': 'review-rating-data'}).text
    return rating

data_scraping()
