SELECT *
FROM orders
JOIN subscriptions
  ON orders.subscription_id = subscriptions.subscription_id;

SELECT *
FROM orders
JOIN subscriptions
  ON orders.subscription_id = subscriptions.subscription_id
WHERE description = 'Fashion Magazine';




SELECT count(*)
FROM newspaper;

SELECT count(*)
FROM online;

SELECT count(*)
FROM newspaper
JOIN online
  ON newspaper.id = online.id;





SELECT *
FROM newspaper
LEFT JOIN online
  ON newspaper.id = online.id;

SELECT *
FROM newspaper
LEFT JOIN online
  ON newspaper.id = online.id
WHERE online.id IS NULL;





SELECT *
FROM classes
INNER JOIN students
  ON classes.id = students.class_id;




SELECT count(*)
FROM newspaper
WHERE start_month <= 3 and end_month >= 3;

SELECT *
FROM newspaper
CROSS JOIN months;

SELECT *
FROM newspaper
CROSS JOIN months
WHERE start_month <= month and end_month >= month;

SELECT month, COUNT(*)
FROM newspaper
CROSS JOIN months
WHERE start_month <= month and end_month >= month
GROUP BY month;




SELECT *
FROM newspaper
UNION
SELECT *
FROM online;





WITH previous_query as (
  SELECT customer_id, COUNT(subscription_id) AS 'subscriptions'
FROM orders
GROUP BY customer_id
)

SELECT customers.customer_name, previous_query.subscriptions
FROM customers
JOIN previous_query
  ON customers.customer_id = previous_query.customer_id;
