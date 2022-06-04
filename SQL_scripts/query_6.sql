select * from 
	(select pr_researcher_id, first_name ,last_name,count(*) as projcount 
    from 
		(select proj_id 
        from projects 
        where expiry_date>curdate() and start_date<curdate()) active_proj 
	inner join projects_researchers on proj_id=pr_proj_id 
    inner join researchers on pr_researcher_id = researcher_id 
    where age<40 
    group by pr_researcher_id)a 
where projcount = 
	(select max(projcount) as maximum 
	from 
		(select pr_researcher_id,first_name,last_name, count(*) as projcount 
        from 
			(select proj_id 
            from projects 
            where expiry_date>curdate() and start_date<curdate()) active_proj 
		inner join projects_researchers on proj_id=pr_proj_id 
		inner join researchers on pr_researcher_id = researcher_id 
		where age<40 group by pr_researcher_id order by projcount desc)b
        );
