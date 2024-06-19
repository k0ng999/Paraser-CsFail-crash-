import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import app_data
import random
import time

global current_game_value
global previous_game_value
global distance
global distance_bet
global driver
global options
global service
global chrome_driver_path

current_game_value = None
previous_game_value = None
distance = None
distance_bet = None
driver = None
options = None
service = None
chrome_driver_path = None


def write_to_csv(variable1):
    global distance
    with open('data.csv', 'a', newline='', encoding='UTF-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([variable1])


def autho_bet():
    time.sleep(random.uniform(0.67, 1.34))

    input_field = driver.find_element(By.ID, "bet-amount")
    input_field.clear()
    input_field.send_keys("0.1")

    time.sleep(random.uniform(0.52, 1.13))

    input_field = driver.find_element(By.ID, "ratio")
    input_field.clear()
    input_field.send_keys("10")

    time.sleep(random.uniform(0.87, 1.77))

    create_bet_button = driver.find_element(By.CLASS_NAME, "bet-creator__action")
    create_bet_button.click()


async def parser():
    global previous_game_value
    global current_game_value
    global distance
    global distance_bet
    global driver
    global options
    global service
    global chrome_driver_path

    chrome_driver_path = r'C:\Users\bayda\PycharmProjects\BotCSFAIL\.venv\chromedriver-win64\chromedriver.exe'
    service = Service(chrome_driver_path)

    options = Options()
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://3cs.fail/ru/crash")
    distance = 0
    distance_bet = 10
    time.sleep(10)

    while True:
        global previous_game_value
        try:
            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'history__game')))
                current_game_value = driver.find_element(By.CLASS_NAME, 'history__game').text.strip()
            except:
                print("Не удалось найти нужную информацию. Перезагрузка страницы.")
                driver.refresh()
                continue
            if current_game_value != previous_game_value:
                current_game_value.strip()
                current_game_value = current_game_value.rstrip('x')
                current_game_value = float(current_game_value)

                if current_game_value != previous_game_value:
                    if current_game_value >= 10:
                        write_to_csv(distance)
                        app_data.app_data_csv('day6.csv', distance)
                        if distance == 0:
                            distance_bet = 0
                        if distance >= 1:
                            distance_bet = 0
                            distance_bet += 1
                        distance = 0
                        previous_game_value = current_game_value
                    else:
                        distance += 1
                        distance_bet += 1
                        previous_game_value = current_game_value

                    if distance_bet == 5:
                        autho_bet()
                    elif distance_bet == 4:
                        autho_bet()
                    elif distance_bet == 3:
                        autho_bet()
                    elif distance_bet == 2:
                        autho_bet()
                    elif distance_bet == 1:
                        autho_bet()
                    print(distance_bet)
        except(ElementClickInterceptedException):
            print('Ошибка при клике на кнопку. Перезагрузка страницы.')
            driver.refresh()
            continue

        await asyncio.sleep(random.uniform(1.86, 2.53))


asyncio.run(parser())
