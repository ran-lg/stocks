from extraction import extract_close_hist, add_to_d_data_file, read_tickers_csv
from processing import generate_stats, generate_csv
from file_management import generate_data_filename, generate_stat_filename
from os import listdir
from shutil import move
from pathlib import Path

tickers_csv = 'tickers.csv'
    
def daily_routine():

    # move .csv to \csv (except the ticker file)
    
    # for f in listdir():
        # if f.endswith('.csv') and f != 'tickers.csv':
            # move(f, Path('csv') / '{f}')
       
    data_filename = generate_data_filename()
    stat_filename = generate_stat_filename()
    companies = read_tickers_csv(tickers_csv)

    # # extract and save the historical data for all tickers
    
    # list_close_w_name = []
    # for ticker in companies.keys():
        # close_hist = extract_close_hist(ticker)
        # for close in close_hist:
            # close_w_name = (ticker, companies[ticker], close[0], close[1])
            # list_close_w_name.append(close_w_name)
    # add_to_d_data_file(list_close_w_name, data_filename)
    
    # # generate statistics

    df_stats = generate_stats(data_filename, companies)
    generate_csv(df_stats, stat_filename)
    
if __name__ == '__main__':          
    daily_routine()