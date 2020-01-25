# MySQL Solutions

## Question 5

### part a)

> Return the names of all salespeople that have an order with George

```sql
SELECT
  DISTINCT s.name
from
  Salesperson as s
  JOIN orders as o ON s.salespersonID = o.salespersonID
  JOIN Customer as c ON o.customerID = c.customerID
WHERE
  LOWER(c.name) = 'george'
```

### part b)

> Return the names of all salespeople that do not have any order with George

```sql
SELECT
  DISTINCT s.name
FROM
  Salesperson as s
  JOIN orders as o ON s.salespersonID = o.salespersonID
WHERE
  o.salespersonID not in (
    SELECT
      s1.salespersonID
    FROM
      Salesperson AS s1
      JOIN orders o1 ON s1.salespersonID = o1.salesPersonID
      JOIN Customer c ON c.customerId = o1.customerId
    WHERE
      LOWER(c.name) = 'george'
  )
```

### part c)

> Return the names of salespeople that have 2 or more orders.

```sql
WITH s1 AS (
  SELECT
    salespersonID,
    COUNT(*) AS c
  FROM
    Orders
  GROUP BY
    salespersonID
  HAVING
    c >= 2
)
SELECT
  s.name
FROM
  Salesperson AS s
  JOIN s1 ON s.SalespersonID = s1.SalespersonID
```

## Question 6

### part a)

> Return the name of the salesperson with the 3rd highest salary.

```sql
SELECT
  name
FROM
  salesperson
ORDER BY
  Salary DESC
LIMIT
  1
OFFSET 2
```

### part b)

> Create a new roll-up table BigOrders(where columns are CustomerID, TotalOrderValue), and insert into that table customers whose total Amount across all orders is greater than 1000

```sql
CREATE TABLE BigOrders
SELECT
  CustomerID,
  SUM(NumberOfUnits * CostOfUnit) as TotalOrderValue
FROM
  Orders
GROUP BY
  CustomerID
HAVING
  TotalOrderValue > 1000
```

### part c)

> Return the total Amount of orders for each month, ordered by year, then month (both in descending order)

```sql
SELECT
  year(OrderDate) as year,
  month(OrderDate) as month,
  Count(*) as MonthOrders
FROM
  Orders
GROUP BY
  year,
  month
ORDER BY
  year DESC,
  month DESC
```
