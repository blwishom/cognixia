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
