# # Example 1
#
# books = [
#     {'title': 'Cosmic Python', 'author': 'Harry Persival'},
#     {'title': 'Testing Goat', 'author': 'Harry Persival'},
#     {'title': 'Harry Potter', 'author': 'J. K. Rowling'},
#     {'title': 'Pan Tadeusz', 'author': 'Adam Mickiewicz'},
# ]
#
# for book in books:
#     match book:
#         case {'author': 'Harry Persival', 'title': title}:
#             print(f'\n{book}\n')
#             print(f'\n{title}\n')


# Example 2
# Match all books by author

books = [
    {'title': 'Harry Potter', 'author': 'J. K. Rowling', 'property': {'pages': 350, 'font': 'Arial'}},
    {'title': 'Cosmic Python', 'author': 'Harry Persival', 'property': {'pages': 300, 'font': 'Arial'}},
    {'title': 'Testing Goat', 'author': 'Harry Persival', 'property': {'pages': 500, 'font': 'Arial'}},
    {'title': 'Pan Tadeusz', 'author': 'Adam Mickiewicz', 'property': {'pages': 200, 'font': 'Arial'}},
    {'foo': 'No match'},
]


class Var:
    pass


def match_books_by_author(author, books):
    var = Var()
    var.author = author

    results = []
    for book in books:
        match book:
            case {'author': var.author, 'title': title, 'property': {'pages': pages}}:
                results.append((title, pages))
    return results


print(match_books_by_author('Harry Persival', books))


# Example 3 regex
import re


foo = ['aaaa', '111111', 'a1a1a1a']


class RegexEqual(str):

    def __eq__(self, other):
        return re.fullmatch(other, self)


for i in foo:

    match RegexEqual(i):
        case '\d+': print('Numbers')
        case '\D+': print('Letters')
        case _: print('Something else')