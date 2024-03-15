from flask import*
from database import*
cbi=Blueprint('cbi',__name__)

@cbi.route('/admin')
def cbi_home():
    return render_template('admin_home.html')



@cbi.route('/managebranch',methods=['post','get'])
def viewbranch():
    data={}
    qry="select * from branch"
    res=select(qry)
    data['viewbranch']=res
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='delete':
        qry="delete from branch where branch_id='%s'"%(id)
        delete(qry)
        return ''' <script>alert("deleted successfully");window.location="/managebranch"</script>'''

    
    if 'submit' in request.form:
        branch=request.form['branch']
        state=request.form['state']
        district=request.form['district']
        address=request.form['address']
        pincode=request.form['pincode']
        phone=request.form['phone']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']

        qry1="insert into login values(null,'%s','%s','branch')"%(username,password)
        login_id=insert(qry1)

        qry="insert into branch values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(login_id,branch,state,district,address,pincode,phone,email)
        insert(qry)

    return render_template('managebranch.html',data=data)

@cbi.route('/branch_home',methods=['POST','GET'])
def updatebranch():
    id=request.args['id']
    data={}
    qry4="select * from branch where branch_id='%s'"%(id)
    res=select(qry4)
    data['viewbranch']=res
    if 'upd' in request.form:
        branch=request.form['branch']   
        state=request.form['state']
        district=request.form['district']
        address=request.form['address']
        pincode=request.form['pincode']
        phone=request.form['phone']
        email=request.form['email']
        qry4="update branch set branch_name='%s',state='%s',district='%s',address='%s',pincode='%s',phone='%s',email='%s' where branch_id='%s'"%(branch,state,district,address,pincode,phone,email,id)
        update(qry4)

        return '''<script>alert("updated");window.location="/managebranch"</script>'''
    
    return render_template('branch_home.html',data=data)   

@cbi.route('/viewdivision',methods=['POST','GET']) 
def viewdivision():
    data={}
    qry="select * from division inner join branch using(branch_id,branch_id)"
    res=select(qry)
    data['viewdivision']=res
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='delete':
        qry="delete from division where d_id='%s'"%(id)
        delete(qry)
        return ''' <script>alert("deleted successfully");window.location="/viewdivision"</script>'''
    if action=='update':
        qry6="select * from division where d_id='%s'"%(id)
        data['up']=select(qry6)
        if 'update' in request.form:
            division=request.form['division']
                 
            q="update division set division_name='%s' where d_id='%s'"%(division,id)
            update(q)
            return '''<script>alert("update successfull");window.locatioin="/registration"</script>'''

    qr1="select * from branch"
    res=select(qr1)
    data['brview']=res
    if 'submit' in request.form:
        branch=request.form['br']
        division=request.form['division']
        username=request.form['username']
        password=request.form['password']
        qry1="insert into login values(null,'%s','%s','division')"%(username,password)
        login_id=insert(qry1)
        qry="insert into division values(null,'%s','%s')"%(branch,division)
        insert(qry)


    return render_template('viewdivision.html',data=data)


        

@cbi.route('/viewstaff',methods=['POST','GET']) 
def viewstaff():
    data={}
    qry="select * from staff"
    res=select(qry)
    data['staffview']=res
    qry1="select * from division"
    res=select(qry1)
    data['divview']=res
    qry2="select * from branch"
    res=select(qry2)
    data['brview']=res
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='delete':
        qry="delete from staff where s_id='%s'"%(id)
        delete(qry)
        return ''' <script>alert("deleted successfully");window.location="/viewstaff"</script>'''
    if action=='update':
        qry6="select * from staff where s_id='%s'"%(id)
        data['up']=select(qry6)
        if 'update' in request.form:
            division=request.form['div']
            branch=request.form['br']
            dob=request.form['dob']
            name=request.form['name']
            state=request.form['state']
            district=request.form['district']
            address=request.form['address']
            pincode=request.form['pincode']
            phone=request.form['phone']
            email=request.form['email']
            
                 
            q="update staff set division_id='%s',branch_id='%s',dob='%s',full_name='%s',state='%s',district='%s',address='%s',pincode='%s',phone='%s',email='%s' where s_id='%s'"%(division,branch,dob,name,state,district,address,pincode,phone,email,id)
            update(q)
            return '''<script>alert("update successfull");window.locatioin="/viewstaff"</script>'''
    qr1="select * from staff"
    res=select(qr1)
    data['staff']=res
    if 'submit' in request.form:
        dob=request.form['dob']
        name=request.form['name']
        state=request.form['state']
        district=request.form['district']
        address=request.form['address']
        pincode=request.form['pincode']
        phone=request.form['phone']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        branch=request.form['br']
        division=request.form['div']
        qry1="insert into login values(null,'%s','%s','staff')"%(username,password)
        login_id=insert(qry1)
        qry="insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(login_id,branch,division,dob,name,state,district,address,pincode,phone,email)
        insert(qry)
    return render_template('viewstaff.html',data=data)


@cbi.route('/viewcase') 
def viewcase():
    data={}
    qry="select * from cases inner join branch using(branch_id,branch_id)"
    res=select(qry)
    data['viewcase']=res
    return render_template('viewcase.html',data=data)

@cbi.route('/viewcomplaints') 
def viewcomplaints():
    data={}
    qry="select * from complaints"
    res=select(qry)
    data['viewcomplaints']=res
    print(res)
    return render_template('viewcomplaints.html',data=data)   

@cbi.route('/sendreply',methods=['get','post'])
def sendreply():
    id=request.args['id']
    data={}
    q="select * from complaints where complaint_id='%s'"%(id)
    res=select(q)
    if res:
        data['viewcomplaint']=res
        
    if 'send' in request.form:
        reply=request.form['reply']
        
        qry="update complaints set reply='%s' where complaint_id='%s'"%(reply,id)
        update(qry)
    
    return render_template("sendreply.html",data=data)






