# Employee Names

Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.

Input Format

The Employee table containing employee data for a company is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/19629/1458557872-4396838885-ScreenShot2016-03-21at4.27.13PM.png" size=70%>

where employee_id is an employee's ID number, name is their name, months is the total number of months they've been working for the company, and salary is their monthly salary.

### Sample Input

<img src="https://s3.amazonaws.com/hr-challenge-images/19629/1458558202-9a8721e44b-ScreenShot2016-03-21at4.32.59PM.png" size=70%>

### Sample Output

```
Angela
Bonnie
Frank
Joe
Kimberly
Lisa
Michael
Patrick
Rose
Todd
```

```SQL
SELECT 
    NAME
    FROM
        EMPLOYEE
ORDER BY NAME ASC
```