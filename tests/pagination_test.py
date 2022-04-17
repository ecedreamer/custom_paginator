import unittest
from paginator.pagination import Paginator, Page, SqlPaginator, SqlPage


class PaginatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.object_list = list(range(1, 121))
        self.page_size = 25
        self.paginator = Paginator(self.object_list, self.page_size)
        
        return super().setUp()
    
    def test_validate_page_number(self):
        self.assertTrue(self.paginator.validate_page_number(4))
        self.assertTrue(self.paginator.validate_page_number(1))
        with self.assertRaises(TypeError):
            self.paginator.validate_page_number(3.4)
        with self.assertRaises(IndexError):
            self.paginator.validate_page_number(6)
    
    def test_page_count(self):
        self.assertEqual(self.paginator.page_count(), 5)
        
    def test_page_range(self):
        self.assertEqual(self.paginator.page_range(), range(1, 6))
    
    def tearDown(self) -> None:
        return super().tearDown()


class PageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.object_list = list(range(1, 121))
        self.page_size = 25
        self.paginator = Paginator(self.object_list, self.page_size)
        self.page1 = Page(self.paginator, self.object_list[:25], 1)
        self.page2 = Page(self.paginator, self.object_list[25:50], 2)
        self.page3 = Page(self.paginator, self.object_list[50:75], 3)
        self.page4 = Page(self.paginator, self.object_list[75:100], 4)
        self.page5 = Page(self.paginator, self.object_list[100:125], 5)
        return super().setUp()
    
    def test_invalid_page(self):
        with self.assertRaises(IndexError):
            self.page6 = Page(self.paginator, self.object_list[125:150], 6)
    
    def test_start_index(self):
        self.assertEqual(self.page1.start_index(), 1)
        self.assertEqual(self.page2.start_index(), 26)
        self.assertEqual(self.page3.start_index(), 51)
        self.assertEqual(self.page4.start_index(), 76)
        self.assertEqual(self.page5.start_index(), 101)
        
    def test_end_index(self):
        self.assertEqual(self.page1.end_index(), 25)
        self.assertEqual(self.page2.end_index(), 50)
        self.assertEqual(self.page3.end_index(), 75)
        self.assertEqual(self.page4.end_index(), 100)
        self.assertEqual(self.page5.end_index(), 120)
            
    def test_object_list(self):
        self.assertEqual(len(self.page1.object_list()), 25)
        self.assertEqual(len(self.page5.object_list()), 20)
        
    def test_has_next_page(self):
        self.assertTrue(self.page1.has_next_page())
        self.assertFalse(self.page5.has_next_page())
        
    def test_has_prev_page(self):
        self.assertFalse(self.page1.has_previous_page())
        self.assertTrue(self.page5.has_previous_page())
    
    def tearDown(self) -> None:
        return super().tearDown()


class SqlPaginatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.total_count = 120
        self.page_size = 25
        self.paginator = SqlPaginator(self.total_count, self.page_size)
        
        return super().setUp()
    
    def test_validate_page_number(self):
        self.assertTrue(self.paginator.validate_page_number(4))
        self.assertTrue(self.paginator.validate_page_number(1))
        with self.assertRaises(TypeError):
            self.paginator.validate_page_number(3.4)
        with self.assertRaises(IndexError):
            self.paginator.validate_page_number(6)
    
    def test_page_count(self):
        self.assertEqual(self.paginator.page_count(), 5)
        
    def test_page_range(self):
        self.assertEqual(self.paginator.page_range(), range(1, 6))
    
    def tearDown(self) -> None:
        return super().tearDown()


class SqlPageTest(unittest.TestCase):
    def mocked_db_fetch_func(self, page):
        if page.page_number == 1:
            return list(range(1, 26))
        elif page.page_number == 2:
            return list(range(26, 51))
        elif page.page_number == 3:
            return list(range(51, 76))
        elif page.page_number == 4:
            return list(range(76, 101))
        elif page.page_number == 5:
            return list(range(101, 121))
        return []
    
    def setUp(self) -> None:
        self.total_count = 120
        self.page_size = 25
        self.paginator = SqlPaginator(self.total_count, self.page_size)
        self.page1 = SqlPage(self.paginator, 1, self.mocked_db_fetch_func)
        self.page2 = SqlPage(self.paginator, 2, self.mocked_db_fetch_func)
        self.page3 = SqlPage(self.paginator, 3, self.mocked_db_fetch_func)
        self.page4 = SqlPage(self.paginator, 4, self.mocked_db_fetch_func)
        self.page5 = SqlPage(self.paginator, 5, self.mocked_db_fetch_func)
        return super().setUp()
    
    def test_limit(self):
        self.assertEqual(self.page1.limit, 25)
        self.assertEqual(self.page5.limit, 25)
    
    def test_offset(self):
        self.assertEqual(self.page1.offset, 0)
        self.assertEqual(self.page2.offset, 25)
        self.assertEqual(self.page3.offset, 50)
        self.assertEqual(self.page4.offset, 75)
        self.assertEqual(self.page5.offset, 100)
    
    def test_start_index(self):
        self.assertEqual(self.page1.start_index(), 1)
        self.assertEqual(self.page2.start_index(), 26)
        self.assertEqual(self.page3.start_index(), 51)
        self.assertEqual(self.page4.start_index(), 76)
        self.assertEqual(self.page5.start_index(), 101)
        
    def test_end_index(self):
        self.assertEqual(self.page1.end_index(), 25)
        self.assertEqual(self.page2.end_index(), 50)
        self.assertEqual(self.page3.end_index(), 75)
        self.assertEqual(self.page4.end_index(), 100)
        self.assertEqual(self.page5.end_index(), 120)
            
    def test_has_next_page(self):
        self.assertTrue(self.page1.has_next_page())
        self.assertFalse(self.page5.has_next_page())
        
    def test_has_prev_page(self):
        self.assertFalse(self.page1.has_previous_page())
        self.assertTrue(self.page5.has_previous_page())
        
    def test_object_list(self):
        self.assertEqual(len(self.page1.object_list()), 25)
        self.assertEqual(len(self.page5.object_list()), 20)
    
    def tearDown(self) -> None:
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()