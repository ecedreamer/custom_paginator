import sys
sys.path.append("./")
from math import ceil
import sqlite3
from dataclasses import dataclass


########################### model class to represent book ######################################
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
    """ connect to sqlite3 database and return connection object """
    try:
        conn = sqlite3.connect("examples/bookdb.sqlite3", isolation_level=None)
        conn.execute('pragma journal_mode=wal')
        conn.execute("create table if not exists book(id integer primary key autoincrement, isbn, title, author, pub_year, publisher, image_url_s, image_url_m, image_url_n) ")
        return conn
    except sqlite3.Error as er:
        sys.exit(1)


def fetch_data(conn, offset=0, limit=25):
    """ gets connection object, offset and limit, executes the query and returns its cursor """
    return conn.execute("SELECT * FROM book ORDER BY id LIMIT ? OFFSET ?", (limit, offset))


def get_pagination_info(total_count, page_size, page_number):
    # calculate start_index
    page_info = {"page_count": ceil(total_count/page_size)}
    page_info["start_index"] = (page_number - 1) * page_size
    page_info["next_page_number"] = page_number + 1 if page_number < page_info["page_count"] else None
    page_info["prev_page_number"] = page_number - 1 if page_number > 1 else None
    return page_info


def get_paginated_data(conn, page_size, page_number):
    # calculate start_index
    total_count = conn.execute("SELECT COUNT() from book").fetchone()[0]
    pagination_info = get_pagination_info(total_count, page_size, page_number)
    # call fetch_data
    fetched_data = fetch_data(conn, offset=pagination_info.get("start_index"), limit=page_size)
    final_result = [BookModel(*row) for row in fetched_data]
    # add the result and return 
    pagination_info["page_size"] = len(final_result)
    pagination_info["object_list"] = final_result
    return pagination_info


def main(paginate_by=100, page_number=1):
    conn = get_connection()
    result = get_paginated_data(conn, paginate_by, page_number)
    print(result)


if __name__ == "__main__":
    """ change the following value as desired """
    paginate_by = 100
    page_number = 2497
    main(paginate_by=paginate_by, page_number=page_number)