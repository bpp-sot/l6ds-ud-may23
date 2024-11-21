-- SQL Tables for an e-commerce order system
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    ShippingAddress VARCHAR(255),
    Status VARCHAR(50),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    UnitPrice DECIMAL(10,2),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

CREATE TABLE OrderStatusHistory (
    HistoryID INT PRIMARY KEY,
    OrderID INT,
    Status VARCHAR(50),
    UpdateDate DATETIME,
    UpdatedBy VARCHAR(100),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Example data
INSERT INTO Orders VALUES (1001, 5432, '2024-03-15', '123 Main St, City, Country', 'Delivered');
INSERT INTO OrderItems VALUES (1, 1001, 101, 2, 29.99);
INSERT INTO OrderItems VALUES (2, 1001, 102, 1, 49.99);
INSERT INTO OrderStatusHistory VALUES (1, 1001, 'Pending', '2024-03-15 10:00:00', 'System');
INSERT INTO OrderStatusHistory VALUES (2, 1001, 'Processing', '2024-03-15 10:30:00', 'John');
INSERT INTO OrderStatusHistory VALUES (3, 1001, 'Shipped', '2024-03-16 09:00:00', 'Mary');
INSERT INTO OrderStatusHistory VALUES (4, 1001, 'Delivered', '2024-03-17 14:00:00', 'Courier');
