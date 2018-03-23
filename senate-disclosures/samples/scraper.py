from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://efdsearch.senate.gov/search/view/annual/046cfe80-e2e5-4fbf-a325-558a3db00bff/'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

# grabs Part 4b Transactions
transactions = page_soup.find("div",{"class":"row"})   
transaction = transactions.div.findAll("section",{"class":"card mb-2"})


filename = "products.csv"
f = open(filename,"w")

headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
	brand = container.div.div.a.img["title"]

	title_container = container.findAll("a",{"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li",{"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	print("brand: " + brand)
	print("product_name: " + product_name)
	print("shipping_container: " + shipping)

	f.write(brand + "," + product_name.replace(",","|") + "," + shipping + "\n") 

f.close()










