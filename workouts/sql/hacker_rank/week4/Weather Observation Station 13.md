# Weather Observation Station 13

Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than $38.7880$ and less than $137.2345$. Truncate your answer to  decimal places.

### Input Format

The STATION table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg">

where LAT_N is the northern latitude and LONG_W is the western longitude.

```SQL
SELECT
    ROUND(SUM(LAT_N), 4)
FROM
    STATION
WHERE 
    LAT_N BETWEEN 38.7880 AND 137.2345;
```