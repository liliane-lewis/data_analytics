import psycopg2
from menu_item import MenuItem
from menu_manager import MenuManager


connection = psycopg2.connect(
    dbname="restaurant_db",
    user="postgres",
    password="P0st2o25",
    #password="your_password",
    host="localhost",
    port="5432"
)


MenuItem.connection = connection

item = MenuItem('Burger', 35)
item.save()
item.update('Veggie Burger', 60)
item.delete()

item2 = MenuManager.get_by_name('Beef')
if item2:
    print(f"{item2.name} - {item2.price}")
else:
    print("Item not found")

items = MenuManager.all()
for i in items:
    print(f"{i.name} - {i.price}")
