from .models import Currency, Currency_Prices, Gold, Gold_Types, Fuel_Types, Fuel, Foreign_Currency



import re
import requests
from requests_html import HTMLSession



def get_currency_price(url):
    """
    Extracts currency prices from a given URL and returns a list of dictionaries.
    Each dictionary contains information about either market or bank prices.

    Returns a list of dictionaries in the format:
    [{'buy_market_price': '48.00', 'sell_market_price': '49.00', 'change': '0.20%'},
     {'buy_bank_price': '30.90', 'sell_bank_price': '30.90', 'change': '0.29%'}]
    """
    session = HTMLSession()
    response = session.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})

    prices = response.html.find('body > div.container.cur-container > div > div.col-md-8.cur-info-container > div.cur-cities-rates > table > tbody', first=True)

    if prices:
        heads = prices.find("th")
        heads = [head.text for head in heads]

        currency_data = []

        rows = prices.find("tbody tr")

        for i, row in enumerate(rows):
            cells = row.find("td")
            data = [cell.text for cell in cells]

            data[0] = heads[i]

            if 'Market' in heads[i]:
                currency_data.append({
                    "buy_market_price": data[1],
                    "sell_market_price": data[2],
                    "change_market": data[3]
                })
            else:
                currency_data.append({
                    "buy_bank_price": data[1],
                    "sell_bank_price": data[2],
                    "change_bank": data[3]
                })

        return currency_data
    else:
        raise ValueError("Prices table not found on the page.")


def get_currency_information(urls):
    """
    take two urls market and bank and return information like this
    """
    all_results = []
    for url in urls:
        session = HTMLSession()
        response = session.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})

        type = response.html.find("body > div.container.cur-container > div > div.col-md-8.cur-info-container > div.cur-convert-data > h3", first=True).text
        if "market" in type:
            type = "market"
        elif "bank" in type:
            type = "bank"

        buy = response.html.find("body > div.container.cur-container > div > div.col-md-8.cur-info-container > div.cur-data > div:nth-child(1) > div:nth-child(1) > span.value", first=True).text
        sell = response.html.find("body > div.container.cur-container > div > div.col-md-8.cur-info-container > div.cur-data > div:nth-child(1) > div:nth-child(2) > span.value", first=True).text
        try: 
            change = response.html.find("body > div.container.cur-container > div > div.col-md-8.cur-info-container > div.cur-data > div:nth-child(1) > div:nth-child(3) > span.up", first=True).text
        except AttributeError:
            change = '0.00% (0)'        
        prev_close = response.html.find("body > div.container.cur-container > div > div.col-md-8.cur-info-container > div.cur-data > div.row-data.cur-extra-data > div:nth-child(1) > span.value", first=True).text
        day_range = response.html.find("body > div.container.cur-container > div > div.col-md-8.cur-info-container > div.cur-data > div.row-data.cur-extra-data > div:nth-child(2) > span.value", first=True).text

        all_results.append({
            "type": type, "buy": buy, "sell": sell, "change": change, "prev_close": prev_close, "day_range": day_range,}) 
    return all_results

def get_currency_links(url):
    session = HTMLSession()
    response = session.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})

    market = list(response.html.find('body > div.container.cur-container > div > div.col-md-8.cur-info-container > div.cur-cities-rates > table > tbody > tr:nth-child(1) > th > a', first=True).absolute_links)[0]
    bank = list(response.html.find('body > div.container.cur-container > div > div.col-md-8.cur-info-container > div.cur-cities-rates > table > tbody > tr:nth-child(2) > th > a', first=True).absolute_links)[0]
    urls = [market, bank]
    return get_currency_information(urls)








#get and return all currencies data(name, abbreviation, buy_market_price, sell_market_price, change_market, buy_bank_price, sell_bank_price, change_bank)
def get_all_currencies(url="https://sarf-today.com/en/currencies"):
    """
    Retrieves information about all currencies from the specified URL.
    Returns a list of dictionaries containing currency details.
    """
    session = HTMLSession()
    response = session.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})

    currencies = response.html.find("#content > div.container > div > div.col-md-8 > table > tbody", first=True)

    if currencies:
        rows = currencies.find("tr")
        currency_list = []
        seen_currency_names = set()

        for row in rows:
            heads = row.find("th")
            heads_link = heads[0].find("a", first=True)
            heads_link = list(heads_link.absolute_links)[0]

            # https://sarf-today.com/en/currency/turkish_lira


            data = get_currency_links(heads_link)
            combined_dict = {}

            for entry in data:
                entry_type = entry['type']
                
                entry_dict = {
                    f'buy_{entry_type}_price': entry['buy'],
                    f'sell_{entry_type}_price': entry['sell'],
                    f'{entry_type}_change': entry['change'],
                    f'{entry_type}_prev_close': entry['prev_close'],
                    f'{entry_type}_day_range': entry['day_range']
                }

                combined_dict.update(entry_dict)

            

            


            heads = [head.text for head in heads]
            currency_name = heads[0].split(':')[0]

            cells = row.find("td")
            data = [cell.text for cell in cells]

            if currency_name not in seen_currency_names:
                name, abbreviation = currency_name.split(" (", 1)
                abbreviation = abbreviation.rstrip(")")

                currency_list.append({
                    "name": name,
                    "abbreviation": abbreviation,
                    **combined_dict  # Use the combined_dict here
                })
                seen_currency_names.add(currency_name)

        return currency_list





def get_gold_urls(url="https://sarf-today.com/en/gold"):
    session = HTMLSession()
    response = session.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})
    gold_data = response.html.find("#content > div > div > div.col-md-8 > table > tbody", first=True)

    if gold_data:
        rows = gold_data.find("tr")

        gold_urls = []
        for row in rows:
            heads = row.find("th", first=True)
            # heads = [head.text for head in heads]
            try:
                heads_link = heads.find("a", first=True)
                heads_link = list(heads_link.absolute_links)[0]

                print(heads_link)
                gold_urls.append(heads_link)
            except:
                pass
        
        return gold_urls
    
def get_ounce(url="https://sarf-today.com/en/gold"):
    
    session = HTMLSession()
    response = session.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})

    ounce = response.html.find("#content > div > div > div.col-md-8 > table > tbody > tr:nth-child(5)", first=True)
    if ounce is not None:
        # Extracting information from the HTML elements
        name = ounce.find("th > span", first=True).text
        buy = ounce.find("td:nth-child(3) > strong", first=True).text
        sell = ounce.find("td:nth-child(4) > strong", first=True).text

        # Creating the dictionary
        result = {'name': name, 'buy_price': buy, 'sell_price': sell, 'change': '', 'prev_close': '', 'day_range': ''}

        # Printing the result
        return result
    else:
        raise ValueError("Element not found.")



# get and return all gold data(name, buy_price, sell_price, change, prev_close, day_range) as a list of dict
def get_gold():
    
    urls = ['https://sarf-today.com/en/gold/karat14','https://sarf-today.com/en/gold/karat18','https://sarf-today.com/en/gold/karat21','https://sarf-today.com/en/gold/karat24']
    all_results = []
    for url in urls:
        session = HTMLSession()
        response = session.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})


        # get karat name
        karat_name_element = response.html.find("body > div.container.cur-container > div > div.col-md-8.cur-info-container > div.cur-header > div:nth-child(1) > h1", first=True)
        karat_name_text = karat_name_element.text

        # Extract karat value using regular expression
        karat_value_match = re.search(r'(\d+)Karat', karat_name_text)
        if karat_value_match:
            karat_value = int(karat_value_match.group(1))
            karat_name = f'{karat_value}Karat'
        else:
            print("Unable to determine karat value.")


        # get karat values
        gold_data = response.html.find("body > div.container.cur-container > div > div.col-md-8.cur-info-container > div.cur-data", first=True)

        if gold_data:
            gold_data_text = gold_data.text
            lines = gold_data_text.strip().split('\n')
            result = {}
            result["name"] = karat_name
            for line in lines:
                if "Buy" in line:
                    result['buy_price'] = line.split()[1]
                elif "Sell" in line:
                    result['sell_price'] = line.split()[1]
                elif "%" in line:
                    result['change'] = line.strip()
                elif "Prev. close" in line:
                    result['prev_close'] = line.split()[2]
                elif "Day's range" in line:
                    result['day_range'] = line.split()[2] + ' - ' + line.split()[4]

            all_results.append(result)
        else:
            print("Unable to fetch gold data.")
        

    all_results.append(get_ounce())
    return all_results



# get all fuel data (name, buy_price, sell_price, change, prev_close, day_range)
def get_fuel():
    # urls = ['https://sarf-today.com/en/fuel/octane_80']
        
    urls = [
        'https://sarf-today.com/en/fuel/octane_80',
        'https://sarf-today.com/en/fuel/octane90',
        'https://sarf-today.com/en/fuel/octane95',
        'https://sarf-today.com/en/fuel/solar'
    ]


        
    all_results = []

    for url in urls:
        session = HTMLSession()
        response = session.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})
        fuel = response.html.find("body > div.container.cur-container > div > div.col-md-8.cur-info-container", first=True)
        

        if fuel is not None:
        # Extracting information from the HTML elements
            name = fuel.find("div.cur-header > div > h2", first=True).text
            octane_rating_match = re.search(r'Octane (\d+)', name)
            if octane_rating_match:
                octane_rating = octane_rating_match.group(1)
                name =  f"Octane {octane_rating}"
            else:
                name = 'Solar'

            buy = fuel.find("div.cur-data > div:nth-child(1) > div:nth-child(1) > span.value", first=True).text
            sell = fuel.find("div.cur-data > div:nth-child(1) > div:nth-child(2) > span.value", first=True).text
            change = fuel.find("div.cur-data > div:nth-child(1) > div:nth-child(3) > span.down", first=True).text
            prev_close = fuel.find("div.cur-data > div.row-data.cur-extra-data > div:nth-child(1) > span.value", first=True).text
            day_range = fuel.find("div.cur-data > div.row-data.cur-extra-data > div:nth-child(2) > span.value", first=True).text

            # Creating the dictionary
            result = {'name': name, 'buy_price': buy, 'sell_price': sell, 'change': change, 'prev_close': prev_close, 'day_range': day_range}

            all_results.append(result)

    return all_results



# get all foreign currencies data( currency, exchange_currency, rate)
def get_foreign_exchange(url='https://sarf-today.com/en', selector='#content > div > div > div.col-md-3 > div:nth-child(2)'):
    try:
        # Make HTTP request
        session = HTMLSession()
        response = session.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})

        # Check if the selector is found
        foreign = response.html.find(selector)
        if not foreign:
            print(f"No matching element found for selector: {selector}")
            return []

        # Extract text content from the div element
        div_text = foreign[0].text

        # Define a regular expression pattern to match the desired information
        pattern = re.compile(r'(\w+/\w+):\s([\d.]+)\s(\w+)')

        # Find all matches in the text
        matches = pattern.findall(div_text)

        # Create a list of dictionaries with extracted information
        result_list = []
        for match in matches:
            currency_pair, rate, exchange_currency = match
            base_currency, _, quote_currency = currency_pair.partition('/')
            result_dict = {
                "currency": base_currency,
                "exchange_currency": quote_currency,
                "rate": rate
            }
            result_list.append(result_dict)

        return result_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return []





####################### this the functions will work in celery #########################


# put currencies data in database 
def currencies_in_database():
    exchange_currency, _ = Currency.objects.get_or_create(name="Egypt Bound", abbreviation="EGP")
    currencies = get_all_currencies()
    for scrape_currency in currencies:
        try:
            currency, _ = Currency.objects.get_or_create(name=scrape_currency["name"], abbreviation=scrape_currency["abbreviation"])
          
            currency_price = Currency_Prices.objects.create(
                currency=currency, exchange_currency=exchange_currency,
                buy_market_price=float(scrape_currency["buy_market_price"]),
                sell_market_price=float(scrape_currency["sell_market_price"]),
                market_change=scrape_currency["market_change"],
                market_prev_close=scrape_currency["market_prev_close"],
                market_day_range=scrape_currency["market_day_range"],
                buy_bank_price=float(scrape_currency["buy_bank_price"]),
                sell_bank_price=float(scrape_currency["sell_bank_price"]),
                bank_change=scrape_currency["bank_change"],
                bank_prev_close=scrape_currency["bank_prev_close"],
                bank_day_range=scrape_currency["bank_day_range"],
            )
            currency_price.save()

        except Exception as e:
            return f"An error occurred: {e}"
    
    return "currencies are saved"


# put currencies data in database 
def gold_in_database():
    golds = get_gold()
    exchange_currency, _ = Currency.objects.get_or_create(name="Egypt Bound", abbreviation="EGP")

    # Your loop starts here
    for scrape_gold in golds:
        try:
            karat, _ = Gold_Types.objects.get_or_create(name=scrape_gold["name"])

            if scrape_gold['name'] == 'Gold Ounce':
                gold = Gold.objects.create(karat=karat, currency=exchange_currency, buy_price=float(scrape_gold["buy_price"].replace(',', '')))
                gold.save()
            else:
                gold = Gold.objects.create(
                    karat=karat,
                    currency=exchange_currency,
                    buy_price=float(scrape_gold["buy_price"].replace(',', '')),
                    sell_price=float(scrape_gold["sell_price"].replace(',', '')),
                    change=scrape_gold["change"],
                    prev_close=scrape_gold["prev_close"],
                    day_range=scrape_gold["day_range"],
                )
                gold.save()
        except Exception as e:
            print(f"An error occurred: {e}")
    return "gold are saved"


# put fuels data in database 
def fuel_in_database():
    fuels = get_fuel()
    exchange_currency, _ = Currency.objects.get_or_create(name="Egypt Bound", abbreviation="EGP")

    for scrape_fuel in fuels:
        try:
            fuel, _ = Fuel_Types.objects.get_or_create(name=scrape_fuel["name"])


            fuel_object = Fuel.objects.create(
                fuel=fuel,
                currency=exchange_currency,
                buy_price=float(scrape_fuel["buy_price"].replace(',', '')),
                sell_price=float(scrape_fuel["sell_price"].replace(',', '')),
                change=scrape_fuel["change"],
                prev_close=scrape_fuel["prev_close"],
                day_range=scrape_fuel["day_range"],
            )
            fuel_object.save()
        except Exception as e:
            print(f"An error occurred: {e}")
    
    return "fuel saved in database"
   
    
# put foreign_currency_in_database
def foreign_currency_in_database():
    currencies = get_foreign_exchange()
    try:

        for data in currencies:
            try:
                # Get or create the foreign currency
                foreign_currency, _ = Currency.objects.get_or_create(abbreviation=data["currency"])

                # Get or create the exchange currency
                exchange_currency, _ = Currency.objects.get_or_create(abbreviation=data["exchange_currency"])

                # Create or update the Foreign_Currency object
                foreign_currency_object = Foreign_Currency.objects.create(
                    currency=foreign_currency,
                    exchange_currency=exchange_currency,
                    rate= float(data["rate"])
                )
                foreign_currency_object.save()
 
            except Exception as e:
                return f"An error occurred while processing foreign exchange data: {e}"
                

    except Exception as e:
        return f"An error occurred: {e}"
    
    return "foreign currencies saved in database"



def main():
    ...


if __name__ == "__main__":
    main()
