CREATE VIEW view_1 AS 
SELECT first_name, last_name, proj_title 
FROM projects_researchers 
INNER JOIN projects ON proj_id = pr_proj_id 
INNER JOIN researchers ON researcher_id = pr_researcher_id 
ORDER BY researcher_id 
;
