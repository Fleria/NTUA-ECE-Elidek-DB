import faker,random,array,datetime
from random import randint
from datetime import date
from datetime import datetime
import numpy as np

fake = faker.Faker()
today = date.today()

content = "";

DUMMY_DATA_NUMBER = 10;
TABLE_NAME = "organisations";
TABLE_COLUMNS = [ "organisation_name", "abbreviation","category","postal_code","street","town"]
catlist=["comp","uni","rs"]

for i in range(DUMMY_DATA_NUMBER):
    organisation_id = i+1
    organisation_name = fake.company()
    abbreviation = organisation_name[0:4]
    postal_code = fake.postcode()
    street = fake.street_address()
    category=random.choice(catlist)
    town = fake.city()
    money = randint(500000,2000000)
    moneygov =randint(500000,2000000)
    content += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{organisation_name}", "{abbreviation}","{category}", "{postal_code}", "{street}", "{town}");\n'
    if (category=="comp") :
        content += f'UPDATE funds SET private="{money}" where f_organisation_id="{organisation_id}" ;\n'
    if (category=="uni") :
        content += f'UPDATE funds SET gov="{moneygov}" where f_organisation_id="{organisation_id}" ;\n'
    if (category=="rs") :
        content += f'UPDATE funds SET private="{money}", gov="{moneygov}" where f_organisation_id="{organisation_id}" ;\n'




DUMMY_DATA_NUMBER = 200;
TABLE_NAME = "researchers";
TABLE_COLUMNS = [ "first_name", "last_name", "sex","date_birth","res_start_date", "town", "res_organisation_id"]
mylist = ["male", "female", "non-binary"]

res_per_org = np.array = ([],[],[],[],[],[],[],[],[],[])
no_res_per_org = [0,0,0,0,0,0,0,0,0,0]

for i in range(DUMMY_DATA_NUMBER):
    first_name = fake.first_name()
    last_name = fake.last_name()
    sex = random.choice(mylist)
    date_birth = fake.date_of_birth(minimum_age = 18, maximum_age =65)
    town = fake.city()
    res_date = today.strftime("%Y-%m-%d")
    res_organisation_id = fake.random_int(1,10)
    res_per_org[res_organisation_id-1].append(i+1)
    no_res_per_org[res_organisation_id-1] += 1
    content += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ( "{first_name}", "{last_name}", "{sex}","{date_birth}","{res_date}",  "{town}", "{res_organisation_id}");\n'

DUMMY_DATA_NUMBER = 100;
TABLE_NAME = "executives";
TABLE_COLUMNS = [ "ename"]

for i in range(DUMMY_DATA_NUMBER):
    ename = fake.name()
    content += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ( "{ename}");\n'


DUMMY_DATA_NUMBER = 100;
TABLE_NAME = "organisations_telephones";
TABLE_COLUMNS = ["ot_organisation_id", "telephone"]

for i in range(DUMMY_DATA_NUMBER):
    ot_organisation_id= fake.random_number(1)+1
    telephone = fake.msisdn()
    content += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{ot_organisation_id}", "{telephone}");\n'



DUMMY_DATA_NUMBER = 100;
TABLE_NAME = "programs";
TABLE_COLUMNS = [ "program_name", "administration"]

for i in range(DUMMY_DATA_NUMBER):
    program_name = fake.word()
    administration = fake.company()
    content += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ( "{program_name}", "{administration}");\n'

DUMMY_DATA_NUMBER = 200;
TABLE_NAME = "projects";
TABLE_COLUMNS = [ "proj_title", "proj_amount", "summary", "start_date", "expiry_date","evaluation_grade", "evaluation_date", "proj_executive_id", "proj_organisation_id", "scientific_officer_id", "evaluator_id", "program_id"]
proj_org= []
date_per_proj=[0]*200
scoff =[]

from datetime import datetime
for i in range(DUMMY_DATA_NUMBER):
    proj_title = fake.word()
    proj_amount = fake.random_int(10000,40000)
    summary = fake.paragraph()
    start_year = str(randint(2019,2024))
    start_monthday = fake.date()
    start_month = start_monthday[5:7]
    start_day = start_monthday[8:10]
    start_date = start_year + '-' + start_month + '-' + start_day

    duration = randint(1,4)
    expiry_year = int(start_year) + duration
    date_per_proj[i] = expiry_year
    expiry_monthday = fake.date()
    expiry_month = expiry_monthday[5:7]
    expiry_day = expiry_monthday[8:10]
    if(int(expiry_month)<int(start_month)) :
        expiry_month=start_month
    if(int(expiry_day)<int(start_day)) :
        expiry_day=start_day
    expiry_date = str(expiry_year) + '-' + expiry_month + '-' + expiry_day

    evaluation_grade = randint(50,100)
    evaluation_year = str(int(start_year)-1)
    evaluation_monthday = fake.date()
    evaluation_month = evaluation_monthday[5:7]
    evaluation_day = evaluation_monthday[8:10]

    evaluation_date = evaluation_year + '-' + evaluation_month + '-' + evaluation_day
    proj_executive_id = fake.random_int(1,100)
    proj_organisation_id = fake.random_int(1,10)
    temp =(proj_organisation_id+1)%10
    proj_org.append(proj_organisation_id)
    evaluator_id = random.choice(res_per_org[temp - 1])
    scientific_officer_id = random.choice(res_per_org[proj_organisation_id-1])
    scoff.append(scientific_officer_id)
    program_id = fake.random_number(2)+1
    content += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{proj_title}", "{proj_amount}", "{summary}", "{start_date}", "{expiry_date}", "{evaluation_grade}", "{evaluation_date}", "{proj_executive_id}", "{proj_organisation_id}", "{scientific_officer_id}", "{evaluator_id}", "{program_id}");\n'


DUMMY_DATA_NUMBER = 16;
TABLE_NAME = "scientific_fields";
TABLE_COLUMNS = ["scientific_field_name"]

scientific_fields_list =["Chemistry", "Biology", "Mathematics", "Psychology", "Medicine", "Sociology", "Astronomy", "Ecology", "Geology", "Oceanography", "Microbiology", "Antrhopology","Archaeology","Philosophy","Civil Engineering","Biochemistry"]
for i in range(DUMMY_DATA_NUMBER):
    scientific_field_name = scientific_fields_list[i]
    content += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{scientific_field_name}");\n'


DUMMY_DATA_NUMBER = 200;
TABLE_NAME = "deliverables";
TABLE_COLUMNS = ["del_title","del_date","del_summary","del_proj_id"]


for i in range(DUMMY_DATA_NUMBER):
    x=randint(0,4)
    del_year = int(date_per_proj[i] - 1)
    for j in range(x):
        start_monthday = fake.date()
        del_month = start_monthday[5:7]
        del_day = start_monthday[8:10]
        del_date=str(del_year) + '-' + del_month +'-'+del_day
        del_title=fake.word()+f'{j}'
        del_summary = fake.paragraph()
        del_proj_id = i+1
        today=date.today().strftime("%Y-%m-%d")
        if((del_date > today)):
            content += f'INSERT INTO {TABLE_NAME} (del_title,del_date,del_proj_id) VALUES ( "{del_title}","{del_date}" ,"{del_proj_id}");\n'
        else :
            content += f'INSERT INTO {TABLE_NAME} (del_title,del_date,del_summary,del_proj_id) VALUES ( "{del_title}","{del_date}","{del_summary}", "{del_proj_id}");\n'

DUMMY_DATA_NUMBER = 500;
TABLE_NAME = "scientific_fields_projects";
TABLE_COLUMNS = ["sfp_scientific_field_name","sfp_proj_id"]

id=0
while DUMMY_DATA_NUMBER > 0 :
    x=fake.random_int(1,5)
    x=min(DUMMY_DATA_NUMBER,x)
    temp = scientific_fields_list.copy()
    id +=1
    for i in range(x) :
        sfp_proj_id=id
        sfp_scientific_field_name=random.choice(temp)
        temp.remove(sfp_scientific_field_name)
        content += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{sfp_scientific_field_name}", "{sfp_proj_id}");\n'
    DUMMY_DATA_NUMBER -=x



DUMMY_DATA_NUMBER = 200;
TABLE_NAME = "projects_researchers";
TABLE_COLUMNS = ["pr_researcher_id","pr_proj_id"]
res_date=[2030]*200

for i in range(DUMMY_DATA_NUMBER):
    pr_proj_id = i+1
    exp=date_per_proj[i]
    unique_res=res_per_org[proj_org[i]-1].copy()
    unique_res.remove(scoff[i])
    for j in range(int(0.5*no_res_per_org[proj_org[i]-1])):
        pr_researcher_id = random.choice(unique_res)
        unique_res.remove(pr_researcher_id)
        year=randint(2017,exp-1)
        start_monthday = fake.date()
        start_month = start_monthday[5:7]
        start_day = start_monthday[8:10]
        res_start_date= str(year) + '-' + start_month + '-' + start_day
        content += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{pr_researcher_id}", "{pr_proj_id}");\n'
        if year<res_date[pr_researcher_id-1]:
            res_date[pr_researcher_id-1]=year
            content += f'UPDATE researchers SET res_start_date="{res_start_date}" where researcher_id="{pr_researcher_id}";\n'
    pr_researcher_id = scoff[i]
    content+= f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{pr_researcher_id}", "{pr_proj_id}");\n'

content += """ delimiter //
create trigger ins_proj_sci_off before insert on projects
for each row
begin
	if not exists( select * from projects
inner join projects_researchers
on (proj_id=pr_proj_id and proj_id=new.proj_id)
where new.evaluator_id=pr_researcher_id )
then
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'EvAluAtOr CanT WOrk At tHe PrOJeCt';
        end if;
end;//
delimiter ; \n"""

content += """ DELIMITER //
create trigger ins_proj_evaluator before insert on projects
for each row
begin
	if exists( select * from projects
inner join projects_researchers
on (proj_id=pr_proj_id and proj_id=new.proj_id)
where new.evaluator_id=pr_researcher_id )
then
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'EvAluAtOr CanT WOrk At tHe PrOJeCt';
        end if;
end;//
delimiter ; \n"""

with open(f"dummy_dummy_data.sql", 'w') as f:
    f.write(content)
