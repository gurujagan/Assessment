import requests
import bs4
from bs4 import Beautifulsoup
import pandas as pd
import time
URL = "https://www.indeed.com/jobs?q=Python&l=Chennai&start=2"
page = requests.get(URL)
soup=Beautifulsoup(page.text,"html.parser")
print(soup.prettify())
