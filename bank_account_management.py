def read_accounts(file_path: str) -> dict:
    accounts = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            account_number, balance = line.strip().split(',')
            accounts[account_number] = float(balance)
    return accounts

def write_accounts(file_path: str, accounts: dict):
    with open(file_path, 'w') as file:
        for account_number, balance in accounts.items():
            file.write(f"{account_number},{balance}\n")

def get_balance(account_number: str) -> float:
    accounts = read_accounts('accounts.txt')
    return accounts.get(account_number, 0.0)

def deposit(account_number: str, amount: float):
    accounts = read_accounts('accounts.txt')
    accounts[account_number] = accounts.get(account_number, 0.0) + amount
    write_accounts('accounts.txt', accounts)

def withdraw(account_number: str, amount: float):
    accounts = read_accounts('accounts.txt')
    if accounts.get(account_number, 0.0) >= amount:
        accounts[account_number] -= amount
    else:
        print("Insufficient funds")
    write_accounts('accounts.txt', accounts)

def update_account(account_number: str, balance: float):
    accounts = read_accounts('accounts.txt')
    accounts[account_number] = balance
    write_accounts('accounts.txt', accounts)

# Example:
if __name__ == "__main__":
    #testing
    print("Initial balance:", get_balance("123456"))
    deposit("123456", 100.0)
    print("Balance after deposit:", get_balance("123456"))
    withdraw("123456", 50.0)
    print("Balance after withdrawal:", get_balance("123456"))
