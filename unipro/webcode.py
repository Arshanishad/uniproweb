from urllib import request
from flask import *
import functools
# from pip._internal.network import session

from unipro.dbconnectionnew import *

app=Flask(__name__)
app.secret_key="123"

def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return redirect("/")
        return func()
    return secure_function

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route("/",methods=['GET','POST'])
def main():
    return render_template("LOGIN.HTML")


@app.route('/login',methods=['GET','POST'])
def login():
    username=request.form['textfield']
    password=request.form['textfield2']

    qry="select * from login where username=%s and password=%s "
    val=(username,password)
    res=selectone(qry,val)
    print(res)

    # print("=============================================")
    # print(session['lid'])
    if res is None:
        return'''<script>alert("invalid"); window.location="/"</script>'''

    elif res['type']=='university':
        session['lid'] = res['lid']
        return redirect('/u_home')
    elif res['type'] == 'college':
        session['lid'] = res['lid']
        return redirect('/c_home')
    else:
        return '''<script>alert("invalid"); window.location="/"</script>'''

@app.route("/u_home",methods=['GET','POST'])
@login_required
def u_home():
    return render_template("univesity/unoiversity_home.html")



@app.route("/addcollege",methods=['GET','POST'])
@login_required
def addcollege():
    return render_template("univesity/addcollege.html")

@app.route('/acollege',methods=['POST'])
@login_required
def acollege():
    collegename=request.form['textfield']
    collegeemail=request.form['textfield2']
    establishedyear =request.form['textfield10']
    phone=request.form['textfield3']
    place=request.form['textfield4']
    post=request.form['textfield5']
    pin=request.form['textfield7']
    username=request.form['textfield6']
    password=request.form['textfield9']
    qry="INSERT INTO `login` (`username`,`password`,`type`) VALUES(%s,%s,'college')"
    val=(username,password)
    id=iud(qry,val)
    qry="INSERT INTO `college`(`c_lid`,`college_name`,`established_year`,`college_email`,`phone`,`place`,`post`,`pin`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(str(id),collegename,establishedyear,collegeemail,phone,place,post,pin)
    iud(qry,val)
    return '''<script>alert("added"); window.location="/viewcollege#get-started"</script>'''

@app.route("/adddept", methods=['GET', 'POST'])
@login_required
def adddept():
    return render_template("univesity/ADDDEPARTMENT.html")

@app.route("/adddept1",methods=['GET', 'POST'])
@login_required
def adddept1():
    department=request.form['textfield']
    qry="insert into `department`(`department`) values (%s)"
    val=(department)
    iud(qry,val)
    return '''<script>alert("added"); window.location="/viewdepartment#get-started"</script>'''









@app.route("/editcollege",methods=['GET','POST'])
@login_required
def editcollege():
    id=request.args.get('id')
    # print("==============================================")
    # print(id)
    session['c_id']=id
    qry = "SELECT * FROM college WHERE `c_id`=%s"
    res = selectone(qry,id)
    print(res)
    return render_template("univesity/EDITCOLLEGE.html",data=res)


@app.route("/editcollege_post",methods=['GET','POST'])
@login_required
def editcollege_post():
    college_name=request.form['textfield']
    established_year=request.form['textfield7']
    college_email=request.form['textfield2']
    phone=request.form['textfield3']
    place=request.form['textfield4']
    post=request.form['textfield5']
    pin=request.form['textfield6']
    qry="update college set college_name=%s,established_year=%s,college_email=%s,phone=%s,place=%s,post=%s,pin=%s where c_id=%s"
    val=(college_name,established_year,college_email,phone,place,post,pin,str(session['c_id']))
    iud(qry,val)
    return '''<script>alert("updated"); window.location="/viewcollege#get-started"</script>'''


@app.route("/viewcollege",methods=['GET','POST'])
@login_required
def viewcollege():
    qry= "SELECT * FROM college"
    res=selectall(qry)
    print(res)
    return render_template("univesity/VIEW COLLEGE.HTML",data=res)

@app.route("/dlt_clg",methods=['GET','POST'])
def dlt_clg():
    id = request.args.get('id')
    qry = "DELETE FROM `college` WHERE c_id=%s"
    iud(qry,id)
    # print(res)
    return '''<script>alert("deleted"); window.location="/viewcollege"</script>'''







@app.route("/addcourse",methods=['GET','POST'])
@login_required
def addcourse():
    qry="select * from department"
    res=selectall(qry)
    return render_template("univesity/ADD COURSE.html",data=res)

@app.route("/addcourse_post",methods=['GET','POST'])
@login_required
def addcourse_post():
    dept_id=request.form['select']
    course=request.form['textfield']
    duration=request.form['textfield2']
    fees=request.form['textfield3']
    qry = "insert into `course`(`dept_id`,`course`,`duration`,`fees`) values (%s,%s,%s,%s)"
    val = (dept_id,course,duration,fees)
    iud(qry, val)
    return '''<script>alert("added"); window.location="/viewcourse#get-started"</script>'''

@app.route("/viewcourse",methods=['GET','POST'])
@login_required
def viewcourse():
    qry = "SELECT course.*,`department`.* FROM `course` INNER JOIN `department` ON `course`.`dept_id`=`department`.`d_id`"
    res = selectall(qry)
    # print(res)
    return render_template("univesity/VIEW COURSE.html", data=res)

@app.route("/dlt_viewcourse",methods=['GET','POST'])
def dlt_viewcourse():
    id = request.args.get('id')
    qry = "DELETE FROM `course` WHERE course_id=%s"
    iud(qry,id)
    # print(res)
    return '''<script>alert("deleted"); window.location="/viewcourse"</script>'''


@app.route("/editcourse",methods=['GET','POST'])
def editcourse():
    id=request.args.get('id')
    session['cid']=id
    qry1="select * from department "
    res1=selectall(qry1)
    qry="SELECT course.*,`department`.* FROM `course` INNER JOIN `department` ON `course`.`dept_id`=`department`.`d_id` WHERE `course`.`course_id`=%s"
    res=selectone(qry,id)
    # print(res)
    return render_template("univesity/EDIT COURSE.html",data=res,data1=res1)

@app.route("/editcourse_post",methods=['GET','POST'])
def editcourse_post():
    dept_id = request.form['select']
    course = request.form['textfield']
    duration = request.form['textfield2']
    fees = request.form['textfield3']
    qry = "update course set dept_id=%s,course=%s,duration=%s,fees=%s where course_id=%s"
    val = (dept_id, course, duration, fees,session['cid'])
    iud(qry, val)
    return '''<script>alert("updated"); window.location="/viewcourse#get-started"</script>'''


@app.route("/viewdepartment",methods=['GET','POST'])
@login_required
def viewdepartment():
    qry = "SELECT * FROM department"
    res = selectall(qry)
    print(res)
    return render_template("univesity/viewdepartment.html",data=res)


@app.route("/dlt_department",methods=['GET','POST'])
@login_required
def dlt_department():
    id = request.args.get('id')
    qry = "DELETE FROM `department` WHERE d_id=%s"
    iud(qry,id)
    # print(res)
    return '''<script>alert("deleted"); window.location="/viewdepartment"</script>'''



@app.route("/sendnotification",methods=['GET','POST'])
@login_required
def sendnotification():
    qry="select * from course"
    val=selectall(qry)
    return render_template("univesity/SENDNOTIFICATION.html",data=val)

@app.route("/sentnotification_post", methods=['GET', 'POST'])
@login_required
def sentnotification_post():
    sem = request.form['select2']
    notification = request.form['textarea']
    course=request.form['select']
    qry = "insert into `notification` values(null,%s,%s,%s,curdate())"
    val = (course,sem,notification)
    iud(qry,val)
    return '''<script>alert("added"); window.location="/viewnotification#get-started"</script>'''


@app.route("/viewnotification",methods=['GET','POST'])
@login_required
def viewnotification():
    qry="SELECT `course`.*,`notification`.* FROM `course` JOIN `notification` ON `course`.course_id=`notification`.course_id"
    res = selectall(qry)
    # print(res)
    return render_template("univesity/view_notification.html",data=res)



@app.route("/dlt_notification",methods=['GET','POST'])
def dlt_notification():
    id = request.args.get('id')
    qry = "DELETE FROM `notification` WHERE n_id=%s"
    iud(qry,id)
    # print(res)
    return '''<script>alert("deleted"); window.location="/viewnotification"</script>'''













@app.route("/viewproject",methods=['GET','POST'])
@login_required
def viewproject():
    qry="select* from project"
    res=selectall(qry)
    print(res)
    return render_template("univesity/VIEWPROJECT.html",data=res)


@app.route("/viewfeedback",methods=['GET','POST'])
@login_required
def viewfeedback():
    return render_template("univesity/VIEWFEEDBACK.html")




@app.route("/viewfeedback1", methods=['GET', 'POST'])
@login_required
def viewfeedback1():
    type=request.form['select']
    if type =='STUDENT':
        qry="select student.firstname,student.lastname,feedback.* from student join feedback on student.l_id=feedback.lid"
        res=selectall(qry)
        return render_template("univesity/VIEWFEEDBACK.html",data=res,t=type)
    else:
        qry='select teachers.firstname,teachers.lastname,feedback.* from teachers join feedback on teachers.lid=feedback.lid'
        res=selectall(qry)
        return render_template("univesity/VIEWFEEDBACK.html",data=res,t=type)




















@app.route("/c_home",methods=['GET','POST'])
@login_required
def c_home():
    return render_template("colleges/college_home.html")









@app.route("/view_teachers",methods=['GET','POST'])
def view_teachers():
    qry="SELECT `department`.*,`teachers`.* FROM `department` INNER JOIN `teachers` ON `department`.`d_id`=`teachers`.`department_id`"
    res=selectall(qry)
    print(res)
    return render_template("colleges/ADD&MANAGE TEACHERS.html",data=res)


@app.route("/reg_teachers",methods=['GET','POST'])
@login_required
def reg_teachers():
    qry="SELECT * FROM `department`"
    res=selectall(qry)
    print(res)
    return render_template("colleges/REGISTER TEACHERS.html",data=res)


@app.route("/register_teachers",methods=['GET','POST'])
@login_required
def register_teachers():
    firstname = request.form['textfield']
    lastname = request.form['textfield2']
    gender = request.form['radio']
    department= request.form['select']
    pin = request.form['textfield4']
    place= request.form['textfield5']
    post= request.form['textfield6']
    phone= request.form['textfield7']
    email= request.form['textfield8']
    username= request.form['textfield9']
    password= request.form['textfield10']
    qry="insert into login values (null,%s,%s,'teacher')"
    val=(username,password)
    res=iud(qry,val)
    qry1="INSERT INTO `teachers`(`college_id`,`firstname`,`lastname`,`gender`,`department_id`,`pin`,`lid`,`place`,`post`,`phone`,`email`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(session['lid']),firstname,lastname,gender,department,pin,str(res),place,post,phone,email)
    res1=iud(qry1,val1)
    return '''<script>alert("Registered"); window.location="/view_teachers#get-started"</script>'''





@app.route("/update_teachers",methods=['GET','POST'])
@login_required
def update_teachers():
    id=request.args.get('id')
    session['t_id']=id
    qry1 = "SELECT * FROM `department`"
    res1 = selectall(qry1)
    # print(res)
    # return render_template("colleges/REGISTER TEACHERS.html", data=res)
    qry="SELECT `department`.*,`teachers`.* FROM `department` INNER JOIN `teachers` ON `department`.`d_id`=`teachers`.`department_id` where teacher_id=%s"
    res=selectone(qry,id)
    return render_template("colleges/UPDATE TEACHERS.html",data=res,data1=res1)



@app.route("/update_teachers_post", methods=['GET', 'POST'])
@login_required
def update_teachers_post():
    firstname=request.form['textfield']
    lastname=request.form['textfield2']
    gender=request.form['radiobutton']
    department=request.form['select']
    pin=request.form['textfield34']
    place=request.form['textfield32']
    post=request.form['textfield33']
    phone=request.form['textfield35']
    qry="update teachers set firstname=%s,lastname=%s,gender=%s,pin=%s,place=%s,post=%s,phone=%s where teacher_id=%s"
    val=(firstname,lastname,gender,pin,place,post,phone,str(session['t_id']))
    iud(qry,val)
    return '''<script>alert("updated"); window.location="/view_teachers#get-started"</script>'''

@app.route("/assign_teachers",methods=['GET','POST'])
@login_required
def assign_teachers():
    qry="SELECT department.department,department.d_id,project.topic,p_id FROM  student JOIN project ON student.`l_id`=`project`.`s_id` JOIN `course` ON `course`.`course_id`=`student`.`course_id` JOIN `department` ON `department`.`d_id`=`course`.`dept_id` WHERE `project`.`status`='pending'"
    val=selectall(qry)
    return render_template("colleges/ASSIGN_WORK_TO_TEACHERS.html",data=val)


@app.route("/assign",methods=['GET','POST'])
@login_required
def assign():
    pid=request.args.get('id')
    session['pid']=pid
    did=request.args.get('did')
    qry="select * from teachers where department_id=%s"
    val=selectall2(qry,did)
    return render_template("colleges/ASSIGN.html",data=val)


@app.route("/assign_post",methods=['GET','POST'])
@login_required
def assign_post():
    teacher_id=request.form['select']
    qry="insert into assignwork values(null,%s,%s,curdate(),'assigned')"
    val=(teacher_id,session['pid'])
    iud(qry,val)
    qry1="update project set status='assigned' where p_id=%s"
    iud(qry1,session['pid'])

    return '''<script>alert("assigned"); window.location="/assign_teachers#get-started"</script>'''





@app.route("/viewcourse1",methods=['GET','POST'])
@login_required
def viewcourse1():
    qry="select * from course"
    val=selectall(qry)
    return render_template("colleges/VIEW COUSRE.html",data=val)








@app.route("/viewstudent",methods=['GET','POST'])
@login_required
def viewstudent():
    qry = "select * from student"
    val = selectall(qry)

    return render_template("colleges/VIEW STUDENT.html",data=val)



@app.route("/viewtopics",methods=['GET','POST'])
@login_required
def viewtopics():
   qry="select * from project"
   val=selectall(qry)
   return render_template("colleges/VIEW TOPICS.html",data=val)


@app.route("/viewproject1",methods=['GET','POST'])
@login_required
def viewproject1():
    qry="select * from project"
    val=selectall(qry)
    return render_template("colleges/VIEWPROJECT1.html",data=val)





@app.route("/viewfeedback2",methods=['GET','POST'])
@login_required
def viewfeedback2():
        return render_template("colleges/VIEWFEEDBACK1.html")

@app.route("/viewfeedback3", methods=['GET', 'POST'])
@login_required
def viewfeedback3():
    type=request.form['select']
    if type =='STUDENT':
        qry="select student.firstname,student.lastname,feedback.* from student join feedback on student.l_id=feedback.lid"
        res=selectall(qry)
        return render_template("colleges/VIEWFEEDBACK1.html",data=res,t=type)
    else:
        qry="select teachers.firstname,teachers.lastname,feedback.* from teachers join feedback on teachers.lid=feedback.lid"
        res=selectall(qry)
        return render_template("colleges/VIEWFEEDBACK1.html",data=res,t=type)




@app.route("/workassigned",methods=['GET','POST'])
@login_required
def workassigned():
    qry="SELECT `assignwork`.`date`,`teachers`.`firstname`,`teachers`.`lastname`,`project`.`topic` FROM `assignwork` JOIN `teachers` ON `assignwork`.`teacher_id`=`teachers`.`lid` JOIN `project` ON `project`.`p_id`=`assignwork`.`p_id`"
    val=selectall(qry)
    return render_template("colleges/workassign.html",data=val)



@app.route("/dlt_teachers",methods=['GET','POST'])
@login_required
def dlt_teachers():
    id = request.args.get('id')
    qry = "DELETE FROM `teachers` WHERE teacher_id=%s"
    iud(qry,id)
    # print(res)
    return '''<script>alert("deleted"); window.location="/view_teachers"</script>'''

app.run(debug=True)
