'''
Exercicio 1

Crie um programa com o Selenium

- Gere um dicionario, onde a chave é a tag h1
    O valor deve ser um dicionario 
    Cada chave do valor deverá ser o valor de 'atributo'
    Cada valor deve ser o texto contido no elemento

https://curso-python-selenium.netlify.app/exercicio_01.html
'''

from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

browser = Firefox()
browser.get(url)

sleep(2)

h1 = browser.find_element_by_tag_name('h1')
print(h1.text)

dic = {}

p = browser.find_elements_by_tag_name('p')
#p_atribute = p.get_attribute("atributo")

n = 1
for element in p:
    p_chave = element.get_attribute("atributo")
    p_valor = element.find_element_by_xpath(f'/html/body/p[{n}]')
    n += 1

    dic[p_chave] = p_valor.text

print(dic)

