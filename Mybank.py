from PIL import Image;
class ATM(object):
    def __init__(self,number,pincode):
        self.number = number
        self.pincode = pincode
    def Withdraw(self):
        atmnum = input('enter your ATM number: ')
        pin = input('enter 3 digit cvv number: ')
        cash = input('enter the amount to withdraw: ')
        if(atmnum ==''):
            print('please enter your atm number')
        if(pin ==''):
            print('please enter your cvv')
        if(cash ==''):
            print('please enter Amount')
        if(cash !='' and pin !='' and atmnum !=''  ):
            print('Transaction Succesfull!!')
            print('atm number :',atmnum)
            print('Amount:',cash)
            print('Your',cash,'rs. has succesfully transacted')        
       
    def deposit(self):
        atmnum = input('enter your A.C number: ')
        pin = input('enter bank Name: ')
        cash = input('enter the amount : ')
        if(atmnum ==''):
            print('please enter your A.C. number')
        if(pin ==''):
            print('please enter your cvv')
        if(cash ==''):
            print('please enter Amount')            
        if(cash !='' and pin !='' and atmnum !=''  ):
            print('Deposit Succesfull!!')
            print('A.C. number :',atmnum)
            print('Amount:',cash)
            print('Your',cash,'rs. has succesfully deposit to your A.C')   

atm = ATM('','')
option = input("withdraw/deposit: ")
if(option == 'withdraw'):                
    atm.Withdraw()
if(option == 'deposit'):
    atm.deposit()
if(option !='deposit' and option != 'withdraw' ):
    print('our machine has only withdraw or deposit')    