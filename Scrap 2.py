import urllib2
from bs4 import Beutifulsoup
page=requests.get(" https://www.amazon.in/s?k=shoes+for+men+sparx&crid=2SFSGY4UQYKNM&sprefix=Shoes%2Caps%2C389&ref=nb_sb_ss_i_9_5" )
soup=Beautifulsoup(page.contetn.'html.parser')
