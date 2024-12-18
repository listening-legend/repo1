"'This program is just a luhn algorithm which is used to verify a credit or debit card'"
account_number=input("Enter your primary account number: ")
if len(account_number)>16:
    print("Invalid account number")
elif len(account_number)==16:
    pass
else:
    print("Invalid account number")
num=account_number
num15=num[14]
process15=int(num15)*2
PROCESS15=str(process15)
if process15>=10:
    answer15=int(PROCESS15[0])+int(PROCESS15[1])
else:
    answer15=PROCESS15
num13=num[12]
process13=int(num13)*2
PROCESS13=str(process13)
if process13>=10:
    answer13=int(PROCESS13[0])+int(PROCESS13[1])
else:
    answer13=PROCESS13
num11=num[10]
process11=int(num11)*2
PROCESS11=str(process11)
if process13>=10:
    answer11=int(PROCESS13[0])+int(PROCESS13[1])
else:
    answer11=PROCESS11
num9=num[8]
process9=int(num9)*2
PROCESS9=str(process9)
if process9>=10:
    answer9=int(PROCESS9[0])+int(PROCESS9[1])
else:
    answer9=PROCESS9
num7=num[6]
process7=int(num7)*2
PROCESS7=str(process7)
if process7>=10:
    answer7=int(PROCESS7[0])+int(PROCESS7[1])
else:
    answer7=PROCESS7
num5=num[4]
process5=int(num5)*2
PROCESS5=str(process5)
if process5>=10:
    answer5=int(PROCESS5[0])+int(PROCESS5[1])
else:
    answer5=PROCESS5
num3=num[2]
process3=int(num3)*2
PROCESS3=str(process3)
if process3>=10:
    answer3=int(PROCESS3[0])+int(PROCESS3[1])
else:
    answer3=PROCESS3
num1=num[0]
process1=int(num1)*2
PROCESS1=str(process1)
if process1>=10:
    answer1=int(PROCESS1[0])+int(PROCESS1[1])
else:
    answer1=PROCESS1
answer2=num[1]
answer4=num[3]
answer6=num[5]
answer8=num[7]
answer10=num[9]
answer12=num[11]
answer14=num[13]
total_answer=int(answer1)+int(answer2)+int(answer3)+int(answer4)+int(answer5)+int(answer6)+int(answer7)+int(answer8)+int(answer9)+int(answer10)+int(answer11)+int(answer12)+int(answer13)+int(answer14)+int(answer15)
TOTAL_ANSWER=str(total_answer)
if len(TOTAL_ANSWER)==2:
    TEN=TOTAL_ANSWER[1]
    checkdigit=10-int(TEN)
if len(TOTAL_ANSWER)==3:
    TEN=TOTAL_ANSWER[2]
    checkdigit=10-int(TEN)
if str(checkdigit)==num[15]:
    print("Your primary account number is valid")
elif str(checkdigit)!=num[15]:
    print("Your primary account number is invalid")
else:
    print("Sorry error occured")
