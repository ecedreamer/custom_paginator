This paginator module accepts user input object_list, page_size and page_number and gives paginated result.

** Usage ** 
    ** Normal Paginator class **
    # import module 
    from paginator.pagination import Paginator

    # make paginator object
    paginator = Paginator(object_list, paginate_by)  # object_list is list type which will be sliced and paginate_by is the page size integer

    # get page range
    page_range = paginator.page_range()

    # request for specific page
    page = paginator.page(page_number) # page number is integer between page_range 

    # get paginated data
    result = page.object_list()

    ** SqlPaginator class **
    from paginator.pagination import SqlPaginator

    # make paginator object
    paginator = Paginator(total_count, paginate_by)  # total_count is count of total objects in the db table and paginate_by is the page size integer

    # get page range
    page_range = paginator.page_range()

    # request for specific page
    page = paginator.page(page_number, db_fetch_func, kwargs_of_db_fetch_function) # arguments needed for db_fetch_function except page argument

    # get paginated data
    result = page.object_list()

To know usase, please view two examples in the example folder. 
    * pagination_example.py 
    * sqlite3_pagination.py

TO RUN EXAMPLES

$ python examples/pagination_example.py
$ python examples/sqlite3_pagination.py

TO RUN TESTS

$ pytest tests