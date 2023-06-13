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
