# Symmetric Pairs

You are given a table, Functions, containing two columns: X and Y.

<img src="https://s3.amazonaws.com/hr-challenge-images/12892/1443818798-51909e977d-1.png">

Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.

Write a query to output all such symmetric pairs in ascending order by the value of X. List the rows such that X1 ≤ Y1.

#### Sample Input

<img src="https://s3.amazonaws.com/hr-challenge-images/12892/1443818693-b384c24e35-2.png">

#### Sample Output

```
20 20
20 21
22 23
```


```SQL
SELECT X, Y
FROM FUNCTIONS
WHERE X = Y
GROUP BY X, Y
HAVING COUNT(*) = 2

UNION

SELECT F1.X, F1.Y
FROM FUNCTIONS F1
    INNER JOIN FUNCTIONS F2 ON F1.X = F2.Y AND F1.Y = F2.X
WHERE F1.X < F1.Y
ORDER BY X
```