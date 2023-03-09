CREATE TABLE sobes_student_marks(
    student_mark SERIAL PRIMARY KEY,
    student_name VARCHAR(20),
    mark INT
);

INSERT INTO sobes_student_marks(student_name, mark)
VALUES ('petrov', 5), ('petrov', 3), ('petrov', 4), ('petrov1', 3), ('petrov1', 3), ('petrov1', 5),
     ('petrov2', 5), ('petrov3', 2), ('petrov2', 4), ('petrov2', 4), ('petrov3', 3);


SELECT * FROM sobes_student_marks;

SELECT student_name, mark, COUNT(*) AS Колво
FROM sobes_student_marks
GROUP BY student_name, mark
ORDER BY mark DESC, student_name;


SELECT student_name, SUM(mark) AS kolvo
FROM (
    SELECT student_name, CASE WHEN mark='5' THEN 1 ELSE 0 END mark
    FROM sobes_student_marks
) AS query_in
GROUP BY student_name;