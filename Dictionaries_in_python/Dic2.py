# Keys(), values(), and Items() methods

spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)
    
for k in spam.keys():
 print(k)
 
for i in spam.items():
    print(i)
    
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))