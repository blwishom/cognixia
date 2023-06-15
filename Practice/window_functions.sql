select *
from streams;

SELECT
   artist,
   week,
   streams_millions,
   LAG(streams_millions, 1, 0) OVER (
      ORDER BY week
   ) previous_week_streams
FROM
   streams
WHERE
   artist = 'Lady Gaga';

SELECT
   artist,
   week,
   streams_millions,
   streams_millions - LAG(streams_millions, 1, streams_millions) OVER (
      ORDER BY week
   ) streams_millions_change
FROM
   streams
WHERE
   artist = 'Lady Gaga';





SELECT
   artist,
   week,
   streams_millions,
   LEAD(streams_millions, 1) OVER (
      PARTITION BY artist
      ORDER BY week
   ) - streams_millions AS 'streams_millions_change'
FROM
   streams;

SELECT
   artist,
   week,
   streams_millions,
   LEAD(streams_millions, 1) OVER (
      PARTITION BY artist
      ORDER BY week
   ) - streams_millions AS 'streams_millions_change',
   chart_position,
   chart_position - LEAD(chart_position, 1) OVER (
      PARTITION BY artist
      ORDER BY week
) AS 'chart_position_change'
FROM
   streams;
