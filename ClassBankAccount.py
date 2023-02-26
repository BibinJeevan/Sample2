class BankAc:
    def custdet(self,cname,acno,actype,bal):
        self.cname=cname
        self.acno=acno
        self.actype=actype
        self.bal=bal
    def deposit(self,amt):
        self.bal=self.bal+amt
    def withdraw(self,amt):
        if self.bal<amt:
            return False
        else:
            self.bal=self.bal-amt
    def dispcustdet(self):
        print("Customer Name:",self.cname)
        print("Account No:",self.acno)
        print("Account Type:",self.actype)
        print("Balance:",self.bal)
obj=BankAc
obj.deposit
obj.withdraw
ch=0
while(ch!=5):
        print("*****Bank Account Details*****")
        print("1.Store Customer Details")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Display Customer Details")
        ch=int(input("Enter your choice:"))
        if ch==1:
            cname=input("Enter your Name:")
            acno=int(input("Enter Account no:"))
            actype=input("Enter Account Type:")
            bal=int(input("Enter Opening Amount:"))
            obj.custdet(cname,acno,actype,bal)
        elif ch==2:
            amt=int(input("Enter Deposit Amount:"))
            obj.deposit(amt)
        elif ch==3:
            amt=int(input("Enter Withdraw Amount:"))
            obj.withdraw(amt)
        elif ch==4:
            obj.dispcustdet()
        else:
            print("Invalid Choice!!")
