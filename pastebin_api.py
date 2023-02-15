import requests

POST_URL = r'https://pastebin.com/api/api_post.php'
DEV_API_KEY = 't4t79PqqCtjT36nc9G_HWfcEHJN-qPyR'

def main():
    paste_url = post_new_paste('Fortnite', 'Big Hamburger')


def post_new_paste(title, body_text, expiration='10M', listed=True, print_url=False):
    """Creates a new Pastebin paste

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str, optional): How long the paste will last. Defaults to '10M'.
        listed (bool, optional): Determines if the paste is listed or unlisted. Defaults to True.

    Returns:
        str: URL of the created paste. None if unsuccessful
    """
    
    #create dictionary of param values

    params = {
        'api_dev_key' : DEV_API_KEY,
        'api_option' : 'paste',
        'api_paste_code' : body_text,
        'api_paste_expire_date' : expiration,
        'api_paste_name' : title,
        'api_paste_private' : 0 if listed else 1
    }


    #Send the POST request to the PasteBin API
    print("Posting new paste to PasteBin...", end='')
    print(body_text)
    response = requests.post(POST_URL, data = params)

    #Check if paste was successful
    if response.status_code == requests.codes.ok:
        print('success')
        if print_url is True:
            print(f'URL of new paste: {response.text}')
        return response.text
    else:
        print('failure')
        print(f'Response code {response.status_code} ({response.reason})')
        print(f"Error: {response.text}")

    #My key t4t79PqqCtjT36nc9G_HWfcEHJN-qPyR
if __name__ == '__main__':
    main()