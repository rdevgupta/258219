#similiar to list and tuples but don't allow
#arbitrary indexing
#created using def and yield keywords
def count():
    i = 5
    while i>0:
        yield i 
        i = i-1
for i in count():
    print(i)