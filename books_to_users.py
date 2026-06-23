import csv
import json


def distribute_books():
    books = []
    with open('books.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            books.append({
                "title": row['Title'],
                "author": row['Author'],
                "pages": int(row['Pages']),
                "genre": row['Genre']
            })

    with open('users.json', 'r', encoding='utf-8') as f:
        users = json.load(f)

    result = []
    for user in users:
        result.append({
            "name": user['name'],
            "gender": user['gender'],
            "address": user['address'],
            "age": user['age'],
            "books": []
        })

    books_per_user = len(books) // len(result)
    remaining = len(books) % len(result)

    book_index = 0
    for i, user in enumerate(result):
        count = books_per_user + (1 if i < remaining else 0)
        user['books'] = books[book_index:book_index + count]
        book_index += count

    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    distribute_books()
