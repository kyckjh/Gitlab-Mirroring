-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

CREATE TABLE classmate (
 name TEXT NOT NULL,
 age INTEGER NOT NULL,
 address TEXT NOT NULL
);

INSERT INTO classmate (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmate
VALUES 
  ('김철수', 30, '경기'),
  ('이영미', 31, '강원'),
  ('박진성', 26, '전라'),
  ('최지수', 12, '충청'),
  ('정요한', 28, '경상');

UPDATE classmate
   SET name='김철수한무두루미',
       address='제주도'
 WHERE rowid = 2;

DELETE FROM classmate WHERE rowid = 5;

SELECT rowid, * FROM classmate;

DELETE FROM classmate WHERE name LIKE '%영%';

DELETE FROM classmate;

-- DELETE 할 때 데이터가 완전히 삭제되는게 무섭다면?
-- Hard Delete vs Soft Delete
-- is_deleted와 같이 삭제를 표시하는 column을 추가
-- 완전히 삭제하는 대신 is_deleted 값을 변경하여 삭제 표시




SELECT COUNT(*) FROM users;

SELECT country, avg(balance) FROM users
GROUP BY country ORDER BY avg(balance) DESC;

SELECT last_name, COUNT(*)
    AS number_of_name
  FROM users
 GROUP BY last_name;