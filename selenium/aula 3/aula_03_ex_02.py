'''
Exercicio 2

Crie um programa com o Selenium

- Jogue o jogo
- Quando voce ganhar o Script deve parar de ser executado 

https://curso-python-selenium.netlify.app/exercicio_02.html
'''

from selenium.webdriver import Firefox
from time import sleep
import re

uri = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

browser = Firefox()
browser.get(uri)

sleep(5)

elements = browser.find_elements_by_tag_name('p')

numero_esperado = browser.find_element_by_xpath("/html/body/p[2]")
numero_esperado = re.findall("[0-9]", numero_esperado.text)
numero_esperado = numero_esperado[0]

click = browser.find_element_by_tag_name("a")

print(len(elements))

n = 1
for element in elements:
    numero = element.find_element_by_xpath(f'/html/body/p[{n}]')

    if numero_esperado != numero.text:
        click.click()

    n += 1

