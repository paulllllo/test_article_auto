import requests

# Replace it with your actual Token ID
api_key = "241a854602bd18eea1ad67e003d698ad29975b8011b5ebd46f384ba28383f4ee6"

author_id = '1013cac9bd7f6c591449312313663f7e677ba82031b82f05631b0088839ff565f'

post_data = {
    'title': 'My Python-Generated Medium Post',
    'contentFormat': 'markdown',
    'content': 'Hello world!! Just testing the medium api ##This should be a header **This should be bold** and ```this, a code snippet```',
    'publishStatus': 'draft'
}

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Accept-Charset': 'utf-8',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
url = f'https://api.medium.com/v1/users/{author_id}/posts'
response = requests.post(url, json=post_data, headers=headers)
if response.status_code == 201:
    print('Post created and published successfully!')
    # Print the response content for detailed information
    print('Response content:', response.content.decode('utf-8'))
else:
    print('Failed to create post. Status code:',  response.content.decode('utf-8'))

