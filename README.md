# Money-Manager

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
accounted for $444 billion of debt. 
About 17 percent of disposable 
income
was spent making installment 
payments on credit card 
balances.Indeed, the use of credit 
cards allows people with
limited incomes to convince others 
that they are in the group of winners. 

## <b>Our Approach</b>:
<p>
First of all we wrote a code in python file named 'input.py' to take the input from the user in the format (Sr No.,Date,Amount,Description,Category) and store all
the records in the file named 'MoneyManager.csv'. Then we wrote a program in the file 'Money-manager.py' to read the input from the csv file and then we did some 
feature extraction on the data(like removing,merging some data, etc). Then we converted the dated in to the format MM-YYYY using pd.to_datetime() function.
And then we made the first graph i.e. the 'Net worth chart' using plotly.graph_objects where the x-axis is date and y-axis is Amount.
<p align="center">
<img src="https://github.com/prathammehta16/Money-Manager-1/blob/images/net_worth.png">
</p>
Then we made a pie chart using plotly to display expenses per category. 
Then we made a line chart called "Expenses_Breakdown_chart" which shows expenses on a category on a particular date.
Then we made a bar graph to show the total monthly expenses.

Then we also used Facebook Prophet neural network to predict future expenses that the user might incurr.
