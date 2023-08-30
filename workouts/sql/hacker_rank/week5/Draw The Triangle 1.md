# Draw The Triangle 1

P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

```
* * * * * 
* * * * 
* * * 
* * 
*
```

Write a query to print the pattern P(20).


```SQL
SET 
    @NUMBER = 21;
SELECT 
    REPEAT('* ', @NUMBER := @NUMBER - 1) 
FROM 
    INFORMATION_SCHEMA.TABLES 
LIMIT 
    20;
```