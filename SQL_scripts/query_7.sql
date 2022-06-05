select ename,organisation_name,sum(proj_amount) as total_amount 
from projects 
inner join organisations on proj_organisation_id= organisation_id 
inner join executives on proj_executive_id = executive_id 
where category='comp' 
group by proj_executive_id 
order by sum(proj_amount) 
desc limit 5;
