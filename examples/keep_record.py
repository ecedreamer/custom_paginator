import sqlite3


def get_connection():
    conn = sqlite3.connect("examples/bookdb.sqlite3", isolation_level=None)
    conn.execute('pragma journal_mode=wal')
    conn.execute("create table if not exists book(id integer primary key autoincrement, isbn, title, author, pub_year, publisher, image_url_s, image_url_m, image_url_n) ")
    return conn


def insert_data(conn, dataset):
    conn.executemany("insert into book(isbn, title, author, pub_year, publisher, image_url_s, image_url_m, image_url_n) values(?, ?, ?, ?, ?, ?, ?, ?)", dataset)
    
    
def read_csv(conn):
    with open('examples/books_data.csv', encoding = "ISO-8859-1") as file:
        lines = file.readlines()
        dataset = []
        for index, line in enumerate(lines, start=1):
            data = line.rstrip("\n").split(";")
            if len(data) == 8:
                dataset.append(data)
            if index % 1000 == 0:
                insert_data(conn, dataset)
                dataset = []

    
    
def main():
    conn = get_connection()
    read_csv(conn)
    
    
if __name__ == "__main__":
    main()