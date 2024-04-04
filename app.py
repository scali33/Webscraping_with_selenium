from  selenium import webdriver

from pages.quotes_page import QuoetesPage,InvlidtagForAuthorError
try:
    author = input('Enter the author you want quotes from: ').title()

    tag =  input('select tag: ')
    fox = webdriver.Firefox()

    fox.get('http://quotes.toscrape.com/search.aspx')

    page = QuoetesPage(fox)



    print(page.search_for_qutoes(author,tag))

except InvlidtagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
fox.close()