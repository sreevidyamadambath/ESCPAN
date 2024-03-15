from flask import*
from database import*
branch=Blueprint('branch',__name__)

@branch.route('/branch')
def branch_home():
    return render_template('br_home.html')

@branch.route('/staff') 
def staff():
    if 'branch' in session:
        branch_id=session['branch']
    data={}
    qry="select * from staff where branch_id='%s'"%(branch_id)
    res=select(qry)
    data['staff']=res

    return render_template('staff.html',data=data)

@branch.route('/addcase',methods=['post','get'])
def addcase():
    data={}
    if 'branch' in session:
        branch_id=session['branch']
    if 'submit' in request.form:
        caseno=request.form['caseno']
        crime=request.form['crime']
        status=request.form['status']
        date=request.form['date']
        staff=request.form['staff']
        qry="insert into cases values(null,'%s','%s','%s','%s','%s')"%(branch_id,caseno,crime,status,date)
        insert(qry)

        

    return render_template('addcase.html',data=data)


    

@branch.route('/viewcase')
def viewcase():

    data={}
    if 'branch' in session:
        branch_id=session['branch']
    qry="select * from cases inner join branch using(branch_id,branch_id) where branch_id='%s'"%(branch_id)

    res=select(qry)
    data['viewcase']=res
    return render_template('viewcase.html',data=data)


@branch.route('/sendcomplaint',methods=['post','get'])
def sendcomplaint():
    data={

    }
    if 'branch' in session:
        branch_id=session['branch']
    if 'submit' in request.form:
        complaint=request.form['complaint']
        date=request.form['date']
        
        qry="insert into complaints values(null,'%s','%s','pending','%s')"%(branch_id,complaint,date)
        insert(qry)
    return render_template('sendcomplaint.html',data=data)

@branch.route('/viewreply')
def viewreply():
    data={}
    if 'branch' in session:
        branch_id=session['branch']
    
        
        qry="select * from complaints where sender_id='%s'"%(branch_id)
        res=select(qry)
        data['viewreply']=res
    return render_template('viewreply.html',data=data)
    
    
