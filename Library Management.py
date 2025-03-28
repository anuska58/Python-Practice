book_numbers = int(input("Enter the total number of books:"))

avg_book_rating = float(input("Enter the average book  rating: "))

librarian_name = input("Enter the name of the librarian: ")

isLibraryOpen = True

book_names = ['new moon', 'the book thief', 'a man called ove']

location = (2.00, 'New Road', 33700, 'Kaski', 'Nepal')

contact_detail = {
    'phone number': int(input('enter phone number')),
    'email id': input('enter your email id')
}
unique_genres = {'fiction', 'sci-fi', 'thrilling'}

print("")
print("")
print("")
print("Library Information")
print(f"Total number of books:{book_numbers}")
print(f"Average book rating: {avg_book_rating}")
print(f"Name of Librarian: {librarian_name}")
print(f"Is library open now? {'Yes' if isLibraryOpen else 'No'}")
print(f"Location Coordinates: {location}")
print(f"Contact Details: {contact_detail}")
print(f"Unique Genres: {unique_genres}")


