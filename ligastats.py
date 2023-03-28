import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the URL
url = "https://www.tycsports.com/estadisticas/liga-profesional-de-futbol.html"
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the statistics
table = soup.find('table')

# Extract the table headers
headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

# Extract the table rows
rows = []
for tr in table.find_all('tr')[1:]:
    row = []
    for td in tr.find_all('td'):
        row.append(td.text.strip())
    rows.append(row)

# Create a Pandas DataFrame with the headers and rows
df = pd.DataFrame(data=rows, columns=headers)

# Save DataFrame to an Excel file using openpyxl engine
writer = pd.ExcelWriter('liga.xlsx', engine='openpyxl')
df.to_excel(writer, sheet_name="liga", index=False)
writer.save()

# Print success message and close webdriver
print("Data successfully scraped and saved to 'liga-profesional-stats.csv")