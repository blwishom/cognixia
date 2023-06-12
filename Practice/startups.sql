''' TRENDS IN STARTUPS '''

select *
from startups;

select count(*)
from startups;

select sum(valuation)
from startups;

select name, max(raised)
from startups;

select name, max(raised)
from startups
where stage like 'Seed';

select name, min(founded)
from startups;

select avg(valuation)
from startups;

select category, avg(valuation)
from startups
group by category;

select category, round(avg(valuation), 2)
from startups
group by category;

select category, round(avg(valuation), 2)
from startups
group by valuation
order by valuation desc;

select category, count(name)
from startups
group by category;

select category, count(name) as counted
from startups
group by category
having counted > 3;

select location, avg(employees)
from startups
group by location;

select location, avg(employees)
from startups
group by location
having avg(employees) > 500;
