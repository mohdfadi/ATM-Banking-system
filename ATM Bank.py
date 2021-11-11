
class ATM():
   
    def __init__(self):
        self.balance = 10000
        self.savings = 13000

    def choices(self):
        print('_________Welcom to BANK OF FADHI(BOF)__________')
        choice  = int(input(
            '1.deposite\n'
            '2.withdraw\n'
            '3.savings\n'
            '4.enquiry\n'
            'enter: '
        ))

        if choice == 1:
            self.deposit()
        elif choice == 2:
            self.withdraw()
        elif choice == 4:
            self.enquiry()
        
        elif choice == 3:
            self.from_savings()

        else:   
            print('Invalid Input')

    def deposit(self):

        pincode = int(input('Enter 4 Digit PIN: :'))
        if pincode == 1234:
            amount = int(input('enter amount  to deposite:  '))
            self.balance = self.balance + amount
            print('Deposit successful. balance is\n 'u'\u20B9%i'% self.balance)
        
        else:
            print("Invalid PIN")

    def withdraw(self):

        pincode = int(input('Enter 4 Digit PIN: '))
        if pincode == 1234:
            amount = int(input('enter amount  to withdraw:  '))
            if amount > self.balance:
                print('Insufficient Balance')   
                 
            else:   
                self.balance = self.balance - amount      
                print('Withdraw successful. balance is\n 'u'\u20B9%i'% self.balance)
        else:
            print('invalid PIN')


    def from_savings(self):
        pincode =int(input('Enter 4 DIGIT PIN: '))
        if pincode == 1234:
            amount = int(input('Enter amount: '))
            if amount > self.savings:
                print('Insufficient Balance')
            
            else:
                self.savings =self.savings - amount
                print('Transaction Successful. your savings is\n 'u'\u20B9%i'% self.savings)

        else:
            print('Invalid PIN')
        



    def enquiry(self): 
        pincode =int(input('Enter 4 Digit PIN: '))
        if pincode == 1234:
            check = input('Do you want to check balance?\n1.yes\n2.no\nEnter: ')
            if check == 'yes':
                 print('your balance. is\n 'u'\u20B9%i'% self.balance)
            else:
                print('Thank you')
        else:
            print('Invalid PIN')

    
close = ATM()
while True:
    close.choices()
    choice_2 = int(input('To Continue, Press 1\nTo Stop, Press 2 \nENTER: '))
    if choice_2 == 1:
        continue  
    elif choice_2 == 2: 
        print('Thank you')
        break



         