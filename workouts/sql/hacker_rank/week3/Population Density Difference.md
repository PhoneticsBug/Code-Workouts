# Population Density Difference

Query the difference between the maximum and minimum populations in CITY.

### Input Format

The CITY table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg" size=70%>

```SQL
SELECT
    MAX(POPULATION) - MIN(POPULATION)
FROM
    CITY
```