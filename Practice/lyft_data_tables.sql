SELECT *
FROM trips;
SELECT *
FROM riders;
SELECT *
FROM cars;

select *
from riders
cross join cars;

select *
from trips
left join riders
  on trips.rider_id = riders.id;

select *
from trips
inner join cars
  on trips.car_id = cars.id;

select *
from riders
union
select *
from riders2;

select round(avg(cost), 2) as Average_Cost
from trips;

select *
from riders
where total_trips < 500;

select count(*) as Active_Cars
from cars
where status is 'active';


select *
from cars
order by trips_completed desc
limit 2;
