n_words = 0
 
with open(r'word.txt','r') as file:
 
    data = file.read()
 
    lines = data.split()
    for word in lines:
        if not word.isnumeric():         
 
            n_words += 1

print(n_words)
