

import pandas as pd                       
import numpy as np                        
from datetime import datetime     
import plotly.express as px               
import plotly.graph_objects as go          
from jupyter_dash import JupyterDash     
import dash_core_components as dcc       
import dash_html_components as html 


df = pd.read_csv("MoneyManager.csv")


df.drop('Sr No.', axis=1, inplace=True)


df['Category'] = np.where(df['Description'].str.contains('papa|mummy'),'Internal', df['Category'] )
df = df[df.Category != "Internal"] 


df['Category'] = np.where(df['Description'].str.contains('ola|uber|jugnoo'),'cab', df['Category'] )
df['Category'] = np.where(df['Description'].str.contains('Amazon|Flipkart'),'Online Shopping', df['Category'] )
df['Category'] = np.where(df['Description'].str.contains('mobile|speaker|charger|headphone'),'Electronics',
 df['Category'] )


df.Category.replace(["Bills", "Expenses", "General", "Housing", "Leisure"], "Other",inplace=True)
df.Category.replace(["Coffee", "Eating out", "Takeaway", "Lunch"], "Food",inplace=True)
df.Category.replace("Drinks", "Entertainment",inplace=True)
df.Category.replace("Petrol", "Transport",inplace=True)



def timestamp(x):
    return datetime.strptime(x, "%d-%m-%Y")


df['Date'] = df['Date'].apply(timestamp)


df.sort_values(by='Date', inplace=True)
df.reset_index(drop=True, inplace=True)


df['Date'] = pd.to_datetime(df['Date'])


df['Date'] = df['Date'].dt.year.astype('str') + '-' + df['Date'].dt.month.astype('str') + '-01'
df['Date'] = pd.to_datetime(df['Date'])
df['year_month_day'] = df['Date'].dt.strftime('%Y-%m')


Net_Worth_Table = df.groupby('year_month_day')['Amount'].sum().reset_index(name ='sum')
Net_Worth_Table['cumulative sum'] = Net_Worth_Table['sum'].cumsum()


Net_Worth_Chart = go.Figure(
    data = go.Scatter(x = Net_Worth_Table["year_month_day"], y = Net_Worth_Table["cumulative sum"]),
    layout = go.Layout(
        title = go.layout.Title(text="Net Worth Over Time"), template="plotly_white"
    )
)

Net_Worth_Chart.update_layout(
    xaxis_title = "Date",
    yaxis_title = "Net Worth )",
    hovermode = 'x unified'
    )

Net_Worth_Chart.update_xaxes(
    tickangle = 45)
Net_Worth_Chart.show()



df = df[df.Category != "Income"] 
df = df[df.Category != "income"]
df.Amount = df.Amount*(-1)


Total_Monthly_Expenses_Table = df.groupby('year_month_day')['Amount'].sum().reset_index(name='sum')
Total_Monthly_Expenses_Table = Total_Monthly_Expenses_Table.rename(columns={'year_month_day': 'DATE',
 'sum': 'TOTAL EXPENSE'})


Total_Monthly_Expenses_Chart = px.bar(Total_Monthly_Expenses_Table, x="DATE", y="TOTAL EXPENSE",
title="Total Monthly Expenses", template="plotly_dark")
Total_Monthly_Expenses_Chart.update_yaxes(title='Expenses', visible=True, showticklabels=True)
Total_Monthly_Expenses_Chart.update_xaxes(title='Date',visible=True, showticklabels=True)


Expenses_Breakdown_Table = pd.pivot_table(df, values = ['Amount'], index = ['Category', 'year_month_day'],
 aggfunc=sum).reset_index()
Expenses_Breakdown_Table.columns = [x.upper() for x in Expenses_Breakdown_Table.columns]
Expenses_Breakdown_Table = Expenses_Breakdown_Table.rename(columns={'YEAR_MONTH_DAY': 'DATE'})
Expenses_Breakdown_Table = Expenses_Breakdown_Table[['DATE', 'CATEGORY', 'AMOUNT']]


Expenses_Breakdown_Table_All_Dates = Expenses_Breakdown_Table.set_index(
    ['DATE', 'CATEGORY']
).unstack(
    fill_value=0
).asfreq(
    'M', fill_value=0
).stack().sort_index(level=1).reset_index()


Expenses_Breakdown_Table_All_Dates['DATE'] = pd.to_datetime(Expenses_Breakdown_Table_All_Dates['DATE'])
Expenses_Breakdown_Table_All_Dates['DATE'] = Expenses_Breakdown_Table_All_Dates['DATE'].dt.strftime('%Y-%m')


Expenses_Breakdown_Table_Final = Expenses_Breakdown_Table.append(Expenses_Breakdown_Table_All_Dates,
 ignore_index=True)
Expenses_Breakdown_Table_Final = Expenses_Breakdown_Table_Final.drop_duplicates(subset = ['DATE', 'CATEGORY'],
 keep = 'first')
Expenses_Breakdown_Table_Final = Expenses_Breakdown_Table_Final.sort_values(['DATE', 'CATEGORY'],
 ascending=[True, False],ignore_index=True)


latest_date = Expenses_Breakdown_Table_Final['DATE'].max()
df_latest_date = Expenses_Breakdown_Table_Final.loc[Expenses_Breakdown_Table_Final['DATE'] == latest_date]


categories_lst = ['Food','Social Life','Self Development','Transportation','Culture','Household','Apprel',
'Beauty','Health','Education','Salary', 'Other']
missing_cat_latest_date = pd.DataFrame({'CATEGORY':
 list(set(df_latest_date['CATEGORY']) ^ set(categories_lst))})
missing_cat_latest_date['AMOUNT']=0.0
missing_cat_latest_date['DATE']= df_latest_date['DATE'].max()
missing_cat_latest_date = missing_cat_latest_date [['DATE', 'CATEGORY', 'AMOUNT']]


Expenses_Breakdown_Table_Final = Expenses_Breakdown_Table_Final.append (missing_cat_latest_date)


Expenses_Pie_Chart = px.pie(Expenses_Breakdown_Table_Final,values="AMOUNT",names="CATEGORY",
 title="Expenses Pie Chart", template="plotly_dark")


Expenses_Breakdown_Chart = px.line(Expenses_Breakdown_Table_Final, x='DATE', y="AMOUNT",
 title="Expenses Breakdown", color = 'CATEGORY', template="none")
Expenses_Breakdown_Chart.update_yaxes(title='Expenses', visible=True, showticklabels=True)
Expenses_Breakdown_Chart.update_xaxes(title='Date', visible=True, showticklabels=True)



app = JupyterDash(__name__)

colors = {
    'background': 'white',
    
    'text': 'red'
}


app.layout = html.Div(style = {'backgroundColor': colors['background']}, children=[
    
    html.Div([
        
        html.H1(str(latest_date)+" Personal Finance ",style={'text-align':'center', 
        
        'color': colors['text']}),
        
        dcc.Graph(figure = Net_Worth_Chart)
    ]),
  
    
    html.Div([
        
        dcc.Graph(figure = Total_Monthly_Expenses_Chart)
    ]),
    
    
    html.Div([
        
        dcc.Graph(figure = Expenses_Breakdown_Chart)

    ]),

    
     html.Div([
        
        dcc.Graph(figure = Expenses_Pie_Chart)

    ])
])

    

if __name__ == "__main__":
	app.run_server()

   

    
