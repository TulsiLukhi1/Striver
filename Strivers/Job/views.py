from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as bs
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from urllib3 import HTTPResponse
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render,redirect, HttpResponseRedirect

from .  models import SearchDetails

# Create your views here.

def index(request):
    if request.method == 'POST':
        search = request.POST['search']
        user = request.POST['user']
        siteurl = request.POST['siteurl']

        search_data=SearchDetails.objects.filter(username=user,search=search,siteurl=siteurl)
        if not search_data:
            data = SearchDetails(
                search=search,
                username=user,
                siteurl=siteurl
            )

            data.save()


        if siteurl=="https://internshala.com/jobs/" :

            url = siteurl + search + '-jobs'

            req = requests.get(url)
            soup = bs(req.text,"html.parser")

            header_data = soup.find_all('div',class_="individual_internship_header")
            job_data= soup.find_all('div',class_="individual_internship_details")

            job_titles_fun = []
            job_company_fun=[]
            job_durl_fun = []
            # job_exp_fun=[]
            # job_salary_fun=[]
            jon_location_fun=[]

            for h_data in header_data:
                
                j_url=h_data.div.div.a.get('href')
                job_durl_fun.append(j_url)
                

                title = h_data.div.div.a.text
                job_title_fun.append(title)
                # print(title)

                c_name = h_data.find('div',class_="company_name").a.text
                job_company_fun.append(c_name)


            
            for j_data in job_data:

                location=j_data.p.a.text
                job_locations_fun.append(location)





            total_div=len(job_titles_fun)
            update_data=UpdateDetails.objects.filter(search=search)
            if not update_data:
                data=UpdateDetails(siteurl=siteurl,search=search,total_div=total_div)
                data.save()
            else:
                if update_data[0].total_div != total_div :
                    update_data[0].total_div=total_div
                    update_data[0].save()


            job_detail_list = zip(job_titles_fun,job_company_fun,job_durl_fun,jon_location_fun)

            context = {
                'job_detail_list':job_detail_list
            }


        return render(request,'index.html',context)

    elif siteurl=="https://www.techgig.com/jobs/":
        return (request,'index.html',context)
    return render(request,'index.html')


        
    






    return render(request,'index.html')


def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass) 
            if user is not None:
                login(request, user)
                return redirect('/')
            messages.error(request,"Login Failed!! Please enter correct credentials :) ")
    else:            
        fm = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':fm})




def user_register(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        print("int post");
        if fm.is_valid():
            messages.success(request, 'Account created Successfully!')
            fm.save() 
            print("fm.save()")
            return render(request, 'accounts/login.html',{'form':fm})

    else:
        fm = SignUpForm()
        print("in else")
        return render(request, 'accounts/signup.html',{'form':fm})

    print("it not in any condition")

def user_logout(request):
    auth.logout(request)
    return redirect('login')


