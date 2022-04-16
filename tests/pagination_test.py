import unittest
from paginator.pagination import Paginator, Page


class PaginatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.object_list = list(range(1, 121))
        self.page_size = 25
        self.paginator = Paginator(self.object_list, self.page_size)
        
        return super().setUp()
    
    def test_validate_page_number(self):
        self.assertTrue(self.paginator.validate_page_number(4))
        with self.assertRaises(IndexError):
            self.assertFalse(self.paginator.validate_page_number(6))
    
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


if __name__ == "__main__":
    unittest.main()