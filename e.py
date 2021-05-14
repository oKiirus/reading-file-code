def count():
    file = input('enter your file name: ')
    store = open(file, 'r')
    number = 0
    number2 = 0

    print('file:')
    for i in store:
        words = i.split()
        number = number + len(words)
        number2 += 1
    
        
        print(i)
    print('number of words: ' , number)
    print('number of lines: ', number2)

count()