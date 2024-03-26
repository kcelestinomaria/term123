import datetime

class Product: # To buy product
    def __init__(self, product, category,
                date_added=None, date_completed=None,
                status=None, position=None):
        self.product = product
        self.category = category
        self.date_added = date_added if date_added is not None else datetime.datetime.now().isoformat()
        self.date_completed = date_completed if date_completed is not None else None
        self.status = status if status is not None else 1 # 1 = available, 2 = not available
        self.position = position if position is not None else None

    def __repr__(self) -> str:
        return f"({self.product}, {self.category}, {self.date_added}, {self.date_completed}, {self.status}, {self.position})"