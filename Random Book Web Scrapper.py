from selenium import webdriver
from selenium.webdriver.common.by import By
import random


def random_book_url():
    number = random.choice(range(1, 70540))
    print(number)    
    random_url = f"https://www.gutenberg.org/cache/epub/{number}/pg{number}.txt"
    return random_url

random_url = random_book_url()
print(random_url)
url = random_url

driver = webdriver.Chrome(r"C:\Users\Henry\Personal Codes\Web Scrapping\Chrome Driver\chromedriver.exe")
driver.get(str(url))
driver.implicitly_wait(5)
body = driver.find_element(By.TAG_NAME,'body')

print(body.text)



from collections import Counter

def word_count(url, driver):
        driver = webdriver.Chrome(driver)
        driver.get(url)
        driver.implicitly_wait(4)
        body = driver.find_element(By.TAG_NAME,'body')
        return Counter(body.text.split())
        
print("Number of words in the file: ", word_count(url = random_book_url(), 
                                                  driver=r"C:\Users\Henry\Personal Codes\Web Scrapping\Chrome Driver\chromedriver.exe"))

