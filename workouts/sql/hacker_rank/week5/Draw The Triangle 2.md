# Draw The Triangle 2

P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

```
* 
* * 
* * * 
* * * * 
* * * * *
```

Write a query to print the pattern P(20).


```SQL
SET
    @NUMBER = 0;
SELECT
    REPEAT('* ', @NUMBER := @NUMBER + 1)
FROM
    INFORMATION_SCHEMA.TABLES
LIMIT
    20;
```