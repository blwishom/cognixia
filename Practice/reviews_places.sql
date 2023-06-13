SELECT *
FROM places;

SELECT *
FROM reviews;

select *
from places
where price_point <= '$$';

select *
from places
join reviews
  on places.id = reviews.place_id;

select *
from places
join reviews
  on places.id = reviews.place_id
where total_reviews not null
order by total_reviews;

select places.name as Name, places.average_rating as AVG_Rating, reviews.username as Username, reviews.rating as Rating, reviews.review_date as Review_Date, reviews.note as Note
from places
join reviews
  on places.id = reviews.place_id
where total_reviews not null
order by total_reviews
limit 10;

select places.name as Name, places.average_rating as AVG_Rating, reviews.username as Username, reviews.rating as Rating, reviews.review_date as Review_Date, reviews.note as Note
from places
left join reviews
  on places.id = reviews.place_id
where total_reviews not null
order by total_reviews
limit 10;

select places.id, places.name
from places
join reviews
  on places.id = reviews.place_id
where reviews.place is null;
