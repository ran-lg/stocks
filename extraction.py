import requests
from dotenv import load_dotenv
from os import getenv
from os.path import isfile
import csv

load_dotenv()
apikey = getenv('API_KEY')
endpoint = 'https://www.alphavantage.co/query'

def read_tickers_csv(tickers_csv):  
    with open(tickers_csv, 'r') as f:
        csv_reader = csv.reader(f, delimiter = '|')
        my_dict = {}
        for row in csv_reader:
            my_dict[row[0]] = row[1]
    return my_dict

# get a dictionary containing all stock prices of company_code since 20+ years

def extract_close_hist(ticker):
    params = {'apikey': apikey,
			  'function': 'TIME_SERIES_DAILY',
	  	  	  'symbol': ticker,
	  	  	  'outputsize': 'full'}
    response = requests.get(endpoint, params)
    raw_data = response.json()["Time Series (Daily)"]
    return [(date, float(raw_data[date]["4. close"])) for date in raw_data.keys()]

# create or update the daily file

def add_to_d_data_file(list_close_w_name, filename):
    does_exist = isfile(filename)
    
    with open(filename, 'w', newline = '') as f:
        csv_writer = csv.writer(f, delimiter='|')
        if not does_exist:
            csv_writer.writerow(("ticker", "company", "date", "close"))
        for close_w_name in list_close_w_name:
            csv_writer.writerow(close_w_name)
    
    return does_exist
