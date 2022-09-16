
-- create
CREATE TABLE STUDENTS (
  Id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

-- insert
INSERT INTO STUDENTS VALUES (0001, 'Александр', 27,г. Долгопрудный);
INSERT INTO STUDENTS VALUES (0002, 'Сергей', 18,г. Москва);
INSERT INTO STUDENTS VALUES (0003, 'Артем', 24,г. Вильнюс);
INSERT INTO STUDENTS VALUES (0004, 'Валерий', 23,г. Берлин);
INSERT INTO STUDENTS VALUES (0005, 'Семен', 16,г. Сан-Франсиско);
INSERT INTO STUDENTS VALUES (0006, 'Татьяна', 14,г. Рим);
INSERT INTO STUDENTS VALUES (0007, 'Алексей', 31,г. Москва);


-- fetch 
SELECT * FROM STUDENTS WHERE age > 18;