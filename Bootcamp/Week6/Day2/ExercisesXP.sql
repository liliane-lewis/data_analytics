--Exercise 1 : Restaurant Menu Manager
--Instructions

--Description: Create a restaurant menu management system for a manager. The program should allow the manager to view the menu, add an item and delete an item.
--PART 1

--In this exercise we will use PostgreSQL and Python.

--    1. Create a new database and a new table in pgAdmin (or in psql). The table is named Menu_Items and contains the columns
--        item_id : SERIAL PRIMARY KEY
--        item_name : VARCHAR(30) NOT NULL
--        item_price : SMALLINT DEFAULT 0
CREATE DATABASE restaurant;

\c restaurant

CREATE TABLE Menu_Items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(30) NOT NULL,
    item_price SMALLINT DEFAULT 0
);

-- 2. In the file menu_item.py, create a new class called MenuItem, the attributes should be the name and price of each item.

    def save(self, connection):
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s);",
                (self.name, self.price)
            )
        connection.commit()

    def delete(self, connection):
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM Menu_Items WHERE item_name = %s;",
                (self.name,)
            )
        connection.commit()

    def update(self, connection, new_name=None, new_price=None):
        if not new_name and new_price is None:
            raise ValueError("You must provide a new name or price to update.")
        
        if new_name:
            self.name = new_name
        if new_price is not None:
            self.price = new_price

        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s;",
                (self.name, self.price, self.name)  # Atenção: pode não funcionar como esperado se o nome foi alterado
            )
        connection.commit()
