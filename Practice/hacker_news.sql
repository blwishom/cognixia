''' Analyze Hacker_News '''

SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;

select sum(score)
from hacker_news;

select user, sum(score) as score_sum
from hacker_news
group by user
having score_sum > 200;

SELECT round((517 + 309 + 304 + 282) / 6366.0, 2) as 'Users Scores';


select user, count(url)
from hacker_news
where url like 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
group by user;

SELECT count(url) as Url_Count, CASE
   WHEN url LIKE '%github.com%' THEN 'GitHub'
   WHEN url LIKE '%medium.com%' THEN 'Medium'
   WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
   ELSE 'Other'
  END AS 'Source'
FROM hacker_news
GROUP BY Source;

select timestamp
from hacker_news
limit 10;

select timestamp, strftime('%H', timestamp)
from hacker_news
group by 1
limit 10;

select strftime('%H', timestamp), avg(score), count(*)
from hacker_news
group by 1
order by 2 desc;

select strftime('%H', timestamp) as 'Time_in_Hours', round(avg(score), 2) as 'Score_Rounded', count(*) as 'Total_Count'
from hacker_news
where timestamp is not null
group by 1
order by 2 desc;
