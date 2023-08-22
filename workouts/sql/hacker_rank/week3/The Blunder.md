# The Blunder

Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's  key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.: actual-miscalculated  average monthly salaries), and round it up to the next integer.

### Input Format

The EMPLOYEES table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/12893/1443817108-adc2235c81-1.png" size=70%>

Note: Salary is per month.

Constraints

$ 1000 < Salary < 10^5 $

### Sample Input

<img src="https://s3.amazonaws.com/hr-challenge-images/12893/1443817161-299cc6eb7f-2.png" size=70%>

### Sample Output

```
2061
```

### Explanation

The table below shows the salaries without zeros as they were entered by Samantha:

<img src="https://s3.amazonaws.com/hr-challenge-images/12893/1443817229-eb00d44a3b-3.png" size=70%>

Samantha computes an average salary of 98.00. The actual average salary is 2159.00.

The resulting error between the two calculations is 2159.00 - 98.00 = 2061.00. Since it is equal to the integer 2061, it does not get rounded up.

```SQL
SELECT 
    CEIL(
        AVG(SALARY) - AVG(REPLACE(SALARY, 0, '')))
FROM
    EMPLOYEES

```