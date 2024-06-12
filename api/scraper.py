# scraper.py
from bs4 import BeautifulSoup
import requests
from .models import Vault

class VaultScraper:
    def scrape(self):
        url = 'https://fallout.fandom.com/wiki/List_of_known_Vaults'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        data = self.extract_table_data(soup)
        self.create_rows(data)

        return data

    def create_rows(self, data):
        # Store data in the database
        for row in data:
            Vault.objects.create(
                name=row[0],
                location=row[1],
                purpose=row[2],
                additional_details=row[3],
                title=row[4]
            )

    def extract_table_data(self, soup):
        table = soup.find('table', class_='va-table va-table-full va-table-center sortable').find('tbody')
        rows = table.find_all('tr')[1:]  # Skip the header row

        data = []
        for row in rows:
            cols = row.find_all(['th', 'td'])
            row_data = [col.text.strip() for col in cols]
            data.append(row_data)

        return self.check_data(data)

    def check_data(self, data):
        data_checked = []
        aux = None

        for row in data:
            if len(row) == 5:
                data_checked.append(row)
                aux = row  # Save the current complete row for reference

            elif aux:
                # Fill in missing data from the last complete row
                if len(row) == 3:
                    row.insert(2, aux[2])  # Insert purpose
                    row.append(aux[4])     # Insert title

                data_checked.append(row)

        return data_checked
