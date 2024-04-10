import frontmatter

data = frontmatter.load('test_article.md')
print(f'keys***{data.keys()}')
print(f'draft***{data["draft"]}')
print(f'preview***{data["preview"]}')
print(f'content***{data.content}')
