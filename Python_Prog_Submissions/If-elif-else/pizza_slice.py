'''Write Python code that asks a user how many pizza slices they want.
The pizzeria charges Rs 123.00 a slice. 
if user order even number of slices, price per slice is Rs 120.00. 
Print the total price depending on how many slices user orders.
'''

print("Enter the number of slices: ")
slices = int(input())
price_slice = 123.00
if(slices % 2 == 0):
    price_slice = 120.00
total_amount = slices * price_slice
print("Total amount for the entered slices is: %.2f" % total_amount)