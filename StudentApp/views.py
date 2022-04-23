from django.shortcuts import render, redirect
from StudentApp.forms import StudentForm,UserForm,User_InfoForm,Registration_Form,Contact_Us_form,NotisForm,EventForm
from StudentApp.models import StudentDB,User_Info,Registration,Contact_Us,Notis,Event
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from StudentDB import settings
from django.core.mail import send_mail


# Create your views here.
@login_required(login_url='/login')
def Add_Students(request):
    Userdata = User.objects.get(id=request.session['id'])
    form = StudentForm
    superuser = request.session['superuser']
    staff = request.session['staff']
    if request.method == 'POST':
        data = StudentForm(request.POST, request.FILES)
        if data.is_valid:
            file = request.FILES['Picture']
            name = file.name
            loc = open('StudentApp/static/media/upload/' + name, 'wb+')
            data.save()
            for i in file.chunks():
                loc.write(i)
            msg = 'The Student is Added'
            return render(request, 'Add_Students.html', {'form': form, 'msg':msg,'super': superuser, 'staff': staff,'Userdata':Userdata})
        else:
            msg = "Wrong Information"
            return render(request, 'Add_Students.html', {'form': form, "msg": msg,'super': superuser, 'staff': staff,'Userdata':Userdata})
    return render(request, 'Add_Students.html', {'form': form,'super': superuser, 'staff': staff,'Userdata':Userdata})



@login_required(login_url='/login')
def Full_Details(request,id):
    Userdata = User.objects.get(id=request.session['id'])
    data = StudentDB.objects.get(Id=id)
    superuser = request.session['superuser']
    staff = request.session['staff']
    return render(request,'Full_Details.html',{'data':data,'super': superuser, 'staff': staff,'Userdata':Userdata})



def index(request):
    data = Notis.objects.all()
    return render(request,'index.html',{'data':data})


@login_required(login_url='/login')
def View_Students(request):
    Userdata = User.objects.get(id=request.session['id'])
    superuser = request.session['superuser']
    staff = request.session['staff']
    data = StudentDB.objects.all
    if request.method == 'POST':
        roll = request.POST['search']
        data = StudentDB.objects.all().filter(Roll=roll)
    return render(request,'View_Students.html', {'data': data,'super': superuser, 'staff': staff,'Userdata':Userdata})



@login_required(login_url='/login')
def Student_Update(request,id):
    Userdata = User.objects.get(id=request.session['id'])
    superuser = request.session['superuser']
    staff = request.session['staff']
    data = StudentDB.objects.get(Id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect(View_Students)
        else:
            msg = 'Update failed... Invalid Data'
            return render(request,'Student_Update.html',{'data':data,'msg':msg,'super': superuser, 'staff': staff,'Userdata':Userdata})
    return render(request, 'Student_Update.html', {'data': data,'super': superuser, 'staff': staff,'Userdata':Userdata})



@login_required(login_url='/login')
def add_user(request):
    Userdata = User.objects.get(id=request.session['id'])
    form1 = UserForm()
    form2 = User_InfoForm()
    superuser = request.session['superuser']
    staff = request.session['staff']
    if superuser:
        if request.method == "POST":
            data1 = UserForm(request.POST)
            data2 = User_InfoForm(request.POST, request.FILES)
            if data1.is_valid() and data2.is_valid():
                if request.POST['password'] == request.POST['c_password']:
                    s = data1.save()
                    s.set_password(s.password)
                    s.save()
                    f = request.FILES['Image']
                    name = f.name
                    loc = open('StudentApp/static/media/user/' + name, 'wb+')
                    data2.save()
                    for i in f.chunks():
                        loc.write(i)
                    return redirect('/')
                else:
                    msg = "Password not matched"
                    return render(request, 'add_user.html', {'form1': form1, 'form2': form2,'msg': msg,'super': superuser, 'staff': staff,'Userdata':Userdata})
            else:
                msg = "data not Valid"
                return render(request,'add_user.html',{'form1': form1, 'form2': form2,'msg': msg,'super': superuser, 'staff': staff,'Userdata':Userdata})

        return render(request, 'add_user.html', {'form1': form1, 'form2': form2,'super': superuser, 'staff': staff,'Userdata':Userdata})
    else:
        return redirect(login_fun)


def login_fun(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        attn = authenticate(username=username,password=password)
        if attn:
            login(request,attn)
            data = User.objects.get(username=username)
            request.session['username'] = username
            request.session['id'] = data.id
            request.session['superuser'] = data.is_superuser
            request.session['staff'] = data.is_staff
            return redirect('/Admin_Page')
        else:
            msg = "Login failed"
            return render(request, 'login.html',{'msg':msg})

    return render(request,'login.html')



def logout_fun(request):
    logout(request)
    return redirect('/login')




def Registration_Fun(request):
    form = Registration_Form
    if request.method == 'POST':
        subject = "School Admission"
        to = request.POST['Email']
        msg_body = "Hi \n"\
                   "Thanks for Applying our School\n" \
                   "We take Best Care of your Child\n" \
                   "We will Contact with You soon\n" \
                   "Thank You"
        data = Registration_Form(request.POST, request.FILES)
        if data.is_valid:
            file = request.FILES['Student_Picture']
            name = file.name
            loc = open('StudentApp/static/media/Registration/' + name, 'wb+')
            data.save()
            send_mail(subject, msg_body, settings.EMAIL_HOST_USER, [to])
            for i in file.chunks():
                loc.write(i)
                return redirect(Rg_Msg)
        else:
            msg = "Request not Acsapted ! Chack Your Input "
            return render(request, 'Registration.html', {'form': form, "msg": msg})
    return render(request, 'Registration.html', {'form': form})




@login_required(login_url='/login')
def Admin_Page(request):
    Userdata = User.objects.get(id=request.session['id'])
    superuser = request.session['superuser']
    staff = request.session['staff']
    return render(request, 'Admin_Page.html',{'super':superuser,'staff':staff,'Userdata':Userdata})


@login_required(login_url='/login')
def View_Registration(request):
    Userdata = User.objects.get(id=request.session['id'])
    data = Registration.objects.all()
    superuser = request.session['superuser']
    staff = request.session['staff']
    return render(request,'View_Registration.html',{'data':data,'super': superuser, 'staff': staff,'Userdata':Userdata})



@login_required(login_url='/login')
def logout_fun(request):
    logout(request)
    return redirect('/login')



@login_required(login_url='/login')
def Std_Reg_pro(request,id):
    Userdata = User.objects.get(id=request.session['id'])
    data = Registration.objects.get(Id=id)
    superuser = request.session['superuser']
    staff = request.session['staff']
    return render(request,'Std_Reg_pro.html',{'data':data,'super':superuser,'staff':staff,'Userdata':Userdata})



@login_required(login_url='/login')
def User_pro(request):
    data = User.objects.get(id=request.session['id'])
    img = User_Info.objects.get(Id=request.session['id'])
    superuser = request.session['superuser']
    staff = request.session['staff']
    return render(request, 'User_pro.html', {'data': data, 'img': img, 'super': superuser, 'staff': staff})



@login_required(login_url='/login')
def Delete_Student(request,id):
    superuser = request.session['superuser']
    if superuser:
        data = StudentDB.objects.get(Id=id)
        data.delete()
    return redirect(View_Students)



def About_Us(request):
    return render(request,'About_Us.html')



def Contact(request):
    form = Contact_Us_form
    if request.method == 'POST':
        data = Contact_Us_form(request.POST)
        if data.is_valid():
            data.save()
            msg =  'Thank You ! Be With Us'
            return render(request,'Contact_Us.html',{'msg':msg,"form":form})
        else:
            msg = 'Wrong Input'
            return render(request,'Contact_Us.html',{"form":form,'msg':msg})
    return render(request,'Contact_Us.html',{'form':form})



@login_required(login_url='/login')
def Show_Msg(request):
    superuser = request.session['superuser']
    staff = request.session['staff']
    Userdata = User.objects.get(id=request.session['id'])
    data = Contact_Us.objects.all()
    return render(request,'Show_Msg.html',{'data':data,'Userdata':Userdata,'super': superuser, 'staff': staff})


def Rg_Msg(request):
    return render(request,'Rg_Msg.html')


@login_required(login_url='/login')
def Admission_delete(request,id):
    superuser = request.session['superuser']
    if superuser:
        data = Registration.objects.get(Id=id)
        data.delete()
        return redirect(View_Registration)
    else:
        return redirect(login_fun)



@login_required(login_url='/login')
def Pub_msg_delete(request,id):
    superuser = request.session['superuser']
    if superuser:
        data = Contact_Us.objects.get(Id=id)
        data.delete()
        return redirect(Show_Msg)
    else:
        return redirect(login_fun)




def Add_notis(request):
    form = NotisForm
    data = Notis.objects.all()
    Userdata = User.objects.get(id=request.session['id'])
    if request.method == 'POST':
        data = NotisForm(request.POST, request.FILES)
        data.save()
    return render(request,'Add_notis.html',{'form': form,'data':data,'Userdata':Userdata})


def del_notis(request,id):
    data = Notis.objects.get(Id=id)
    data.delete()
    return redirect(Add_notis)


def Add_Event(request):
    form = EventForm
    data = Event.objects.all()
    Userdata = User.objects.get(id=request.session['id'])
    if request.method == 'POST':
        data = EventForm(request.POST, request.FILES)
        if data.is_valid:
            file = request.FILES['Event_Pic']
            name = file.name
            loc = open('StudentApp/static/media/Event/' + name, 'wb+')
            data.save()
            for i in file.chunks():
                loc.write(i)
    return render(request,'Add_Event.html',{'form':form,'data':data,'Userdata':Userdata})

def Show_Event(request):
    data = Event.objects.all()
    return render(request,'Event.html',{'data':data})


def del_event(request,id):
    data = Event.objects.get(Id=id)
    data.delete()
    return redirect(Add_Event)