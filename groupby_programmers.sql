-- 1
SELECT ANIMAL_TYPE,COUNT(ANIMAL_TYPE) AS CNT FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE
-- 2
SELECT NAME,COUNT(*) AS COUNT FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) >= 2 ORDER BY NAME
--3 
SELECT HOUR(DATETIME) ,COUNT(*) AS CNT FROM ANIMAL_OUTS WHERE HOUR(DATETIME) BETWEEN "9" AND "19" GROUP BY HOUR(DATETIME) ORDER BY HOUR(DATETIME) ASC
-- 4
SET @HOUR = -1; SELECT (@HOUR := @HOUR + 1) HOUR, (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @HOUR ) COUNT FROM ANIMAL_OUTS WHERE @HOUR < 23