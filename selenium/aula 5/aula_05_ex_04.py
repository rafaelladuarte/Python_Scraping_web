from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse, parse_qsl

url = 'https://selenium.dunossauro.live/exercicio_04.html'

browser = Firefox()
browser.get(url)

sleep(2)

form = {
    'nome': browser.find_element_by_name('nome'),
    'email': browser.find_element_by_name('email'),
    'senha': browser.find_element_by_name('senha'),
    'telefone': browser.find_element_by_name('telefone'),
    'btn': browser.find_element_by_name('btn')
}

form['nome'].send_keys('elladarte')
form['email'].send_keys('livedepython@selenium.com')
form['senha'].send_keys('123456')
form['telefone'].send_keys('999999999')
form['btn'].click()

sleep(2)

dic_text_area = eval(browser.find_element_by_tag_name('textarea').text)
dic_text_url = dict(parse_qsl(urlparse(browser.current_url).query))

dic_text_url.pop('btn')

assert dic_text_area == dic_text_url

