import sys

sys.path.append("./")

import sqlite3
from paginator.pagination import Paginator



def get_connection():
    conn = sqlite3.connect("examples/bookdb.sqlite3", isolation_level=None)
    conn.execute('pragma journal_mode=wal')
    conn.execute("create table if not exists book(id integer primary key autoincrement, isbn, title, author, pub_year, publisher, image_url_s, image_url_m, image_url_n) ")
    return conn


def fetch_data(conn, limit=25):
    return conn.execute("SELECT * FROM book ORDER BY id").fetchall()


def get_paginated_data(conn, paginate_by):
    object_list = fetch_data(conn)
    return Paginator(object_list, paginate_by)


def main():
    conn = get_connection()
    paginator_obj = get_paginated_data(conn, 100)
    page = paginator_obj.page(25)
    print("Object Count: ", len(page.object_list()))
    print("Total Page: ", paginator_obj.page_count())


if __name__ == "__main__":
    main()
