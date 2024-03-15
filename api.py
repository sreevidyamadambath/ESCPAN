from flask import*
from database import*
api=Blueprint('api',__name__)

@api.route('/stafflogin')
def login():
    data={}
    username=request.args["username"]
    password=request.args["password"]
          
    qry="select * from login where username='%s' and password='%s'"%(username,password)
    res=select(qry)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
        
    
    return str(data)

@api.route('/staffprofile')
def staffprofile():
    data={}
    lid=request.args["lid"]
    qry="select * from staff inner join branch on staff.branch_id=branch.branch_id INNER JOIN division on staff.division_id=division.d_id where staff.login_id='%s'"%(lid)
    
    res=select(qry)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    
     
    return str(data)