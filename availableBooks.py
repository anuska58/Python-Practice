books = ['i dont love you any more','atomic habits', 'the book thief']

searchBook= input("Enter name of the book you want to search: ").lower()
if searchBook in books:
    print('The book is available')
else:
    print('Unfortunately, the book is not available currently.')
