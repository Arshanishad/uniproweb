import os
from flask import *
from werkzeug.utils import secure_filename
from unipro.maincode import cb
# from unipro.maincode import cb
from unipro.dbconnectionnew import *

app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login():

    username=request.form['uname']
    password=request.form['password']

    qry="select * from login where username=%s and password=%s"
    val=(username,password)
    res=selectone(qry,val)

    if res is None:
        return jsonify({'task':'invalid'})

    else:
        id= res['lid']
        return jsonify({'task':'success','lid':id,'type':res['type']})









@app.route("/register_students",methods=['POST'])
def register_students():
    print(request.form)
    course_id = request.form['courseid']
    firstname = request.form['fname']
    lastname = request.form['lname']
    dob= request.form['dob']
    genter = request.form['genter']
    college_id = request.form['collegeid']
    email = request.form['email']
    contact = request.form['contact']
    place = request.form['place']
    post = request.form['post']
    pin= request.form['pin']
    dept_id = request.form['deptid']
    username= request.form['uname']
    password= request.form['password']
    qry="insert into login values (null,%s,%s,'student')"
    val=(username,password)
    id = iud(qry,val)
    qry1="INSERT INTO `student`(`l_id`,`course_id`,`firstname`,`lastname`,`dob`,`genter`,`college_id`,`email`,`contact`,`place`,`post`,`pin`,`dept_id`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(id,course_id,firstname,lastname,dob,genter,college_id,email,contact,place,post,pin,dept_id)
    iud(qry1,val1)
    return jsonify({'task': 'registered'})



@app.route('/view_notification',methods=['POST'])
def view_notification():
    qry="SELECT `notification`.*,`course`.`course` FROM `notification` JOIN `course` ON `notification`.`course_id`=`course`.`course_id` "
    res=androidselectallnew(qry)
    print(res)
    return jsonify(res)



@app.route("/submit_abstract",methods=['POST'])
def submit_abstract():
    print(request.form)
    print(request.files)
    lid=request.form['lid']
    topic=request.form['topic']
    area=request.form['area']
    des=request.form['des']
    abstract = request.files['file']

    res=cb(des)
    if len(res)> 0:
        return jsonify({'task': 'failed'})

    print(abstract.filename)
    # abs=secure_filename(abstract.filename)
    # abstract.save(os.path.join('static/abstract',abs))

    import datetime
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    abstract.save('static/abstract/'+date+'.jpg')
    path = 'static/abstract/'+date+'.jpg'


    qry="insert into `project` values (null,%s,%s,%s,%s,%s,'pending',curdate())"
    val=(lid,topic,path,area,des)
    iud(qry,val)
    return jsonify({'task': 'success'})




@app.route("/search_project",methods=['post'])
def search_project():
    # des="Crimes are a common social problem affecting the quality of life and the economic"
    des=request.form['des']

    s=cb(des)

    s.append("0")
    ss=','.join(s)
    qry = "SELECT * FROM project where p_id in("+ss+")"
    res=selectall(qry)
    print(res)
    return jsonify(res)


# @app.route("/search_project1",methods=['POST'])
# def search_project1():
#     s = request.form['s']
#     print(s)
#     qry="SELECT * FROM `project` WHERE `topic` LIKE '%"+s+"%'"
#     # val=
#     res=androidselectallnew(qry)
#     return jsonify(res)



@app.route("/send_feedback",methods=['POST'])
def send_feedback():
    print(request.form)
    lid = request.form['lid']
    feedback = request.form['feedback']
    qry="insert into `feedback` values(null,%s,%s,curdate())"
    val=(lid,feedback,)
    iud(qry,val)
    return jsonify({'task': 'send'})






@app.route('/view_assignedwork',methods=['POST'])
def view_assignedwork():
    lid = request.form['lid']
    print(lid)
    # qry="SELECT `project`.topic,`assignwork`.*  FROM `project` JOIN `assignwork` ON `project`.`p_id`=`assignwork`.`p_id`"
    qry1="SELECT `project`.topic,`assignwork`.*,`teachers`.`firstname`,`lastname`  FROM `project` JOIN `assignwork` ON `project`.`p_id`=`assignwork`.`p_id` JOIN `teachers` ON `teachers`.`lid`=`assignwork`.`teacher_id` WHERE `assignwork`.`teacher_id`=%s"
    res=androidselectall(qry1,lid)
    print(res)
    return jsonify(res)





@app.route('/view_student',methods=['POST'])
def view_student():
    qry="SELECT `student`.*,`course`.`course` FROM `student` JOIN `course` ON `student`.`course_id`=`course`.`course_id`"
    res=androidselectallnew(qry)
    return jsonify(res)




@app.route('/view_feedback1',methods=['POST'])
def view_feedback1():
    qry="SELECT * FROM `feedback`"
    res=androidselectallnew(qry)
    return jsonify(res)


@app.route('/view_abstract',methods=['POST'])
def view_abstract():
    qry="SELECT * FROM `project` where status='pending'"
    res=androidselectallnew(qry)
    print(res)
    return jsonify(res)


@app.route('/accept_abstract',methods=['POST'])
def accept_abstract():
    print(request.form)
    pid=request.form['pid']
    qry="update project set  status='accepted' where p_id=%s"
    iud(qry,pid)
    return jsonify({'task': 'success'})

@app.route('/reject_abstract',methods=['POST'])
def reject_abstract():
    pid=request.form['pid']
    qry="update project set  status='rejected' where p_id=%s"
    iud(qry, pid)
    return jsonify({'task': 'reject'})




@app.route('/spinner_course',methods=['POST'])
def spinner_course():
    qry="select * from course"
    res=androidselectallnew(qry)
    print('================course', res)
    return jsonify(res)




@app.route('/spinner_college',methods=['POST'])
def spinner_college():
    print('esdrftgyhujimk,l')
    qry="SELECT * FROM college"
    res=androidselectallnew(qry)
    print('================',res)
    return jsonify(res)



@app.route('/spinner_department',methods=['POST'])
def spinner_department():
    # print('esdrftgyhujimk,l')
    qry="SELECT * FROM department"
    res=androidselectallnew(qry)
    print('================ dept',res)
    return jsonify(res)




app.run(host='0.0.0.0',port=5000)