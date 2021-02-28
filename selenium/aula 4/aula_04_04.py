from selenium.webdriver import Firefox
from urllib.parse import urlparse

browser = Firefox()
browser.get("https://selenium.dunossauro.live/aula_04_b.html")

url_parseada = urlparse(browser.current_url)