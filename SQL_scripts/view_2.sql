CREATE VIEW view_2 AS 
SELECT organisation_name, telephone  
FROM organisations_telephones 
INNER JOIN organisations ON organisation_id = ot_organisation_id 
ORDER BY organisation_id 
;