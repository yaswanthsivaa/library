Amount = 10000

print('------- Welcome to Bank -------')
while True:
    User = input('Enter Your operation(check balance,withdraw,depoiste):  ')
    if User == 'exit':
      break
    if User.casefold() == 'checkbalance'.casefold():
      print('Your Amount is:  ',Amount)
      
    elif User.casefold() == 'withdraw'.casefold():
      amount = int(input('Enter the amount:  '))
      if amount <= Amount:
         print(f'Take your Amount:  {amount}\n Remaining Balance  :{Amount - amount}')  
         Amount -= amount
      else:
         print('Insufficient Balance')
         break
    else:
      deposite = int(input('Enter the Amount to Deposite:  '))
      Amount += deposite 
      print('Your Balance is:  ',Amount)
print('Thank You for Banking here 😊.')


