# [Revising Aggregations - The Count Function](https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem?isFullScreen=true)

Query a count of the number of cities in CITY having a Population larger than .

### Input Format

The CITY table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg">

```SQL
SELECT
    COUNT(NAME)
FROM
    CITY
WHERE
    POPULATION > 100000
```