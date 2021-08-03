from account import Account

def main():
    #write your code below this line
    matt_account = Account("Matthews account", 1000)
    my_account = Account("My account", 0)

    matt_account.withdraw(100)
    my_account.deposit(100)

    print(matt_account)
    print(my_account)

if __name__ == '__main__':
    main()
