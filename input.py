import csv
fields=['Sr No.', 'Date', 'Amount', 'Description', 'Category']
lst = [ ]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = [int(input("Sr No:")),input("DATE:"), float(input("Amount:")),input("Description:"),
    input("Category [Food/Social Life/Self Development/Transportation/Culture/Household/Apprel/Beauty/Health/Education/Salary/Other]:")]
    lst.append(ele)

    
with open('321.csv','a') as f:
    csvwriter = csv.writer(f)
    #csvwriter.writerow(fields)
    for x in (lst):
        csvwriter.writerow(x)    
 
    
