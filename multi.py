from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from supabase import create_client, Client
from threading import Thread, Event
import time
import names
import csv
import string
import random
import sys
import os

from concurrent.futures import (
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    wait,
    FIRST_EXCEPTION,
)

SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxYWtyb3dueHVqZWZodG1zZWZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIyNjMyMzMsImV4cCI6MjA0NzgzOTIzM30.E9jJxNBxFsVZsndwhsMZ_2hXaeHdDTLS7jZ50l-S72U"
SUPABASE_TABLE_NAME = "abrir"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))

    # return random.choice(string.ascii_letters)


def load_data(start_data, end_data):

    script_dir = os.path.dirname(os.path.realpath("__file__"))
    data_file = os.path.join(script_dir, "data.csv")

    data_account = []

    with open(data_file) as csv_data_file:
        data_account = list(csv.reader(csv_data_file, delimiter=","))

    data_account = data_account[int(start_data) : int(end_data)]

    return data_account


def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    # options.add_argument('--no-sandbox')
    # options.add_argument('--headless')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920, 1200")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver


def run_bot(data_account, recover=1):
    kw = data_account[0]

    driver = web_driver()
    

    try:

        
        namadepan = names.get_first_name()
        namabelakang = names.get_last_name()
        gmailnya = f'{namadepan}{random_string(7)}@gmail.com'
        time.sleep(3)

        title = kw

        username =  kw.replace(" ", "_")

        fix_username = username+random_string(5)

        judul =f'{kw} Leaked Onlyfans New Files Update {random_string(5)}' 

      

        xnama = namadepan+random_string(5)
        hasil_nama = xnama.lower()





        driver.get("https://abrir.link/en/user/register")
        time.sleep(5)


        driver.find_element(By.CSS_SELECTOR, "#input-username").send_keys(hasil_nama)
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "#input-email").send_keys(gmailnya)
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "#input-pass").send_keys('@@USKOPKELAo29')
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "#input-cpass").send_keys('@@USKOPKELAo29')
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "#terms").click()
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(7)


        driver.get("https://abrir.link/en/user/bio")
        time.sleep(5)

        driver.find_element(By.CSS_SELECTOR, "body > div.wrapper > div > main > div > div.d-flex.mb-5 > div.ms-auto > a").click()
        time.sleep(7)

        driver.find_element(By.CSS_SELECTOR, "#name").send_keys(judul)
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "#name").send_keys(Keys.ENTER)
        time.sleep(7)

        # driver.find_element(By.CSS_SELECTOR, "#createModal > div > div > form > div.modal-footer > button.btn.btn-success").click()
        # time.sleep(7)

        driver.find_element(By.XPATH,'//*[@id="links"]/div[2]/button').click()
        time.sleep(1)

        driver.find_element(By.XPATH,'//*[@id="content-content"]/div[6]/a/div').click()
        time.sleep(2)

        driver.find_element(By.XPATH,'//*[@id="linkcontent"]/form/div/div[2]/div[1]/div[1]/a').click()
        time.sleep(1)

        konten = f'''
        Get Access Content {title} Onlyfans Video and Pict For Free - New Update Files 2025 <br><br>
        LINK ⏩⏩  <a href="https://clipsfans.com/{username}">https://clipsfans.com/{username} </a> <br>

        Tags:<br>
        {title} Leaked Video <br>
        {title} Onlyfans Leaked<br>


            '''

        urii = driver.find_element(By.CSS_SELECTOR, "input[name='custom']")
        value = urii.get_attribute("value")

        

        driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="e.g. some description here"]').send_keys(konten)
        time.sleep(4)

        driver.find_element(By.CSS_SELECTOR,'button[data-trigger="savewidget"]').click()
        time.sleep(5)


        response = (
            supabase.table(SUPABASE_TABLE_NAME)
            .insert({"result": 'https://abrir.link/'+value})
            .execute()
        )

        print(f"SUKSES CREATE: {kw}", file=sys.__stderr__)

        time.sleep(2)
        driver.close()
    except Exception as e:
        if recover == 0:
            print(
                f"TERJADI ERROR: ${e}",
                file=sys.__stderr__,
            )
            #driver.close()
            return e

        run_bot(data_account, recover - 1)


def main():

    if len(sys.argv) < 3:
        print('Params require "node run.js 0 5"')
        os._exit(1)

    start_data = int(sys.argv[1])
    end_data = int(sys.argv[2])

    workers = 1

    if not start_data and not end_data:
        print('Params require "node run.js 0 5"')
        os._exit(1)

    data = load_data(start_data, end_data)

    futures = []
    line_count = 0
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for index in range(start_data + 1, end_data + 1):
            try:
                futures.append(
                    executor.submit(
                        run_bot,
                        data[line_count],
                    )
                )
            except:
                pass
            line_count += 1

    wait(futures, return_when=FIRST_EXCEPTION)


if __name__ == "__main__":
    main()
