# Weather Observation Station 19

Consider $P_1(a, c)$ and $P_2(b, d)$ to be two points on a 2D plane where $(a, b)$ are the respective minimum and maximum values of Northern Latitude (LAT_N) and $(c, d)$ are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.

Query the Euclidean Distance between points $P_1$ and $P_2$ and format your answer to display $4$ decimal digits.

### Input Format

The STATION table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg">

where LAT_N is the northern latitude and LONG_W is the western longitude.

```SQL
SELECT
    ROUND(
        SQRT(
            POWER((MAX(LAT_N) - MIN(LAT_N)), 2) +
            POWER((MAX(LONG_W) - MIN(LONG_W)), 2)
        ), 
        4)
FROM
    STATION
```