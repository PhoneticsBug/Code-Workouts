# Weather Observation Station 18

Consider $P_1(a, b)$ and $P_2(c, d)$ to be two points on a 2D plane.

 - $a$ happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
 - $b$ happens to equal the minimum value in Western Longitude (LONG_W in STATION).
 - $c$ happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
 - $d$ happens to equal the maximum value in Western Longitude (LONG_W in STATION).

Query the Manhattan Distance between points $P_1$ and $P_2$ and round it to a scale of $4$ decimal places.

### Input Format

The STATION table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg">

where LAT_N is the northern latitude and LONG_W is the western longitude.

```SQL
-- (c - a) + (d - b)

SELECT
    ROUND((MAX(LAT_N) - MIN(LAT_N)) + (MAX(LONG_W) - MIN(LONG_W)), 4)
FROM
    STATION
```