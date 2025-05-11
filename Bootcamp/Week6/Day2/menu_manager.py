from menu_item import MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        with MenuItem.connection.cursor() as cursor:
            cursor.execute(
                "SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s;",
                (name,)
            )
            result = cursor.fetchone()

        if result:
            item_name, item_price = result
            return MenuItem(item_name, item_price)
        return None

    @classmethod
    def all_items(cls):
        with MenuItem.connection.cursor() as cursor:
            cursor.execute("SELECT item_name, item_price FROM Menu_Items;")
            results = cursor.fetchall()

        return [MenuItem(name, price) for name, price in results]