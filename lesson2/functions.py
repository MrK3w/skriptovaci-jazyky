import os
#task1

def interval(my_function,_from,_step,_to):
    list_of_steps = []
    while _from <= _to:
        list_of_steps.append(my_function(_from))
        _from += _step
    return (round(min(list_of_steps)),max(list_of_steps))


#task 2
def bank_transactions(*paths):
    bank_accounts_dictionary = {}
    for path in paths:
        dir_name = ''.join(path)
        if os.path.exists(dir_name):
            files_in_directory = os.listdir(dir_name)
            for file_name in files_in_directory:
                file = open(dir_name+'/'+file_name,'r')
                for line_in_file in file:
                    line_in_file = line_in_file.rstrip()
                    #account operation amount
                    transaction = [x for x in line_in_file.split(' ')]
                    transaction[2] = int(transaction[2])
                    if transaction[0] in bank_accounts_dictionary:
                        if transaction[1] == 'D':
                            bank_accounts_dictionary[transaction[0]] += transaction[2]
                        elif transaction[1] == 'W':
                            bank_accounts_dictionary[transaction[0]] -= transaction[2]
                    else:
                        if transaction[1] == 'D':
                            bank_accounts_dictionary[transaction[0]] = transaction[2]
                        else: 
                            print("Error cannot withdraw from not existing account!")
                for transaction in bank_accounts_dictionary:
                    bank_accounts_dictionary[transaction] *= 1.05
                file.close()
    return bank_accounts_dictionary

#task3
def erase_accounts_which_overlapped_limit(bank_accounts,**params):
    bad_accounts = []
    if '_from' in params:
        value = params['_from']
        for bank_account in bank_accounts:
            if bank_accounts[bank_account] < value:
                bad_accounts.append(bank_account)
    if '_to' in params:
        value = params['_to']
        for bank_account in bank_accounts:
            if bank_accounts[bank_account] > value:
                  bad_accounts.append(bank_account)
    for account in bad_accounts:
        bank_accounts.pop(account)
    return bank_accounts

print(interval(lambda x: x**2,-2,0.5,2))
bank_accounts = bank_transactions("transactions")
print(bank_accounts)
print(erase_accounts_which_overlapped_limit(bank_accounts,_from=5000,_to=8000))





