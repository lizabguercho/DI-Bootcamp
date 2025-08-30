import math

class Pagination:
    def __init__(self,items = None, page_size = 10):
        if items == None: 
            self.items = []
        else:
            self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_num_page = math.ceil(len(self.items)/self.page_size)

    def get_visible_items(self):
        visible_items = self.items[
            self.page_size * self.current_idx:
            self.page_size * self.current_idx + self.page_size
            ]
        return visible_items


    def go_to_page(self,page_num):
        if self.total_num_page == 0:
            raise ValueError ("No pages available")            

        if page_num < 1:
            page_num = 1
            print("Page number is lower than 1. Will proceed to go to page 1")
        elif page_num > self.total_num_page:
            page_num = self.total_num_page
            print(f"Page number is greater than total number of pages ({self.total_num_page}). Will proceed to go to page {self.total_num_page}")
        self.current_idx = page_num - 1
        return self.get_visible_items()
             
    def first_page(self):
        return self.go_to_page(1)
        
    
    def last_page(self):
        return self.go_to_page(self.total_num_page)  
      

    def next_page(self):
        if self.current_idx + 1 < self.total_num_page:
             self.current_idx += 1
        return self.get_visible_items()

    def previous_page(self):
        if self.current_idx > 0:
             self.current_idx -= 1
        return self.get_visible_items()   

    def __str__(self) -> str:
          current_items = self.get_visible_items()
          return "\n".join(str(item) for item in current_items)


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(p.get_visible_items())
p.next_page()
print(p.get_visible_items())
p.last_page()
print(p.get_visible_items())
p.go_to_page(10)
print(p.current_idx + 1)
p.go_to_page(0)





