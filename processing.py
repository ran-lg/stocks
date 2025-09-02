import pandas as pd

list_d = [30, 90, 360, 720]

def generate_stats(filename, companies):
    df = pd.read_csv(filename, delimiter = '|', dtype = {'c': 'datetime64'})
    my_list = []

    for ticker in list(df['ticker'].unique()):     
        my_dict = {'ticker': ticker}
        my_dict['company'] = companies[ticker]
        for d in list_d:
            df_d = df.loc[df['ticker'] == ticker].sort_values(by = ['ticker', 'date'], ascending = False).head(d)        
            my_dict[f'max_{d}d']  = df_d['close'].max()
            my_dict[f'min_{d}d']  = df_d['close'].min()
            my_dict[f'diff_{d}d'] = df_d['close'].iloc[0] - df_d['close'].iloc[-1]
        my_list.append(my_dict)

    return pd.DataFrame(my_list)
    
def generate_csv(df_stats, filename):
    df_stats.to_csv(filename, sep = '|', index = False)