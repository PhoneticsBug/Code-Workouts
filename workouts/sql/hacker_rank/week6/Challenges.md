# Challenges

Julia asked her students to create some coding challenges. Write a query to print the hacker_id, name, and the total number of challenges created by each student. Sort your results by the total number of challenges in descending order. If more than one student created the same number of challenges, then sort the result by hacker_id. If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.

Input Format

The following tables contain challenge data:

- Hackers: The hacker_id is the id of the hacker, and name is the name of the hacker. 

<img src="https://s3.amazonaws.com/hr-challenge-images/19506/1458521004-cb4c077dd3-ScreenShot2016-03-21at6.06.54AM.png" size=70%c>

- Challenges: The challenge_id is the id of the challenge, and hacker_id is the id of the student who created the challenge.

<img src="https://s3.amazonaws.com/hr-challenge-images/19506/1458521079-549341d9ec-ScreenShot2016-03-21at6.07.03AM.png" size=70%>

### Sample Input 0

<img src="https://s3.amazonaws.com/hr-challenge-images/19506/1458521384-34c6866dae-ScreenShot2016-03-21at6.07.15AM.png" size=70%>

Hackers Table:

Challenges Table:

<img src="https://s3.amazonaws.com/hr-challenge-images/19506/1458521410-befa8e1cd9-ScreenShot2016-03-21at6.07.25AM.png" size=70%>

### Sample Output 0

```
21283 Angela 6
88255 Patrick 5
96196 Lisa 1
```

### Sample Input 1

<img src="https://s3.amazonaws.com/hr-challenge-images/19506/1458521469-87036deea3-ScreenShot2016-03-21at6.07.48AM.png" size=70%>

Hackers Table:

Challenges Table:

<img src="https://s3.amazonaws.com/hr-challenge-images/19506/1458521490-358215cf0b-ScreenShot2016-03-21at6.07.58AM.png" size=70%>

### Sample Output 1

```
12299 Rose 6
34856 Angela 6
79345 Frank 4
80491 Patrick 3
81041 Lisa 1
```

### Explanation

For Sample Case 0, we can get the following details:

<img src="https://s3.amazonaws.com/hr-challenge-images/19506/1458521677-fd04c384c0-ScreenShot2016-03-21at6.07.38AM.png" size=70%>

Students $5077$ and $62743$ both created $4$ challenges, but the maximum number of challenges created is  so these students are excluded from the result.

For Sample Case 1, we can get the following details:

<img src="https://s3.amazonaws.com/hr-challenge-images/19506/1458521836-24039e7523-ScreenShot2016-03-21at6.08.08AM.png" size=70%>

Students $12299$ and $34856$ both created $6$ challenges. Because  is the maximum number of challenges created, these students are included in the result.