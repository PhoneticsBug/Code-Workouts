# Weather Observation Station 15

Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than $137.2345$. Round your answer to $4$ decimal places.

### Input Format

The STATION table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg">

where LAT_N is the northern latitude and LONG_W is the western longitude.

```SQL
SELECT
    ROUND(LONG_W, 4)
FROM
    (SELECT * FROM STATION
    WHERE LAT_N < 137.2345) AS STATION
ORDER BY 
    LAT_N DESC
LIMIT 1;
```