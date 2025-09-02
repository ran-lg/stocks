import pandas as pd
from dash import Dash, html, dcc, Input, Output, dash_table
from file_management import get_last_stat_filename, get_date_last_stat_filename

df = pd.read_csv(get_last_stat_filename(), sep = '|')
app = Dash(__name__)

def generate_table(df):
    return dash_table.DataTable(df.to_dict('records'),
                                  [{"name": i, "id": i} for i in ["company", "diff_30d", "diff_90d", "diff_360d", "diff_720d"]])

app.layout = [
    html.Div([html.H2(f'Closing price stats ({get_date_last_stat_filename()})')]), 
    generate_table(df)
]


if __name__ == '__main__':
    app.run(debug = False)