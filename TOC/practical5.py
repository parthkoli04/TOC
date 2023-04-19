#{"A" : {"b":"1Lb", "0":"0Ra", "1":""}, "B":{"b":"bRc", "0":"0Lb", "1":"1Lb"}}
#tm["a"]["b"]

import re

states=""
states = input ("Enter a string containing states :")
start = input("which is your start state?:")
end = input("what are your final state(s)?:")

terminals=""
terminals = input ("Enter a string containing variables :")


tm  = {}
for state in states :
    tm[state] = {}
    for terminal in terminals:
        tm[state][terminal] = "-"

print(tm)


ans='y'
while ans=='y' :        
    tmentry = input("Enter rule as currstate:currinp:tablentry with a comma separated table entry as newstate,output,direction - ")
    tokens = tmentry.split(":")
    if (tokens[0] in states and tokens[1] in terminals):
        tm[tokens[0]][tokens[1]] = tokens[2]
    ans = input("Enter 'y' to contiue:")

print(tm)

for state in states :
    for terminal in terminals:
        print(tm[state][terminal])


userstring = input("enter a string to validate :")
userstring = start + userstring
currstate = start
while True:
    print("Current String -| ", userstring)
    stringparts = re.split(currstate, userstring)
    if((currstate in end) and (stringparts[0] =='' or re.search('b+', stringparts[0])) and (stringparts[1] =='' or re.search('b+', stringparts[1]))) :
        print("succcessfully parsed...")
        break
    if ( stringparts[1] =='' or tm[currstate][stringparts[1][0]] == '-') :
        print("cant proceed further...")
        break
    rule = tm[currstate][stringparts[1][0]]
    ruleparts = rule.split(",")
    currstate = ruleparts[0]
    stringparts[1] =  ruleparts[1] + stringparts[1][1:]
    if(ruleparts[2]=='L'):
        stringparts[0] = stringparts[0][:len(stringparts[0])-1] + currstate + stringparts[0][len(stringparts[0])-1]
    if(ruleparts[2]=='R'):
        stringparts[1] = stringparts[1][0] + currstate + stringparts[1][1:]

    userstring = stringparts[0] + stringparts[1]    