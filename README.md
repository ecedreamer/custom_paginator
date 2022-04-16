This paginator module accepts user input object_list, page_size and page_number and gives paginated result.

There are two examples here. One example is using this module. In case of large data fetching from database, processing will be slower so if you want fast result, check the sqlite3_pagination.py which does not use this paginator module but gives idea how you can implement inside database query. 

TO RUN EXAMPLES

$ python examples/pagination_example.py

TO RUN TESTS

$ pytest tests