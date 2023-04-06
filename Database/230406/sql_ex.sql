INSERT INTO emp (ename, job, sal)
     VALUES('KIMSSAFY', 'PROGRAMMER', '6000');

INSERT INTO EMP
VALUES('2531', 'MINSSAFY', 'SALESMAN', '7755', '2/5/1969', '9000', '300', '10');

DELETE FROM emp;
DELETE FROM DEPT;

DELETE FROM emp WHERE ename='SCOTT';

UPDATE EMP
  SET deptno = 30
 WHERE mgr = 7698;

SELECT sum(sal), deptno
  FROM EMP
 GROUP BY deptno;

SELECT sum(sal+comm), job
  FROM emp
 GROUP BY job;

SELECT sum(sal+IFNULL(comm,0)), deptno, job
  FROM emp
 GROUP BY deptno, job;

SELECT empno, ename
  FROM emp e1
 WHERE e1.sal > (SELECT avg(e2.sal+IFNULL(e2.comm, 0))
                   FROM emp e2
                  WHERE e2.job = e1.job
                  GROUP BY e2.job);

SELECT avg(sal+IFNULL(comm,0)), job
  FROM emp
 GROUP BY job;

-- 동등 조인 (INNER JOIN)
SELECT empno, ename, e.deptno, d.deptno, dname
  FROM emp e, dept d  -- e, d 는 각각 emp, dept 의 별명... emp AS e 처럼 AS를 붙여서 쓸 수도 있음
 WHERE e.deptno = d.deptno;

SELECT * FROM emp;

SELECT e1.empno, e1.ename, e1.deptno, e1.mgr as "매니저", e1.job
  FROM emp e1, emp e2
 WHERE e1.mgr = e2.empno;