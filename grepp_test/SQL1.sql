-- 코드를 입력하세요
SELECT  EMPLOYEE_ID,
CASE 
    when (COUNT(EMPLOYEE_ID) BETWEEN 2 and 3) then "우수 사원"
    when (COUNT(EMPLOYEE_ID)  >= 4) then "최우수 사원"
    else "일반 사원"
    END as "분류 상태"
,COUNT(EMPLOYEE_ID) as "COUNT" from SELLINGS group by EMPLOYEE_ID Having count(EMPLOYEE_ID) >=1