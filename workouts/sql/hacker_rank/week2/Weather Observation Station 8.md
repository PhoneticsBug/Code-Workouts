# Weather Observation Station 8

Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

### Input Format

The STATION table is described as follows:

<img src="<img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg" size=70%>" size=70%>

where LAT_N is the northern latitude and LONG_W is the western longitude.

```SQL
SELECT DISTINCT
    CITY
    FROM
        STATION
WHERE
    UPPER(LEFT(CITY, 1)) IN ('A', 'E', 'I', 'O', 'U')
    AND UPPER(RIGHT(CITY, 1)) IN ('A', 'E', 'I', 'O', 'U');
```