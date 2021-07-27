import requests
import hashlib
from os import system, name


def clear():
    # For Windows
    if name == 'nt':
        _ = system('cls')
    # For Linux/Mac
    else:
        _ = system('clear')

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.status_code} , check the api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5] , sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(args):
        count = pwned_api_check(args)
        if count:
            print(f'{args} was found {count} times... You should probably change your password.')
        else:
            print(f'{args} was NOT found. Carry on!')

        print('\n Would you like to check different password?      (Y/N)')
        ans = input('--->')
        if ans == 'y' or ans == 'Y':
            startProgram()
        elif ans == 'n' or ans == 'N':
            exit()
        else:
            print('Invalid command')


def startProgram():
    clear()
    print('===================[CheckMyHash]==========================')
    print('How to use:')
    print('Insert your password and the program will check how many times you password has been used.')
    print('===================[CheckMyHash]==========================')
    ans = input('\nCheck your password: ')
    main(ans)

startProgram()