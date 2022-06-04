import faker,random,array,datetime
from random import randint
from datetime import date
from datetime import datetime

fake = faker.Faker()
today = date.today()

content = "";

DUMMY_DATA_NUMBER = 10;
TABLE_NAME = "organisations";
TABLE_COLUMNS = [ "organisation_name", "abbreviation","category","postal_code","street","town"]
catlist=["comp","uni","rs"]

for i in range(DUMMY_DATA_NUMBER):
    organisation_id = i
    organisation_name = fake.company()
    abbreviation = organisation_name[0:4]
    postal_code = fake.postcode()
    street = fake.street_address()
    category=random.choice(catlist)
    town = fake.city()
    content += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{organisation_name}", "{abbreviation}","{category}", "{postal_code}", "{street}", "{town}");\n'


DUMMY_DATA_NUMBER = 200;
TABLE_NAME = "researchers";
TABLE_COLUMNS = [ "first_name", "last_name", "sex","date_birth","res_start_date", "town", "res_organisation_id"]
mylist = ["male", "female", "non-binary"]

res_per_org = array.arr = ([],[],[],[],[],[],[],[],[],[])
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

ev=[]
sco=[]
DUMMY_DATA_NUMBER = 200;
TABLE_NAME = "projects";
TABLE_COLUMNS = [ "proj_title", "proj_amount", "summary", "start_date", "expiry_date","evaluation_grade", "evaluation_date", "proj_executive_id", "proj_organisation_id", "scientific_officer_id", "evaluator_id", "program_id"]
proj_org= []

from datetime import datetime
for i in range(DUMMY_DATA_NUMBER):
    proj_title = fake.word()
    proj_amount = fake.random_number(5)
    summary = fake.paragraph()
    start_year = str(randint(2015,2024))
    start_monthday = fake.date()
    start_month = start_monthday[5:7]
    start_day = start_monthday[8:10]
    start_date = start_year + '-' + start_month + '-' + start_day

    duration = randint(1,4)
    expiry_year = int(start_year) + duration
    expiry_monthday = fake.date()
    expiry_month = expiry_monthday[5:7]
    expiry_day = expiry_monthday[8:10]
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
TABLE_COLUMNS = ["del_summary","del_proj_id"]


for i in range(DUMMY_DATA_NUMBER):
    del_summary = fake.paragraph()
    del_proj_id = randint(1,200)
    content += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ( "{del_summary}", "{del_proj_id}");\n'

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

for i in range(DUMMY_DATA_NUMBER):
    pr_proj_id = i+1
    for i in range(int(0.5*no_res_per_org[proj_org[i]-1])):
        pr_researcher_id = random.choice(res_per_org[proj_org[i]-1])
        content += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{pr_researcher_id}", "{pr_proj_id}");\n'



with open(f"dummy_dummy_data.sql", 'w') as f:
    f.write(content)
