DROP TABLE zoo;
CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);


BEGIN;                  -- BEGIN 명령어로 트랜잭션 시작
  DELETE FROM zoo       -- zoo TABLE에서
  WHERE weight < 100;   -- weight가 100 미만인 레코드 삭제
ROLLBACK;               -- 트랜잭션 시작 이후로 수행된 모든 작업 취소 => 데이터베이스 원래 상태로 복구
BEGIN;                      -- 트랜잭션 시작
  DELETE FROM zoo           -- zoo TABLE에서
  WHERE eat = 'omnivore';   -- eat column이 'omnivore'인 record 모두 삭제
COMMIT;                     -- 트랜잭션 이후 수행된 연산 데이터베이스에 반영 => 실제 데이터 삭제됨

-- zoo TABLE의 모든 레코드의 수 출력, 위에서 eat column이 'omnivore'인 레코드가 모두 삭제되었으므로
-- 남은 레코드는 총 3개
SELECT COUNT(*)
FROM zoo;