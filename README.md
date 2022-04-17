# Money-Manager
### Concepts used:
Python, pandas, numpy, plotly, Dash, HTML, Jupyter Notebook,Deep learning, Facebook Prophet
## <b>Introduction</b>:
The term Personal Finance refers 
to how you manage your money and 
plan for your future. All of your 
financial 
decisions and activities have an effect 
on your financial health. 
 In this times of Consumerism 
and materialistic Obsession, it is hard 
to track all our expenses and due to 
this
we end up spending more money 
than we thought of.
 Money comes in, money goes 
out. For many people this is about as 
deep as their understanding gets 
when it comes 
to personal finances.
 After the invention of credit 
cards in late 1950's and interest rates 
getting record low, people all around 
the globe were more likely to take 
debt to fulfil their personal 
requirements.
 By the late 1990, credit cards 
accounted for <b>$444</b> billion of debt. 
About <b>17</b> percent of disposable 
income
was spent making installment 
payments on credit card 
balances.Indeed, the use of credit 
cards allows people with
limited incomes to convince others 
that they are in the group of winners. 

## <b>Our Approach</b>:
<p>
 First of all we wrote a code in python file named <u>'input.py'</u> to take the input from the user in the format (Sr No.,Date,Amount,Description,Category) and store all
 the records in the file named <u>'MoneyManager.csv'</u>. Then we wrote a program in the file <u>'Money-manager.py'</u> to read the input from the csv file and then we did some 
feature extraction on the data(like removing,merging some data, etc). Then we converted the dated in to the format <b>MM-YYYY</b> using <b>pd.to_datetime()</b> function.
And then we made the first graph i.e. 
 <br>1. the <b>'Net worth chart'</b> using plotly.graph_objects where the x-axis is date and y-axis is Amount.
<p align="center">
<img src="https://github.com/prathammehta16/Money-Manager-1/blob/images/net_worth.png">
</p>
2. Then we made a <b>pie chart</b> using plotly to display expenses per category. 
<p align="center">
<img src="https://github.com/prathammehta16/Money-Manager-1/blob/images/pie_chart.png">
</p>
3. Then we made a line chart called <b>"Expenses_Breakdown_chart"</b> which shows expenses on a category on a particular date.
<p align="center">
<img src="https://github.com/prathammehta16/Money-Manager-1/blob/images/expenses_breakdown.png">
</p>
4. Then we made a <b>bar graph</b> to show the total monthly expenses.
<p align="center">
<img src="https://github.com/prathammehta16/Money-Manager-1/blob/images/total_monthly.png">
</p>
5. Then we also used <b>Facebook Prophet neural network</b> to predict future expenses that the user might incurr.
<p align="center">
<img src="https://github.com/prathammehta16/Money-Manager-1/blob/images/facebook_prophet(1).png">
</p>
<p align="center">
<img src="https://github.com/prathammehta16/Money-Manager-1/blob/images/facebook_prophet(2).png">
</p>

## <b>Conclusion</b>
<p>
 The financial literacy is very low in 
the world. Very few people track their 
expenses and in turn they always
spend way more than they need.
Thus By using our App, the person 
can continuously track their monthly 
expenses, where they spent most of 
their
money, etc. which would help the 
user to cut down their unneccessary 
expenses.</p>
