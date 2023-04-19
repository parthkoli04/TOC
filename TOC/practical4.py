x='aba'

xx=[]

for i in x:
    xx.append(i)

prodRules={'a':'A','b':'B'}

userInput1=input('Enter the Input Alphabet: ')

if userInput1=='a':
    xx[0]=prodRules[xx[0]]
    print(xx)
    userInput1=input('Enter the Input Alphabet: ')
    if userInput1=='b':
        xx[1]=prodRules[xx[1]]
        print(xx)
        print(prodRules)
        userInput1=input('Enter the Input Alphabet: ')
        if userInput1=='a':
            xx[2]=prodRules['a']
            print(xx)  

main=""

for i in xx:
    main += i

if main=='ABA':
    print('Found!')
else:
    print('Not Found!')