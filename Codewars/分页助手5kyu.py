class PaginationHelper:
    
    def __init__(self, collection, items_per_page):
        self.items_per_page = items_per_page
        self.collection = collection


    def item_count(self):
        return len(self.collection)

    def page_count(self):
        i = int(PaginationHelper.item_count(self) / self.items_per_page)
        j = int(PaginationHelper.item_count(self) % self.items_per_page)
        if j == 0:
            return i
        return i + 1

    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= PaginationHelper.page_count(self):
            return -1
        if page_index == PaginationHelper.page_count(self) - 1:
            return PaginationHelper.item_count(self) - page_index * self.items_per_page
        return self.items_per_page

    def page_index(self, item_index):
        if item_index < 0 or item_index >= PaginationHelper.item_count(self):
            return -1
        return int(item_index / self.items_per_page)


helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print(helper.page_count())
print(helper.item_count())
print(helper.page_item_count(0))
print(helper.page_item_count(1)) 
print(helper.page_item_count(2))

print(helper.page_index(5))
print(helper.page_index(2))
print(helper.page_index(20))
print(helper.page_index(-10))