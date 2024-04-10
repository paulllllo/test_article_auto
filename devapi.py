import frontmatter
import requests


#Print frontmatter content
data = frontmatter.load('test_article.md')

# Replace it with your actual Token ID
api_key = "HRAda2o8Fxziq2w33kFJpraY"

post_data = {
    "article": {
        "title": data['title'],
        "published": False,
        "body_markdown": data.content,
        "tags": [],
        "series": ""
    }
}

headers = {
    'api-key': api_key,
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Accept-Charset': 'utf-8',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
url = 'https://dev.to/api/articles'
response = requests.post(url, json=post_data, headers=headers)
if response.status_code == 201:
    print('Post created and published successfully!')
    # Print the response content for detailed information
   # print('Response content:', response.content.decode('utf-8'))
else:
    print('Failed to create post. Status code:',  response.content.decode('utf-8'))

