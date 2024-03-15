from flask import*
from database import*
public=Blueprint('public',__name__)




@public.route('/')
def home():
    return render_template("home.html")


@public.route('/login',methods=['get','post'])
def login():
    if'login' in request.form:
        uname=request.form['uname']
        passw=request.form['password']
        qry="select * from login where username='%s' and password='%s'"%(uname,passw)
        res=select(qry)
        if res:
            session['lid']=res[0]['login_id']
            if res:
                utype=res[0]['usertype']
                
                if utype=='admin':
                    return redirect(url_for('cbi.cbi_home'))
                elif utype=='branch':
                    a="select * from branch where login_id='%s'"%(session['lid'])
                    q=select(a)
                    if q:
                        session['branch']=q[0]['branch_id']
                
                    return redirect(url_for('branch.branch_home'))
                # elif utype=='user':
                #     a="select * from user where login_id='%s'"%(session['lid'])
                #     q=select(a)
                #     session['uid']=q[0]['user_id']
                #     return redirect(url_for('user.userhome'))
            
                
    return render_template("login.html")





