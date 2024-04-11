with open('test_copy', 'r') as f:
    str = f.read()

with open('test_copy', 'w') as f:
    str = str.replace('{% embed', '')
    str = str.replace('%}', '')
    f.write(str)

print('check')
