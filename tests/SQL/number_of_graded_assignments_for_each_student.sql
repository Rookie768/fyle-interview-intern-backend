-- Write query to get number of graded assignments for each student:
SELECT student_id, COUNT(*) as graded_count
FROM assignments
WHERE grade IS NOT NULL
GROUP BY student_id;
