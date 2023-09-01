# Placements

You are given three tables: Students, Friends and Packages. Students contains two columns: ID and Name. Friends contains two columns: ID and Friend_ID (ID of the ONLY best friend). Packages contains two columns: ID and Salary (offered salary in $ thousands per month).

<img src="https://s3.amazonaws.com/hr-challenge-images/12895/1443820186-2a9b4939a8-1.png">

Write a query to output the names of those students whose best friends got offered a higher salary than them. Names must be ordered by the salary amount offered to the best friends. It is guaranteed that no two students got same salary offer.

#### Sample Input

<img src="https://s3.amazonaws.com/hr-challenge-images/12895/1443820079-9bd1e231b1-2_1.png">

<img src="https://s3.amazonaws.com/hr-challenge-images/12895/1443820100-adb691b2f5-2_2.png"> 

<img src="https://s3.amazonaws.com/hr-challenge-images/12895/1443820100-adb691b2f5-2_2.png">

#### Sample Output

```
Samantha
Julia
Scarlet
```

#### Explanation

See the following table:

<img src="https://s3.amazonaws.com/hr-challenge-images/12895/1443819966-c37c146d27-3.png">

Now,

Samantha's best friend got offered a higher salary than her at 11.55
Julia's best friend got offered a higher salary than her at 12.12
Scarlet's best friend got offered a higher salary than her at 15.2
Ashley's best friend did NOT get offered a higher salary than her
The name output, when ordered by the salary offered to their friends, will be:

- Samantha
- Julia
- Scarlet

#### 풀이 전략
친구 ID로 조회한 연봉과 본인 ID로 조회한 연봉을 가진 테이블 두개를 만든 후 합치면서 비교

#### 실패한 코드
```SQL
SET SQL_MODE = ''; 

SELECT S.NAME, FP.SALARY, FP.FRIEND_ID, S.ID
FROM (
    SELECT * FROM STUDENTS S
    JOIN PACKAGES S ON S.ID = P.ID 
    ) STUD
JOIN (
    SELECT F.ID, F.FRIEND_ID, MAX(P.SALARY) AS SALARY FROM FRIENDS F
    JOIN PACKAGES P ON F.FRIEND_ID = P.ID
    GROUP BY F.ID) FP ON FP.FRIEND_ID = S.ID
ORDER BY FP.SALARY DESC
```


#### 정답
```SQL
SELECT S.NAME
FROM STUDENTS S
    INNER JOIN FRIENDS F ON F.ID = S.ID
    INNER JOIN PACKAGES P ON P.ID = S.ID
    INNER JOIN PACKAGES PP ON PP.ID = F.FRIEND_ID
WHERE P.SALARY < PP.SALARY
ORDER BY PP.SALARY
```