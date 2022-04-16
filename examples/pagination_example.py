import sys

sys.path.append("./")

import sqlite3
from paginator.pagination import Paginator



def get_connection():
    return sqlite3.connect("examples/bookdb.sqlite3")


def fetch_data(conn, limit=25):
    return conn.execute("SELECT * FROM book ORDER BY id").fetchall()


def get_paginated_data(conn, paginate_by):
    object_list = fetch_data(conn)
    return Paginator(object_list, paginate_by)


def main(paginate_by, page_number):
    conn = get_connection()
    paginator_obj = get_paginated_data(conn, paginate_by)
    page = paginator_obj.page(page_number)
    print("Object Count: ", len(page.object_list()))
    print("Total Page: ", paginator_obj.page_count())
    print("Data: ", page.object_list())


if __name__ == "__main__":
    paginate_by = 100
    page_number = 2497
    main(paginate_by, page_number)
