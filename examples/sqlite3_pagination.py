import sys
sys.path.append("./")
from math import ceil
import sqlite3
from dataclasses import dataclass
from paginator.pagination import SqlPaginator


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
        return sqlite3.connect("examples/bookdb.sqlite3", isolation_level=None)
    except sqlite3.Error as er:
        sys.exit(1)


def fetch_data(conn, offset=0, limit=25):
    """ gets connection object, offset and limit, executes the query and returns its cursor """
    return conn.execute("SELECT * FROM book ORDER BY id LIMIT ? OFFSET ?", (limit, offset))


def get_paginated_data(conn, page):
    fetched_data = fetch_data(conn, offset=page.offset, limit=page.limit)
    final_result = [BookModel(*row) for row in fetched_data]
    return final_result


def main(paginate_by=100, page_number=1):
    conn = get_connection()
    total_count = conn.execute("SELECT COUNT() from book").fetchone()[0]
    paginator = SqlPaginator(total_count=total_count, page_size=paginate_by)
    page = paginator.page(page_number, db_fetch_func=get_paginated_data, conn=conn)
    print(page.object_list())
    print(len(page.object_list()))
    print(page.has_next_page())


if __name__ == "__main__":
    """ change the following value as desired """
    paginate_by = 100
    page_number = 2495
    main(paginate_by=paginate_by, page_number=page_number)