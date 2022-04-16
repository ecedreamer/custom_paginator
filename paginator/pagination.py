import math


class Paginator:
    """ This is a pagination class that accepts object list and page size to provide pagination interface """
    def __init__(self, object_list, page_size) -> None:
        self.object_list = object_list
        self.page_size = page_size
        self.object_count = len(self.object_list)
        
    def validate_page_number(self, number):
        if number <= self.page_count() and number > 0:
            return number
        else:
            raise IndexError
        
    def page(self, page_number=1):
        page_number = self.validate_page_number(page_number)
        bottom = (page_number-1) * self.page_size
        top = bottom + self.page_size
        return Page(self, self.object_list[bottom:top], page_number)
    
    def page_count(self):
        return math.ceil(self.object_count/self.page_size)
    
    def page_range(self):
        return range(1, self.page_count()+1)
        

class Page:
    def __init__(self, paginator: Paginator, object_list, page_number) -> None:
        self.paginator = paginator
        self._object_list = object_list
        self.page_number = self.paginator.validate_page_number(page_number)
        
    def object_list(self):
        return self._object_list
        
    def start_index(self):
        return self.paginator.page_size * (self.page_number - 1) + 1
    
    def has_next_page(self):
        return self.page_number < self.paginator.page_count()
    
    def has_previous_page(self):
        return self.page_number > 1
    
    def next_page_number(self):
        return self.paginator.validate_page_number(self.page_number + 1)
    
    def previous_page_number(self):
        return self.paginator.validate_page_number(self.page_number - 1)
            
    def end_index(self):
        end_index = self.paginator.page_size * self.page_number
        if len(self._object_list) < self.paginator.page_size:
            return self.paginator.page_size * (self.page_number - 1) + len(self._object_list)
        else:
            return end_index