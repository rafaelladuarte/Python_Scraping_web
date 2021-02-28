from selenium.webdriver import Firefox
from time import sleep

url = 'http://selenium.dunossauro.live/aula_05_c.html'

browser = Firefox()
browser.get(url)

def melhor_filme(browser, filme, email, telefone):
    # Preenche o formulario do melhor filme de 2020
    browser.find_element_by_name("filme").send_keys(filme)
    browser.find_element_by_name("email").send_keys(email)
    browser.find_element_by_name("telefone").send_keys(telefone)
    browser.find_element_by_name("enviar").click()

sleep(1)

melhor_filme(
    browser, 
    'Parasita',
    'livedepython@selenium.com',
    '(99)999999999'
)

sleep(2)
browser.quit()