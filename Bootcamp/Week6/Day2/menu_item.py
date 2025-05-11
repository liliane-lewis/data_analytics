## 2. In the file menu_item.py, create a new class called MenuItem, the attributes should be the name and price of each item.

class MenuItem:
    connection = None

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        with MenuItem.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s);",
                (self.name, self.price)
            )
        MenuItem.connection.commit()

    def delete(self):
        with MenuItem.connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM Menu_Items WHERE item_name = %s;",
                (self.name,)
            )
        MenuItem.connection.commit()

    def update(self, new_name, new_price):
        with MenuItem.connection.cursor() as cursor:
            cursor.execute(
                "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s;",
                (new_name, new_price, self.name)
            )
        MenuItem.connection.commit()
        self.name = new_name
        self.price = new_price