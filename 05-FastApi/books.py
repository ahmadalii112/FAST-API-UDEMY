from fastapi import Body, FastAPI


app = FastAPI()


#  List of Books
Books = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'Math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'Math'},
]


"""———————————————————Endpoint———————————————————"""
@app.get("/books")
# async def first_api(): // async is optional
def read_all_books():
    return Books



"""—————————— Path Parameters (Dynamic Params)————————"""

#
# @app.get("/books/{dynamic_param}")
# def read_all_books(dynamic_param):
#     return {
#         'dynamic_param': dynamic_param
#     }


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in Books:
        if book.get('title').casefold() == book_title.casefold():
            return book



"""——————————————————Query Parameters  ?———————————————"""


@app.get("/books/category/{category}")
async def read_category_by_book(category: str):
    books_to_return = []
    for book in Books:
        if book.get('category').casefold() == book_title.casefold():
            return books_to_return.append(book)
            
    return books_to_return



"""——————————————————Post Request———————————————"""

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    Books.append(new_book)




"""——————————————————PUT Request———————————————"""

@app.put("/books/update_book")
async def update_book(update_book=Body()):
    for i in range(len(Books)):
        # print(Books[i]) 
        if Books[i].get('title') == update_book.get('title').casefold():
            Books[i] = update_book



"""—————————————————DELETE Request———————————————"""

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == book_title.casefold():
            Books.pop(i)
            break