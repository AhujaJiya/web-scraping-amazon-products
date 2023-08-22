import re
import openpyxl
from bs4 import BeautifulSoup

# Read the HTML file
with open("amazon.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all divs with the specified class
divs = soup.find_all("div", class_=re.compile(r'^s-card-container.*'))

# Initialize lists to store data
urls = []
names = []
prices = []
reviews = []

# Extract information from each div
for div in divs:
    # Extract URL
    url_tag = div.find("a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
    if url_tag:
        url = url_tag.get("href")
        urls.append(url)

    # Extract Name
    name_tag = div.find("span", class_="a-size-medium a-color-base a-text-normal")
    if name_tag:
        name = name_tag.get_text(strip=True)
        names.append(name)

    # Extract Price
    price_tag = div.find("span", class_="a-price-whole")
    if price_tag:
        price = price_tag.get_text(strip=True)
        prices.append(price)

    # Extract Review
    review_tag = div.find("span", class_="a-size-base puis-normal-weight-text")
    if review_tag:
        review = review_tag.get_text(strip=True)
        reviews.append(review)

# Create and populate an Excel file
wb = openpyxl.Workbook()
ws = wb.active
ws.append(["URLs", "Names", "Prices", "Reviews"])

for url, name, price, review in zip(urls, names, prices, reviews):
    ws.append([url, name, price, review])

# Save the Excel file
wb.save("amazon_bags_data.xlsx")
print("Data written to amazon_bags_data.xlsx")
