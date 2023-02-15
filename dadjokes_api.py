import requests

DAD_JOKE_URL = r'https://icanhazdadjoke.com/'

def main():
    print(get_random_dad_joke())

def get_random_dad_joke():
    
    #setup the header params
    header = {
        'Accept': 'application/json'
    }
    
    #Send a GET request for a random dad joke
    print('Getting a random dad joke...', end='')
    response = requests.get(DAD_JOKE_URL, headers = header)
    
    #Check whether the request was successful
    if response.ok:
        print('success')
        body_dict = response.json()
        return body_dict['joke']

    else:
        print('failure')
        print(f'Response code {response.status_code} ({response.reason})')
        print(f"Error: {response.text}")
    return

if __name__ == '__main__':
    main()