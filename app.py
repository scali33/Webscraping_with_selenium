from  selenium import webdriver
from selenium.webdriver.common.by import By

from pages.quotes_page import QuoetesPage

fox = webdriver.Firefox()


fox.get('http://quotes.toscrape.com/search.aspx')

page = QuoetesPage(fox)

author = input('Enter the author you want quotes from: ').title()
page.select_author(author)
tags = page.get_avaliable_tags()
print(f"select one of this tags: [{" | ".join(tags)}]")
page.select_tag(input('select tag: '))
page.search_button.click()

