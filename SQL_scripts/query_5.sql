DROP PROCEDURE FindTop3;
DELIMITER $$

CREATE PROCEDURE FindTop3()
BEGIN
DECLARE x INT;
SET x=0;
create temporary table scientific_fields_pairs select a.scientific_field_name as sf1,b.scientific_field_name as sf2 from scientific_fields a inner join scientific_fields b on a.scientific_field_name < b.scientific_field_name;
alter table scientific_fields_pairs add pair_appearance_count int;
SET @lim= (select count(*) from scientific_fields_pairs);
loop_label: LOOP
IF x >@lim THEN LEAVE loop_label;
END IF;
set @sf1 = (select sf1 from scientific_fields_pairs limit x,1);
set @sf2 = (select sf2 from scientific_fields_pairs limit x,1);
select count(*) from (select distinct a.sfp_proj_id from scientific_fields_projects a inner join scientific_fields_projects b where a.sfp_scientific_field_name = @sf1 and  b.sfp_scientific_field_name = @sf2 and a.sfp_proj_id=b.sfp_proj_id)c into @paircount;
update scientific_fields_pairs set pair_appearance_count = @paircount where sf1 = @sf1 and sf2 = @sf2;
SET x=x+1;
END LOOP;
select sf1,sf2,pair_appearance_count from scientific_fields_pairs order by pair_appearance_count desc limit 3;
END$$
DELIMITER ;