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
