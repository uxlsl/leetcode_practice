-- 第二高的薪水
-- 分页查询
-- LIMIT <M> OFFSET <N>
-- https://www.liaoxuefeng.com/wiki/1177760294764384/1217864791925600
-- 
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
