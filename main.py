#!/usr/bin/env python3
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://resultados.tse.jus.br/oficial/app/index.html'
def main():
    driver.get(url)
    driver.maximize_window()
    cnt = 1
    while True:
        driver.refresh()
        sleep(60)
        cnt += 1
        print(f'Iniciando loop número {cnt}...')

if __name__ == '__main__':
    main()

