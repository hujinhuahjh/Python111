# TODO: complete this class

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.items_per_page = items_per_page
        self.collection = collection

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        i = int(PaginationHelper.item_count(self) / self.items_per_page)
        j = int(PaginationHelper.item_count(self) % self.items_per_page)
        if j == 0:
            return i
        return i + 1

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= PaginationHelper.page_count(self):
            return -1
        if page_index == PaginationHelper.page_count(self) - 1:
            return PaginationHelper.item_count(self) - page_index * self.items_per_page
        return self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index >= PaginationHelper.item_count(self):
            return -1
        return int(item_index / self.items_per_page)
