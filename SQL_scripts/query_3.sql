 select scientific_field_name, proj_title, first_name, last_name 
 from 
 (select scientific_field_name, proj_id,proj_title 
 from 
 (select scientific_field_name , count(*) 
 from scientific_fields   
 inner join scientific_fields_projects on scientific_field_name = sfp_scientific_field_name  
 inner join projects on proj_id=sfp_proj_id 
 group by scientific_field_name 
 order by count(*) DESC 
 limit 1) a 
 inner join scientific_fields_projects on a.scientific_field_name = sfp_scientific_field_name 
 inner join projects on proj_id=sfp_proj_id)b 
 inner join projects_researchers on pr_proj_id = b.proj_id 
 inner join researchers on pr_researcher_id=researcher_id 
order by proj_title 
 ;