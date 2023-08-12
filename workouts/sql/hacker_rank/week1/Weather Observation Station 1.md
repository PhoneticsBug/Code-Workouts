# Weather Observation Station 1

Query a list of CITY and STATE from the STATION table.

The STATION table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg" size=70%>

where LAT_N is the northern latitude and LONG_W is the western longitude.

```sql
SELECT
    CITY,
    STATE
    FROM
        STATION
```