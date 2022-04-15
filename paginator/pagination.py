import math


class Paginator:
    def __init__(self, object_list, page_size) -> None:
        self.object_list = object_list
        self.page_size = page_size
        self.object_count = len(self.object_list)
        
    def validate_page_number(self, number):
        return number <= self.page_count()
        
        
    def page(self, page_number=1):
        bottom = (page_number-1) * self.page_size
        top = bottom + self.page_size
        return Page(self, self.object_list[bottom:top], page_number)
    
    def page_count(self):
        return math.ceil(self.object_count/self.page_size)
    
    def page_range(self):
        return range(1, self.page_count()+1)
        


class Page:
    def __init__(self, paginator, object_list, page_number) -> None:
        self.paginator = paginator
        self.object_list = object_list
        self.page_number = page_number
        
    
        
    def sliced_object_list(self):
        if self.paginator.validate_page_number(self.page_number):
            return self.object_list
        
    def start_index(self):
        if self.page_number == 1:
            return 1
        start_index = self.paginator.page_size * (self.page_number - 1) + 1
        if start_index > self.paginator.object_count:
            raise IndexError
        return start_index
    
    def end_index(self):
        if self.page_number == 1:
            return self.paginator.page_size
        end_index = self.paginator.page_size * self.page_number
        if self.paginator.object_count > self.start_index() and self.paginator.object_count < end_index:
            return self.paginator.object_count
        elif end_index < self.paginator.object_count:
            return end_index
        else:
            return IndexError
            