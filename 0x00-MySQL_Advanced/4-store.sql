-- Write a SQL script that creates a trigger that
-- decreases the quantity of an item after adding a new order.
-- Quantity in the table items can be negative
-- Change the delimiter to avoid conflicts
DELIMITER //
-- Change the delimiter to avoid conflicts
CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	-- Decrease the quantity by the quantity ordered
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END//

-- Reset the delimiter
DELIMITER ;
