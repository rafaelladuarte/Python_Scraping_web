from selenium.webdriver import Firefox

def find_by_text(browser, tag, text):
    """
    Encontrar o elemento com o texto 'text'

    Argumentos:
        - browser = Instancia do browser [firefox, chrome, ...]
        - texto = conteudo que deve estar na tag
        - tag = tag onde o texto sera procurado
    """

    elementos = browser.find_elements_by_tag_name(tag)

    for elemento in elementos:
        if elemento.text == text:
            return elemento

def find_by_href(browser, link):
    """
    Encontrar o elemento 'a' com link 'link'

    Argumentos:
        - browser = Instancia do browser [firefox, chrome,...]
        - link = link que será procurado em todas as tags 'a'
    """

    elementos = browser.find_elements_by_tag_name('a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento


browser = Firefox()
browser.get("https://selenium.dunossauro.live/aula_04_a.html")

#elemento_ddg = find_by_text(browser,'li','DuckDuckGo')
elemento_ddg = find_by_href(browser,'ddg')