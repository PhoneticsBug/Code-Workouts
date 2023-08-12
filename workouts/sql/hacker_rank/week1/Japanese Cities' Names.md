# Japanese Cities' Names

Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.

The CITY table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg" size=70%>

```sql
SELECT
    NAME
    FROM
        CITY
WHERE
    COUNTRYCODE = "JPN"
```