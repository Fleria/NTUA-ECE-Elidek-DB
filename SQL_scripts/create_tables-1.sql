/*
Navicat MySQL Data Transfer

Source Server         : elidek
Source Server Version : 80022
Source Host           : localhost:3306
Source Database       : db-project-demo

Target Server Type    : MYSQL
Target Server Version : 80022
File Encoding         : 65001

Date: 2022-03-03 14:01:37
*/

SET FOREIGN_KEY_CHECKS=1;
SET @sum = 0;

-- ----------------------------
-- Create database
-- ----------------------------
DROP schema if exists elidek1;
CREATE SCHEMA elidek1;
USE elidek1;

-- ----------------------------
-- Table structure
-- ----------------------------

DROP TABLE IF EXISTS organisations;
DROP TABLE IF EXISTS organisations;
CREATE TABLE organisations (
organisation_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
organisation_name varchar(45) NOT NULL,
abbreviation varchar(45) , 
category enum ('comp','uni', 'rs') NOT NULL,
postal_code varchar(45) , 
street varchar(45) ,
town varchar(45) ,
unique (category,organisation_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS funds;
CREATE TABLE funds(
f_organisation_id int not null,
f_category enum ('comp','uni', 'rs') NOT NULL,
private int default 0,
gov int default 0,
CHECK ((f_category='uni' and private=0)or(f_category='comp' and gov=0)or(f_category='rs')),
unique index  idx_fun_id (f_organisation_id,f_category),
constraint fun_id foreign key (f_organisation_id) references organisations (organisation_id) on delete cascade on update restrict,
constraint fund_cat foreign key (f_category) references organisations ( category) on delete cascade on update restrict
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS organisations_telephones;
CREATE TABLE organisations_telephones (
ot_organisation_id int NOT NULL,
telephone varchar(15) NOT NULL,
CONSTRAINT ot_organisation_id FOREIGN KEY (ot_organisation_id) REFERENCES organisations(organisation_id) ON DELETE restrict ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS executives;
CREATE TABLE executives  (
executive_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
ename varchar(45) NOT NULL 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS researchers;
CREATE TABLE researchers  (
researcher_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
first_name varchar(45) not null, 
last_name varchar(45) not null,
sex enum('non-binary','male','female'), 
date_birth date not null,
age int as (timestampdiff(year,date_birth,curdate())),
res_start_date date,
town varchar(45),
res_organisation_id int NOT NULL,
CONSTRAINT res_organisation_id FOREIGN KEY (res_organisation_id) REFERENCES organisations (organisation_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS programs;
CREATE TABLE programs  (
program_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
program_name varchar(45) NOT NULL,
administration varchar(45) not null
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS scientific_fields;
CREATE TABLE scientific_fields  (
scientific_field_name varchar(45) NOT NULL PRIMARY KEY
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS projects;
CREATE TABLE projects (
  proj_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  proj_title varchar(45) NOT NULL,
  proj_amount int NOT NULL,
  summary varchar(200),
  start_date date NOT NULL,
  expiry_date date NOT NULL,
  CHECK(start_date<expiry_date),
  duration int as (timestampdiff(year,start_date,expiry_date)), 
  CHECK (0<duration<5),
  evaluation_grade smallint NOT NULL,
  evaluation_date date NOT NULL,
  CHECK (evaluation_date<start_date),
  proj_executive_id int NOT NULL,
  proj_organisation_id int NOT NULL,
  scientific_officer_id int NOT NULL,
  evaluator_id int NOT NULL,
  program_id int NOT NULL,
  CONSTRAINT proj_executive_id FOREIGN KEY (proj_executive_id) REFERENCES executives (executive_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT proj_organisation_id FOREIGN KEY (proj_organisation_id) REFERENCES organisations (organisation_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT scientific_officer_id FOREIGN KEY (scientific_officer_id) REFERENCES researchers (researcher_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT evaluator_id FOREIGN KEY (evaluator_id) REFERENCES researchers (researcher_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT program_id FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE ON UPDATE CASCADE
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
  DROP TABLE IF EXISTS deliverables;
CREATE TABLE deliverables  (
del_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
del_summary varchar(200), 
del_proj_id int NOT NULL,
CONSTRAINT del_proj_id FOREIGN KEY (del_proj_id) REFERENCES projects (proj_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS scientific_fields_projects;
CREATE TABLE scientific_fields_projects  (
sfp_scientific_field_name varchar(45),
sfp_proj_id int NOT NULL,
CONSTRAINT sfp_scientific_field_name FOREIGN KEY (sfp_scientific_field_name) REFERENCES scientific_fields(scientific_field_name) ON DELETE CASCADE ON UPDATE CASCADE, 
CONSTRAINT sfp_proj_id FOREIGN KEY (sfp_proj_id) REFERENCES projects (proj_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS projects_researchers;
CREATE TABLE projects_researchers  (
pr_researcher_id int,
pr_proj_id int NOT NULL,
CONSTRAINT pr_researcher_id FOREIGN KEY (pr_researcher_id) REFERENCES researchers (researcher_id) ON DELETE CASCADE ON UPDATE CASCADE, 
CONSTRAINT pr_proj_id FOREIGN KEY (pr_proj_id) REFERENCES projects (proj_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*triggers*/

DELIMITER //
create trigger ins_org after insert on organisations FOR EACH ROW
begin
	insert into funds (f_organisation_id,f_category) values (new.organisation_id,new.category) ;
end; //
delimiter ;



