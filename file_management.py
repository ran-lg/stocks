from datetime import datetime
from os import listdir

def generate_data_filename():
    return f'{datetime.now().strftime('%Y%m%d')}_close_hist.csv'

def generate_stat_filename():
    return f'{datetime.now().strftime('%Y%m%d')}_close_stat.csv'

def get_last_stat_filename():
    my_list = [f for f in listdir() if f.endswith('_close_stat.csv')]
    my_list.sort(reverse = True)
    return my_list[0]
    
def get_date_last_stat_filename():
    filename = get_last_stat_filename()
    return f'{filename[6:8]}/{filename[4:6]}/{filename[0:4]}'