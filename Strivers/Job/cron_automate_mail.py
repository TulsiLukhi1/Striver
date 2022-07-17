from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User,auth
from django.contrib import messages
import requests
from bs4 import BeautifulSoup as bs
from django.core.mail import send_mail
from django.conf import settings
from .models import Job_details,Search_details,Update_details
from urllib.parse import quote



def send_mail():

    #collecting all user's interested category
    categorys = Update_details.objects.all()
    print(len(categorys))
    for category in categorys:

        search =  category.search
        url = 'https://internshala.com/jobs/'+search+'-jobs'
        print(url)
        req = requests.get(url)
        soup = bs(req.text,"html.parser")
        current_data=soup.find_all('div',class_="individual_internship")
        total_div = len(current_data)-1
        print(total_div)

        update_data = Update_details.objects.filter(search=search)
        print(update_data[0].total_div)
        
        if update_data[0].total_div != total_div :
            search_data = Search_details.objects.filter(search=search)

            if update_data[0].total_div < total_div :
                update_data[0].total_div=total_div
                update_data[0].save()
                for search in search_data:
                    job_name=(search.search.replace("%20"," ")).capitalize()
                    username = search.username
                    userdetail = User.objects.filter(username=username)
                    email = userdetail[0].email
                    print(email)
                    subject='About Job Update'
                    message=f'Hey {username}! New job added to the category  {job_name}  you have searched before \n Go and check it out using the link below!!\n{url} \n You can also visit our website and search about job...'
                    from_email = settings.EMAIL_HOST_USER
                    print("send mail")
                    print(job_name)
                    print("")

                    send_mail(subject, message, from_email, [email])

           
            
                update_data[0].total_div=total_div
                # print(f'total_div = {total_div}')
                update_data[0].total_div=total_div
                # print(f'after updating db {update_data[0].total_div}')  
                update_data[0].save()

    return 



