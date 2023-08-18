# Higher Than 75 Marks

Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

### Input Format

<img src="https://s3.amazonaws.com/hr-challenge-images/12896/1443815243-94b941f556-1.png" size=70%>

The STUDENTS table is described as follows:  The Name column only contains uppercase (A-Z) and lowercase (a-z) letters.

### Sample Input

<img src="https://s3.amazonaws.com/hr-challenge-images/12896/1443815209-cf4b260993-2.png vb" size=70%>


### Sample Output

```
Ashley
Julia
Belvet
Explanation
```

Only Ashley, Julia, and Belvet have Marks > . If you look at the last three characters of each of their names, there are no duplicates and 'ley' < 'lia' < 'vet'.

```SQL
SELECT
    NAME
    FROM
        STUDENTS
WHERE MARKS > 75
ORDER BY RIGHT(NAME, 3), ID ASC;
```