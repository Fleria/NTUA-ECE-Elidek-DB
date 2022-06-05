from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_mysqldb import MySQL
from elidek import app, el ## initially created by __init__.py, need to be used here


@app.route("/", methods = ["GET","POST"])
def index():
    return render_template("landing.html", pageTitle = "Landing Page")



@app.route("/deliverables", methods = ["GET", "POST"])
def showdel():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from deliverables;")
        column_names = [i[0] for i in cur.description]
        deliverables = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("deliverables.html",deliverables=deliverables)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/deliverables/insert", methods = ["GET", "POST"])
def insdel():
    if(request.method == "POST"):
         del_summary = str(request.form.get("del_summary"))
         del_proj_id = int(request.form.get("del_proj_id"))
         cur = el.connection.cursor()
         query = f"INSERT INTO deliverables(del_summary,del_proj_id) VALUES ('{del_summary}',{del_proj_id});"
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showdel'))
    cur = el.connection.cursor()
    cur.execute("select proj_id from projects order by proj_id;")
    column_names = [i[0] for i in cur.description]
    projids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    return render_template("deliverables-insert.html",projids=projids)

@app.route("/deliverables/delete", methods = ["GET", "POST"])
def deldel():
    if(request.method == "POST"):
         del_id = int(request.form.get("del_id"))
         cur = el.connection.cursor()
         query = f"delete from deliverables where del_id = {del_id};"
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showdel'))
    cur = el.connection.cursor()
    cur.execute("select del_id from deliverables order by del_id;")
    column_names = [i[0] for i in cur.description]
    delids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    return render_template("deliverables-delete.html",delids=delids)

@app.route("/deliverables/update", methods = ["GET", "POST"])
def updel():
    if(request.method == "POST"):
         del_id = int(request.form.get("del_id"))
         del_summary = str(request.form.get("del_summary"))
         del_proj_id = int(request.form.get("del_proj_id"))
         cur = el.connection.cursor()
         query = f"update deliverables set del_summary = '{del_summary}',del_proj_id = {del_proj_id} where del_id = {del_id};"
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showdel'))
    cur = el.connection.cursor()
    cur.execute("select del_id from deliverables order by del_id;")
    column_names = [i[0] for i in cur.description]
    delids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    cur.execute("select proj_id from projects order by proj_id;")
    column_names = [i[0] for i in cur.description]
    projids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    return render_template("deliverables-update.html",delids=delids,projids=projids)

@app.route("/executives", methods = ["GET", "POST"])
def showexec():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from executives;")
        column_names = [i[0] for i in cur.description]
        executives = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("executives.html",executives=executives)
    except Exception as e:
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/executives/insert", methods = ["GET", "POST"])
def insexec():
    if(request.method == "POST"):
         ename = str(request.form.get("ename"))
         cur = el.connection.cursor()
         query = f"INSERT INTO executives(ename) VALUES ('{ename}');"
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showexec'))
    return render_template("executives-insert.html")

@app.route("/executives/delete", methods = ["GET", "POST"])
def delexec():
    if(request.method == "POST"):
         executive_id = int(request.form.get("executive_id"))
         cur = el.connection.cursor()
         query = f"delete from executives where executive_id = {executive_id};"
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showexec'))
    cur = el.connection.cursor()
    cur.execute("select executive_id from executives order by executive_id;")
    column_names = [i[0] for i in cur.description]
    exids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    return render_template("executives-delete.html",exids=exids)

@app.route("/executives/update", methods = ["GET", "POST"])
def upexec():
    if(request.method == "POST"):
         executive_id = int(request.form.get("executive_id"))
         ename = str(request.form.get("ename"))
         cur = el.connection.cursor()
         query = f"update executives set ename = '{ename}' where executive_id = {executive_id};"
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showexec'))
    cur = el.connection.cursor()
    cur.execute("select executive_id from executives order by executive_id;")
    column_names = [i[0] for i in cur.description]
    exids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    projids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    return render_template("executives-update.html",exids=exids)


@app.route("/funds", methods = ["GET", "POST"])
def showfunds():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from funds;")
        column_names = [i[0] for i in cur.description]
        funds = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("funds.html",funds=funds)
    except Exception as e:
        return render_template("landing.html", pageTitle = "Landing Page")



@app.route("/organisations", methods = ["GET", "POST"])
def showorg():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from organisations;")
        column_names = [i[0] for i in cur.description]
        organisations = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("organisations.html",organisations=organisations)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")


@app.route("/organisations/insert", methods = ["GET", "POST"])
def insorg():
    if(request.method == "POST"):
         organisation_name = str(request.form.get("organisation_name"))
         abbreviation = str(request.form.get("abbreviation"))
         category = str(request.form.get("category"))
         postal_code = str(request.form.get("postal_code"))
         street = str(request.form.get("street"))
         town = str(request.form.get("town"))
         cur = el.connection.cursor()
         query = f"insert into organisations(organisation_name,abbreviation,category,postal_code,street,town) VALUES ('{organisation_name}','{abbreviation}','{category}','{postal_code}','{street}','{town}');"
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showorg'))
    cur = el.connection.cursor()
    cur.execute("select distinct category from organisations;")
    column_names = [i[0] for i in cur.description]
    cats = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    return render_template("organisations-insert.html",cats=cats)


@app.route("/organisations/delete", methods = ["GET", "POST"])
def delorg():
    if(request.method == "POST"):
         organisation_id = int(request.form.get("organisation_id"))
         cur = el.connection.cursor()
         query = f"delete from organisations where organisation_id = {organisation_id};"
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showorg'))
    cur = el.connection.cursor()
    cur.execute("select organisation_id from organisations order by organisation_id;")
    column_names = [i[0] for i in cur.description]
    orgids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    return render_template("organisations-delete.html",orgids=orgids)

@app.route("/organisations/update", methods = ["GET", "POST"])
def uporg():
    if(request.method == "POST"):
         organisation_id = int(request.form.get("organisation_id"))
         organisation_name = str(request.form.get("organisation_name"))
         abbreviation = str(request.form.get("abbreviation"))
         category = str(request.form.get("category"))
         postal_code = str(request.form.get("postal_code"))
         street = str(request.form.get("street"))
         town = str(request.form.get("town"))
         cur = el.connection.cursor()
         query = f"update organisations set organisation_name = '{organisation_name}',abbreviation = '{abbreviation}',category='{category}',postal_code='{postal_code}',street='{street}',town='{town}' where organisation_id = {organisation_id};"
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showorg'))
    cur = el.connection.cursor()
    cur.execute("select organisation_id from organisations order by organisation_id;")
    column_names = [i[0] for i in cur.description]
    orgids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    cur.execute("select distinct category from organisations;")
    column_names = [i[0] for i in cur.description]
    cats = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    return render_template("organisations-update.html",orgids=orgids,cats=cats)


@app.route("/organisations_telephones", methods = ["GET", "POST"])
def showorg_tel():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from organisations_telephones order by ot_organisation_id;")
        column_names = [i[0] for i in cur.description]
        organisations_telephones = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("organisations_telephones.html",organisations_telephones= organisations_telephones)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/programs", methods = ["GET", "POST"])
def showprog():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from programs;")
        column_names = [i[0] for i in cur.description]
        programs = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("programs.html", programs=programs)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/programs/insert", methods = ["GET", "POST"])
def insprog():
    if(request.method == "POST"):
         program_name = str(request.form.get("program_name"))
         administration = str(request.form.get("administration"))
         cur = el.connection.cursor()
         query = f"insert into programs(program_name,administration) VALUES ('{program_name}','{administration}');"
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showprog'))
    cur = el.connection.cursor()
    return render_template("programs-insert.html")

@app.route("/programs/delete", methods = ["GET", "POST"])
def delprog():
    if(request.method == "POST"):
         program_id = int(request.form.get("program_id"))
         cur = el.connection.cursor()
         query = f"delete from programs where program_id = {program_id};"
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showprog'))
    cur = el.connection.cursor()
    cur.execute("select program_id from programs order by program_id;")
    column_names = [i[0] for i in cur.description]
    progids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    return render_template("programs-delete.html",progids=progids)

@app.route("/programs/update", methods = ["GET", "POST"])
def upprog():
    if(request.method == "POST"):
         program_id = int(request.form.get("program_id"))
         program_name = str(request.form.get("program_name"))
         administration = str(request.form.get("administration"))
         cur = el.connection.cursor()
         query = f"update programs set program_name = '{program_name}',administration = '{administration}' where program_id ={program_id};"
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showprog'))
    cur = el.connection.cursor()
    cur.execute("select program_id from programs order by program_id;")
    column_names = [i[0] for i in cur.description]
    progids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    return render_template("programs-update.html",progids=progids)

@app.route("/projects", methods = ["GET", "POST"])
def showproj():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from projects;")
        column_names = [i[0] for i in cur.description]
        projects = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("projects.html", projects=projects)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/projects/insert", methods = ["GET", "POST"])
def insproj():
    if(request.method == "POST"):
         proj_title=str(request.form.get("proj_title"))
         proj_amount = int(request.form.get("proj_amount"))
         summary = str(request.form.get("summary"))
         start_date=str(request.form.get("start_date"))
         expiry_date=str(request.form.get("expiry_date"))
         evaluation_grade=int(request.form.get("evaluation_grade"))
         evaluation_date=str(request.form.get("evaluation_date"))
         proj_executive_id=int(request.form.get("proj_executive_id"))
         proj_organisation_id=int(request.form.get("proj_organisation_id"))
         evaluator_id=int(request.form.get("evaluator_id"))
         scientific_officer_id=int(request.form.get("scientific_officer_id"))
         program_id=int(request.form.get("program_id"))
         cur = el.connection.cursor()
         query = f'INSERT INTO projects (proj_title,proj_amount,summary,start_date,expiry_date,evaluation_grade,evaluation_date,proj_executive_id, proj_organisation_id,evaluator_id, scientific_officer_id,program_id) values ("{proj_title}","{proj_amount}", "{summary}","{start_date}" ,"{expiry_date}","{evaluation_grade}","{evaluation_date}","{proj_executive_id}","{proj_organisation_id}","{scientific_officer_id}","{evaluator_id}","{program_id}");'
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showproj'))
    cur = el.connection.cursor()
    cur.execute("select executive_id from executives order by executive_id;")
    column_names = [i[0] for i in cur.description]
    execids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    cur.execute("select organisation_id from organisations order by organisation_id;")
    column_names = [i[0] for i in cur.description]
    orgids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    #query= f'select researcher_id from researchers where res_organisation_id != "{organisation}" order by researcher_id;'
    #cur.execute(query)
    cur.execute("select researcher_id from researchers order by researcher_id;")
    column_names = [i[0] for i in cur.description]
    evids =[dict(zip(column_names, entry)) for entry in cur.fetchall()]
    cur.execute("select researcher_id from researchers order by researcher_id;")
    column_names = [i[0] for i in cur.description]
    scids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    cur.execute("select program_id from programs order by program_id;")
    column_names = [i[0] for i in cur.description]
    progids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    return render_template("projects-insert.html",execids=execids, orgids=orgids,evids=evids,scids=scids,progids=progids)


@app.route("/projects_researchers", methods = ["GET", "POST"])
def showproj_res():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from projects_researchers;")
        column_names = [i[0] for i in cur.description]
        projects_researchers = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("projects_researchers.html", projects_researchers=projects_researchers)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/research_centers", methods = ["GET", "POST"])
def showres_cen():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from research_centers;")
        column_names = [i[0] for i in cur.description]
        research_centers = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("research_centers.html", research_centers=research_centers)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/researchers", methods = ["GET", "POST"])
def showres():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from researchers;")
        column_names = [i[0] for i in cur.description]
        researchers = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("researchers.html", researchers=researchers)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/researchers/insert", methods = ["GET", "POST"])
def insres():
    if(request.method == "POST"):
         first_name = str(request.form.get("first_name"))
         last_name = str(request.form.get("last_name"))
         sex = str(request.form.get("sex"))
         date_birth = str(request.form.get("date_birth"))
         res_start_date = str(request.form.get("res_start_date"))
         town = str(request.form.get("town"))
         res_organisation_id = int(request.form.get("res_organisation_id"))
         cur = el.connection.cursor()
         query = f"insert into researchers(first_name,last_name,sex,date_birth,res_start_date,town,res_organisation_id) VALUES ('{first_name}','{last_name}','{sex}','{date_birth}','{res_start_date}' ,'{town}' ,'{res_organisation_id}');"
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showres'))
    cur = el.connection.cursor()
    cur.execute("select distinct res_organisation_id from researchers order by res_organisation_id;")
    column_names = [i[0] for i in cur.description]
    rorgids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    return render_template("researchers-insert.html",rorgids=rorgids)


@app.route("/researchers/delete", methods = ["GET", "POST"])
def delres():
    if(request.method == "POST"):
         researcher_id = int(request.form.get("researcher_id"))
         cur = el.connection.cursor()
         query = f"delete from researchers where researcher_id = {researcher_id};"
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showres'))
    cur = el.connection.cursor()
    cur.execute("select researcher_id from researchers order by researcher_id;")
    column_names = [i[0] for i in cur.description]
    resids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    return render_template("researchers-delete.html",resids=resids)

@app.route("/researchers/update", methods = ["GET", "POST"])
def upres():
    if(request.method == "POST"):
         researcher_id = int(request.form.get("researcher_id"))
         first_name = str(request.form.get("first_name"))
         last_name = str(request.form.get("last_name"))
         sex = str(request.form.get("sex"))
         date_birth = str(request.form.get("date_birth"))
         res_start_date = str(request.form.get("res_start_date"))
         town = str(request.form.get("town"))
         res_organisation_id = int(request.form.get("res_organisation_id"))
         cur = el.connection.cursor()
         query = f"update researchers set first_name = '{first_name}', last_name = '{last_name}', sex='{sex}', date_birth='{date_birth}', res_start_date='{res_start_date}',town='{town}', res_organisation_id = {res_organisation_id} where researcher_id = {researcher_id};"
         cur.execute(query)
         el.connection.commit()
         return redirect(url_for('showres'))
    cur = el.connection.cursor()
    cur.execute("select researcher_id from researchers order by researcher_id;")
    column_names = [i[0] for i in cur.description]
    resids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    cur.execute("select organisation_id from organisations order by organisation_id;")
    column_names = [i[0] for i in cur.description]
    rorgids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    return render_template("researchers-update.html",resids=resids,rorgids=rorgids)


@app.route("/scientific_fields", methods = ["GET", "POST"])
def showsci_fld():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from scientific_fields;")
        column_names = [i[0] for i in cur.description]
        scientific_fields = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("scientific_fields.html", scientific_fields=scientific_fields)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/scientific_fields_projects", methods = ["GET", "POST"])
def showsci_fld_proj():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from scientific_fields_projects;")
        column_names = [i[0] for i in cur.description]
        scientific_fields_projects = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("scientific_fields_projects.html", scientific_fields_projects=scientific_fields_projects)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/universities", methods = ["GET", "POST"])
def showuni():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from universities;")
        column_names = [i[0] for i in cur.description]
        universities = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("universities.html", universities=universities)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")


@app.route("/query1prog", methods = ["GET", "POST"])
def query1prog():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from programs;")
        column_names = [i[0] for i in cur.description]
        query1prog = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("query1prog.html", query1prog=query1prog)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/query1projform", methods = ["GET", "POST"])
def query1projform():

    if(request.method == "POST"):
        duration = int(request.form.get("duration"))
        proj_executive_id = int(request.form.get("proj_executive_id"))
        start_date = str(request.form.get("start_date"))
        query = f"select * from projects where duration = {duration} and proj_executive_id = {proj_executive_id} and start_date ={start_date} "
        cur = el.connection.cursor()
        cur.execute(query)
        column_names = [i[0] for i in cur.description]
        query1proj = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("query1projshow.html",query1proj=query1proj)

    cur = el.connection.cursor()
    cur.execute("select distinct duration from projects order by duration;")
    column_names = [i[0] for i in cur.description]
    projdurs = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    cur.execute("select distinct proj_executive_id from projects order by proj_executive_id;")
    column_names = [i[0] for i in cur.description]
    exids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    cur.execute("select start_date from projects order by start_date;")
    column_names = [i[0] for i in cur.description]
    dates = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    return render_template("query1projform.html",projdurs=projdurs,exids=exids,dates=dates)


@app.route("/query2view1", methods = ["GET", "POST"])
def query2view1():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from view_1;")
        column_names = [i[0] for i in cur.description]
        query2view1 = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("query2view1.html", query2view1=query2view1)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/query2view2", methods = ["GET", "POST"])
def query2view2():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from view_2;")
        column_names = [i[0] for i in cur.description]
        query2view2 = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("query2view2.html", query2view2=query2view2)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")



@app.route("/query3", methods = ["GET", "POST"])
def query3():
    try:
        if(request.method == "POST"):
            sfname = str(request.form.get("sfname"))
            cur = el.connection.cursor()
            query = f"select scientific_field_name, proj_title, first_name, last_name from scientific_fields a inner join scientific_fields_projects on a.scientific_field_name = sfp_scientific_field_name inner join projects on proj_id=sfp_proj_id inner join projects_researchers on pr_proj_id = proj_id inner join researchers on pr_researcher_id=researcher_id where scientific_field_name = '{sfname}' and expiry_date>curdate();"
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            query3 = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
            return render_template("query3.html",query3=query3)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")


@app.route("/query4", methods = ["GET", "POST"])
def query4():
    try:
        cur = el.connection.cursor()
        cur.execute("""select orga organisation, DATE_FORMAT(std1, "%Y") first_year,DATE_FORMAT(std2, "%Y") second_year, count1 projects_per_year from (select * from (select organisation_name orga, proj_title t1, start_date std1,count(*) count1 from projects inner join organisations on organisation_id = proj_organisation_id group by organisation_name,DATE_FORMAT(start_date, "%Y") having count1>=2) a inner join (select organisation_name orgb, proj_title t2, start_date std2, count(*) count2 from projects inner join organisations on organisation_id = proj_organisation_id group by organisation_name,DATE_FORMAT(start_date, "%Y") having count2>=2) b on t1!=t2) c where orga=orgb and count1=count2 and CAST(DATE_FORMAT(std1, "%Y") AS int)+1 = CAST(DATE_FORMAT(std2, "%Y") AS int);""")
        column_names = [i[0] for i in cur.description]
        query4 = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("query4.html", query4=query4)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/query5", methods = ["GET", "POST"])
def query5():
    try:
        cur = el.connection.cursor()
        cur.execute("call FindTop3;")
        column_names = [i[0] for i in cur.description]
        query5 = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("query5.html", query5=query5)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")


@app.route("/query6", methods = ["GET", "POST"])
def query6():
    try:
        cur = el.connection.cursor()
        cur.execute("select * from (select pr_researcher_id, count(*) as projcount from (select proj_id from projects where expiry_date>curdate()) active_proj inner join projects_researchers on proj_id=pr_proj_id inner join researchers on pr_researcher_id = researcher_id where age<40 group by pr_researcher_id)a where projcount = (select max(projcount) as maximum from (select pr_researcher_id, count(*) as projcount from (select proj_id from projects where expiry_date>curdate()) active_proj inner join projects_researchers on proj_id=pr_proj_id inner join researchers on pr_researcher_id = researcher_id where age<40 group by pr_researcher_id order by projcount desc)b);")
        column_names = [i[0] for i in cur.description]
        query6 = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("query6.html", query6=query6)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/query7", methods = ["GET", "POST"])
def query7():
    try:
        cur = el.connection.cursor()
        cur.execute("select ename,organisation_name,sum(proj_amount) as total_amount from projects inner join organisations on proj_organisation_id= organisation_id inner join executives on proj_executive_id = executive_id where category ='comp' group by proj_executive_id order by sum(proj_amount) desc limit 5;")
        column_names = [i[0] for i in cur.description]
        query7 = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("query7.html", query7=query7)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/query8", methods = ["GET", "POST"])
def query8():
    try:
        cur = el.connection.cursor()
        cur.execute("select first_name,last_name,projcount from (select pr_researcher_id,count(*) as projcount from projects_researchers where NOT EXISTS (select distinct del_proj_id from deliverables where pr_proj_id=del_proj_id) group by pr_researcher_id)a inner join researchers on researcher_id= pr_researcher_id where projcount>4;")
        column_names = [i[0] for i in cur.description]
        query8 = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        return render_template("query8.html", query8=query8)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("errors/404.html", pageTitle = "Not Found"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("errors/500.html", pageTitle = "Internal Server Error"), 500
