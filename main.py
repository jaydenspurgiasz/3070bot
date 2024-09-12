from selenium import webdriver
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from dotenv import load_dotenv
import os

load_dotenv()

# Import env variables
ADDRESS = os.getenv("ADDRESS")
PASSWORD = os.getenv("PASSWORD")
RECIEVER = os.getenv("RECIEVER")

# Bestbuy link to buy from
link = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
#link = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402"


try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(ADDRESS, PASSWORD)
except:
    print("SOMETHING WENT WRONG...")
def sendEmail(body):
    message = MIMEMultipart()
    message['From'] = ADDRESS
    message['To'] = RECIEVER
    message['Subject'] = 'GRAPHICS CARD ALERT'
    message.attach(MIMEText(body, 'plain'))
    text = message.as_string()
    server.sendmail(ADDRESS, RECIEVER, text)


driver = webdriver.Firefox()
driver.get(link)
buyButton = False

while not buyButton:
    addToCartBtn = addButton = driver.find_elements_by_class_name("btn-disabled")
    if len(addToCartBtn) == 1:
        print("Button is not ready yet.")
        time.sleep(1)
        driver.refresh()
    elif len(addToCartBtn) == 0:
        addToCartBtn = addButton = driver.find_elements_by_class_name("btn-lg")
        time.sleep(2)
        addToCartBtn[0].click()
        print("Ok it worked"*10)
        print("CHECK!!!!"*100)
        print(addToCartBtn)
        buyButton = True
        time.sleep(3)
        driver.get("https://www.bestbuy.com/cart")
        sendEmail("CHECK THE COMPUTER: " + link)
        server.quit()
