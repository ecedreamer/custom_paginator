import sys
sys.path.append("./")
from math import ceil
import sqlite3
from dataclasses import dataclass


@dataclass
class BookModel:
    id: int
    isbn: str
    title: str
    author: str
    published_year: str
    publisher: str
    image_url_s: str
    image_url_m: str
    image_url_n: str
    
    


def get_connection():
    conn = sqlite3.connect("examples/bookdb.sqlite3", isolation_level=None)
    conn.execute('pragma journal_mode=wal')
    conn.execute("create table if not exists book(id integer primary key autoincrement, isbn, title, author, pub_year, publisher, image_url_s, image_url_m, image_url_n) ")
    return conn


def fetch_data(conn, offset=0, limit=25):
    return conn.execute("SELECT * FROM book ORDER BY id LIMIT ? OFFSET ?", (limit, offset))


def get_paginated_data(conn, page_size, page_number):
    # calculate start_index
    count = conn.execute("SELECT COUNT() from book").fetchone()[0]
    page_count = ceil(count/page_size)
    start_index = (page_number - 1) * page_size
    # call fetch_data
    fetched_data = fetch_data(conn, offset=start_index, limit=page_size)
    final_result = [BookModel(*row) for row in fetched_data]
    # return data
    return {"page_count": page_count, "start_index": start_index, "page_number": page_number, "object_list": final_result, "object_count": len(final_result)}


def main(paginate_by=100, page_number=1):
    conn = get_connection()
    result = get_paginated_data(conn, paginate_by, page_number)
    print(result)
    print(len(result["object_list"][0].published_year))


if __name__ == "__main__":
    paginate_by = 100
    page_number = 25
    main(paginate_by=paginate_by, page_number=page_number)