select first_name,last_name,projcount 
from 
(select pr_researcher_id,count(*) as projcount 
from projects_researchers 
where NOT EXISTS 
(select distinct del_proj_id 
from deliverables 
where pr_proj_id=del_proj_id) 
group by pr_researcher_id)a 
inner join researchers on researcher_id= pr_researcher_id 
where projcount>4; 