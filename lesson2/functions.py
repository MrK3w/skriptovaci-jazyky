import os

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

def transactions_from_to(bank_accounts,**params):
    reduced_bance_accounts = {}
    min = False
    max = False
    for param in params:
        if param == '_from':
            min = params[param]
        elif param == '_to':
            max = params[param]
    if min == False and max == False:
        return bank_accounts
    elif min == False:
         for bank_account in bank_accounts:
            value = bank_accounts[bank_account]
            if value < max:
                reduced_bance_accounts[bank_account] = value
         return reduced_bance_accounts
    elif max == False:
         for bank_account in bank_accounts:
            value = bank_accounts[bank_account]
            if value > min:
                reduced_bance_accounts[bank_account] = value
         return reduced_bance_accounts
    else:
        for bank_account in bank_accounts:
            value = bank_accounts[bank_account]
            if value > min and value < max:
                reduced_bance_accounts[bank_account] = value
        return reduced_bance_accounts


bank_accounts = bank_transactions("transactions")
print(bank_accounts)
print(transactions_from_to(bank_accounts))





