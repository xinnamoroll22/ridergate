from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import csv



chrome_options = Options()
# chrome_options.add_argument("--headless")  # Runs browser in the background (no GUI)

# Path to ChromeDriver executable
driver_path = r"C:\Users\Aiman Danial\Desktop\chromedriver.exe"  

# Initialize the Chrome WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


# Open the Mudah.my Vespa page
# url = "https://www.mudah.my/malaysia/motorcycles-for-sale/vespa"

# Mudah.my without any brands filtration
url = "https://www.mudah.my/malaysia/motorcycles-for-sale"
driver.get(url)

wait = WebDriverWait(driver, 100)  # 100 seconds timeout              

# vespas = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="sc-kIPQKe kNClJo"]')))
motorcycles = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="sc-eInJlc ggFGDy"]')))
# --scrapes everthing in one list
# price = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="sc-iQKALj fWRVpF"]')))
#             # class="sc-iQKALj fWRVpF"
# make_year = wait.until(EC.presence_of_all_elements_located((By.XPATH, './/div[@class="flex items-center gap-1" and @title="Manufactured Year"]')))
# condition =  wait.until(EC.presence_of_all_elements_located((By.XPATH, './/div[@class="flex items-center gap-1" and @title="Condition"]')))

                                                           
# vespas_list = []
# for v in range(len(vespas)):
#     vespas_list.append(vespas[v].text)

motorcycles_list = []
for m in range(len(motorcycles)):
    motorcycles_list.append(motorcycles[m].text)

# price_list = []
# for p in range(len(price)):
#     price_list.append(price[p].text)

# make_year_list = []
# for my in range(len(make_year)):
#     make_year_list.append(make_year[my].text)

# condition_list = []
# for c in range(len(condition)):
#     condition_list.append(condition[c].text)

time.sleep(3)
driver.close()

# if len(vespas_list) > 0:
#     print(vespas_list)
#     print(len(vespas_list))
       

if len(motorcycles_list)>0:
    print(motorcycles_list)
    print(len(motorcycles_list))

# if len(price_list) > 0:
#     print(price_list)
#     print(len(price_list))

# if len(make_year_list) > 0:
#     print(make_year_list)
#     print(len(make_year_list))

# if len(condition_list) > 0:
#     print(condition_list)


# with open('motors_data.csv', mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
    
#     # Write the header row
#     writer.writerow(['Name', 'Price', 'Condition', 'Make Year'])
    
#     # Process each item in the list
#     for item in motorcycles_list:
#         # Split the string by '\n' and write as a row
#         writer.writerow(item.split('\n'))


