# selenium 4
# from selenium.webdriver.chrome.service import Service as ChromeService
# driver = webdriver.Chrome("C:\chrome webdriver/chromedriver.exe")
# ***************************************************************************


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import openpyxl
import smtplib
from email.message import EmailMessage
import glob
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
print(driver.execute_script("return navigator.userAgent;"))

# driver = webdriver.Chrome((ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://www.amazon.in/')
driver.implicitly_wait(10)
print("Title is :",driver.title)
print("URL is :",driver.current_url)
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Samsung")
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
# driver.find_element(By.XPATH, "").click()
driver.find_element(By.XPATH, "//span[text()='Samsung']").click()

mobile=driver.find_elements(By.XPATH, "//span[contains(@class,'a-size-medium a-color-base a-text-normal')]")
price=driver.find_elements(By.XPATH, "//span[contains(@class,'a-price-whole')]")

myphone=[]
myprice=[]

print("Total mobiles are :",len(mobile))
print("Total prices are :",len(price))

for i in mobile:
    # print(i.text)
    myphone.append(i.text)

for i in price:
    # print(i.text)
    myprice.append(i.text)

final=zip(myphone,myprice)

# for data in list(final):
#     print(data)

wb=openpyxl.Workbook()
sheet=wb.active
sheet.title="Amazon Mobiles"
sheet.append(["Mobiles","Price"])
for data in list(final):
    sheet.append(data)

wb.save("XiaomiPhone.xlsx")

msg=EmailMessage()
msg['Subject']='Amazon Iphone web scraping'
msg['From']='Abhishek Kumar'
msg['To']='x4abhiop@gmail.com','sahniak9868@gmail.com','cse2023abhinav5@iesbpl.ac.in','cse2023abhishek10@iesbpl.ac.in'
# msg.set_content('This is a test email')
with open('EmailTemplate.txt') as myfile:
    data=myfile.read()
    msg.set_content(data)

files=glob.glob('*.xlsx')
for file in files:
    with open(file,'rb') as f:
        file_data=f.read()
        file_name=f.name
        msg.add_attachment(file_data,maintype='application',subtype='xlsx',filename=file_name)



with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login('sahniak9868@gmail.com','eawbeidlglcmoiju')
    smtp.send_message(msg)

print("Email sent successfully 💕")




driver.quit()
