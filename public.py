from flask import*
from database import*
public=Blueprint('public',__name__)


def redirect_with_popup(view_name, **kwargs):
    redirect_url = url_for(view_name)
    return render_template('redirect_with_popup.html', redirect_url=redirect_url, **kwargs)


@public.route("/", methods=['GET', 'POST'])
def home():
    session.clear()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        q = "SELECT * FROM `login` WHERE `username`='%s' AND `password`='%s'" % (username, password)
        res = select(q)  # Assuming select function is defined elsewhere
        if not res:
            # flash('INCORRECT USERNAME OR PASSWORD')
            return """<script>alert('INCORRECT USERNAME OR PASSWORD');window.location='/'</script>"""
        else:
            session['lid'] = res[0]['login_id']
            if res[0]['usertype'] == 'admin':
                flash('HELLO ADMIN')
                title = "Lgoin Success :)"
                return redirect_with_popup(view_name='head.headoffice', request=request, title=title)
            elif res[0]['usertype'] == 'branch':
                o="select * from branch where login_id='%s'"%(session['lid'])
                rs=select(o)
                session['bid'] = rs[0]['branch_id']
                print(session['bid'],"session['bid']session['bid']session['bid']session['bid']session['bid']session['bid']")
                flash('HELLO BRANCH')
                title = "Login Success :)"
                return redirect_with_popup(view_name='branch.branchhome', request=request, title=title)
            elif res[0]['usertype'] == 'staff':
                o="select * from staff where login_id='%s'"%(session['lid'])
                rs=select(o)
                session['sid'] = rs[0]['staff_id']
                # print(session['bid'],"session['bid']session['bid']session['bid']session['bid']session['bid']session['bid']")
                # flash('HELLO Staff')
                title = "Login Success :)"
                return redirect_with_popup(view_name='staff.staffhome', request=request, title=title)
   
    return render_template("home.html")

# @public.route('/')
# def home():
#     return render_template("home.html")


# @public.route('/login',methods=['get','post'])
# def login():
#     if'login' in request.form:
#         uname=request.form['uname']
#         passw=request.form['password']
#         qry="select * from login where username='%s' and password='%s'"%(uname,passw)
#         res=select(qry)
#         if res:
#             session['lid']=res[0]['login_id']
#             if res:
#                 utype=res[0]['usertype']
                
#                 if utype=='admin':
#                     return redirect(url_for('cbi.cbi_home'))
#                 elif utype=='branch':
#                     a="select * from branch where login_id='%s'"%(session['lid'])
#                     q=select(a)
#                     if q:
#                         session['branch']=q[0]['branch_id']
                
#                     return redirect(url_for('branch.branch_home'))
#                 # elif utype=='user':
#                 #     a="select * from user where login_id='%s'"%(session['lid'])
#                 #     q=select(a)
#                 #     session['uid']=q[0]['user_id']
#                 #     return redirect(url_for('user.userhome'))
            
                
#     return render_template("loginn.html")





