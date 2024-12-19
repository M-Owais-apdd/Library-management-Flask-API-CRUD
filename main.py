# app.py

from flask import Flask, jsonify, request
from models import books, members, Book, Member
from auth import token_required

app = Flask(__name__)

# CRUD for Books
@app.route('/books', methods=['GET'])
def get_books():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    start = (page - 1) * per_page
    end = start + per_page
    return jsonify(books[start:end])

@app.route('/books', methods=['POST'])
@token_required
def add_book():
    data = request.json
    new_book = Book(id=len(books) + 1, title=data['title'], author=data['author'])
    books.append(new_book)
    return jsonify({'message': 'Book added!'}), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
@token_required
def update_book(book_id):
    data = request.json
    for book in books:
        if book.id == book_id:
            book.title = data['title']
            book.author = data['author']
            return jsonify({'message': 'Book updated!'})
    return jsonify({'message': 'Book not found!'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
@token_required
def delete_book(book_id):
    global books
    books = [book for book in books if book.id != book_id]
    return jsonify({'message': 'Book deleted!'})

@app.route('/books/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '')
    results = [book for book in books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
    return jsonify(results)

# CRUD for Members
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(members)

@app.route('/members', methods=['POST'])
@token_required
def add_member():
    data = request.json
    new_member = Member(id=len(members) + 1, name=data['name'])
    members.append(new_member)
    return jsonify({'message': 'Member added!'}), 201

@app.route('/members/<int:member_id>', methods=['PUT'])
@token_required
def update_member(member_id):
    data = request.json
    for member in members:
        if member.id == member_id:
            member.name = data['name']
            return jsonify({'message': 'Member updated!'})
    return jsonify({'message': 'Member not found!'}), 404

@app.route('/members/<int:member_id>', methods=['DELETE'])
@token_required
def delete_member(member_id):
    global members
    members = [member for member in members if member.id != member_id]
    return jsonify({'message': 'Member deleted!'})

if __name__ == '__main__':
    app.run(debug=True)