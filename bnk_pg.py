accounts={}

def create_account():
  acc_no=input("enter account number")
  if acc_no in accounts:
    print("account already exists")
    return

  name=input("enter account holder name")
  balance=float(input("enter initial deposit"))

  accounts[acc_no]={
    "name":name,
    "balance":balance
}
  print("account created successfully")

def deposit():
  acc_no=input("enter account number:")
  if acc_no not in accounts:
        print("account not found")
        return

  amount=float(input("enter deposit amount:"))
  accounts[acc_no]["balance"]+=amount
  print("deposit successful")

def withdraw():
  acc_no=input("enter account number:")
  if acc_no not in accounts:
        print("account not found")
        return
  amount=float(input("enter withdrawal amount"))

  if amount > accounts[acc_no]["balance"]:
    print("insufficient balance")
    return
  else:
    accounts[acc_no]["balance"]-=amount
    print("withdrawal successful")

def checkbalance():
  acc_no=input("enter account number:")

  if acc_no not in accounts:
    print("account not found")
    return

  print("account holder:",accounts[acc_no]["name"])
  print("account balance:",accounts[acc_no]["balance"])


while True:
  print("1.create account")
  print("2.deposit")
  print("3.withdraw")
  print("4.check balance")
  print("5.exit")

  choice=input("enter your choice:")

  if choice=="1":
    create_account()
  elif choice=="2":
    deposit()
  elif choice=="3":
    withdraw()
  elif choice=="4":
    checkbalance()
  elif choice=="5":
    break
  else:
    print("invalid choice")
