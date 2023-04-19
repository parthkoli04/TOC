# Practical 3 - Reduction of a string


# prodrules = {
#     'S':'aAc',
#     'A':'Bb',
#     'B':'b',
# }

# string = str(input("Enter String: "))



def reDuction(grammer,string):
    n=len(string)
    parse_table = [[[] for i in range(n-j+1)] for j in range(n+1)]

    for j in range(1,n+1):
        for production in grammer:
            rhs = production[1]
            if len(rhs) == 1 and rhs[0] == string[j-1]:
                parse_table[1][j-1].append(production[0])

    for i in range(2,n+1):
        for j in range(n-i+1):
            for k in range(1,i):
                for production in grammer:
                    rhs=production[1]           
                    if len(rhs) == 2:
                        B = parse_table[k][j]
                        C= parse_table[i-k][j+k]
                        for b in B:
                            for c in C:
                                if b+c==rhs:
                                    parse_table[i][j].append(production[0])
    return 'Accepted' if 'S' in parse_table[n][0] else 'Rejected'


grammer = [('S','AB'),('A','BA'),('A','a'),('B','CC'),('B','b'),('C','AB'),('C','a')]

string = 'abbc'

print(reDuction(grammer,string))



