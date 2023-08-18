# Type of Triangle

Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

- Equilateral: It's a triangle with  sides of equal length.
- Isosceles: It's a triangle with  sides of equal length.
- Scalene: It's a triangle with  sides of differing lengths.
- Not A Triangle: The given values of A, B, and C don't form a triangle.

### Input Format

The TRIANGLES table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/12887/1443815629-ac2a843fb7-1.png" size=70%>

Each row in the table denotes the lengths of each of a triangle's three sides.

### Sample Input

<img src="https://s3.amazonaws.com/hr-challenge-images/12887/1443815827-cbfc1ca12b-2.png" size=70%>

### Sample Output

```
Isosceles
Equilateral
Scalene
Not A Triangle
Explanation
```

<img src="triangle_img1.png" size=70%>


```SQL
SELECT
    CASE
        WHEN (A + B > C) AND (A + C > B) AND (B + C > A) THEN
        CASE
            WHEN (A = B) AND (B = C) THEN "Equilateral"
            WHEN (A = B) OR (A = C) OR (B = C) THEN "Isosceles"
            ELSE "Scalene"
            END
        ELSE "Not A Triangle"
    END
FROM
    TRIANGLES;
```