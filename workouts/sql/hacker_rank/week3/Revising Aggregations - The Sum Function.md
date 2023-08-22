# Revising Aggregations - The Sum Function

Query the total population of all cities in CITY where District is California.

### Input Format

The CITY table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg" size=70%>

```SQL
SELECT
    SUM(POPULATION)
FROM 
    CITY
WHERE
    DISTRICT = 'California'
```