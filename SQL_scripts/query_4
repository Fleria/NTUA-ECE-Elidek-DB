select orga organisation, DATE_FORMAT(std1, "%Y") first_year,DATE_FORMAT(std2, "%Y") second_year, count1 projects_per_year 
from 
(select * 
from 
(select organisation_name orga, proj_title t1, start_date std1,count(*) count1 
from projects 
inner join organisations on organisation_id = proj_organisation_id  
group by organisation_name,DATE_FORMAT(start_date, "%Y") 
having count1>=2) a 
inner join 
(select organisation_name orgb, proj_title t2, start_date std2, count(*) count2 
from projects 
inner join organisations on organisation_id = proj_organisation_id  
group by organisation_name,DATE_FORMAT(start_date, "%Y")  
having count2>=2) b 
on t1!=t2) c 
where orga=orgb and count1=count2 and (CAST(DATE_FORMAT(std1, "%Y") AS int)+1= CAST(DATE_FORMAT(std2, "%Y") AS int));
