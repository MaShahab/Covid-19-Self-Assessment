from collections import OrderedDict
import mysql.connector
import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import itertools
import re
from sklearn import tree
from sklearn.datasets import make_blobs
from sklearn.metrics import precision_score
from email.header import Header
from email.utils import formataddr


class Patient:
    def __init__(self, name, age, sex, mail):
        self.name = name
        self.age = age
        self.sex = sex
        self.mail = mail


patient_specifications = []


def mainFunction():
    name = input("Enter your name : ")  # Breath shortnes
    while name.isnumeric():
        name = input("Enter your name : ")

    while True:
        try:
            age = int(input('Enter your age: '))
            while age not in range(10, 101):
                age = int(input('Enter your age carefully: '))
                if age > 10 or age < 101:
                    break
                break
            break
        except:
            print("That's not a valid age!")

    sex = input('Enter your gender : (male/female) ')
    while sex != 'male' and sex != 'female':
        sex = input('Enter your gender : (male/female) ')
    if sex == 'female':
        sex_int = 0
    elif sex == 'male':
        sex_int = 1
    email = input("Enter your email address : ")
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        email = input("Enter your email address carefully: ")

    patient = Patient(name, age, sex, email)

    while True:
        try:
            Q1 = int(input("What's your fever degree?"))  # Fever or chills
            if Q1 not in range(35, 42):
                Q1 = int(input("Enter your fever degree carefully: "))
            break
        except:
            print("That's not a valid fever degree!")
    try:
        Q2 = input("Are you feeling Cough ? (y/n) ")  # Cough
        while Q2 != 'y' and Q2 != 'n':
            Q2 = input('Please answer enter y as yes or n as no : ')
    except:
        Q2 = input('Please answer enter y as yes or n as no : ')

    Q3 = input("Are you feeling Shortness of breath ? (y/n)")  # Breath shortnes
    while Q3 != 'y' and Q3 != 'n':
        Q3 = input('Please answer enter y as yes or n as no : ')

    Q4 = input("Are you feeling Fatigue ? (y/n)")  # Fatigue
    while Q4 != 'y' and Q4 != 'n':
        Q4 = input('Please answer enter y as yes or n as no : ')
    Q5 = input("Are you feeling Muscle or body aches ? (y/n)")  # Body ache
    while Q5 != 'y' and Q5 != 'n':
        Q5 = input('Please answer enter y as yes or n as no : ')
    Q6 = input("Are you feeling Headache ? (y/n)")  # Head ache
    while Q6 != 'y' and Q6 != 'n':
        Q6 = input('Please answer enter y as yes or n as no : ')
    Q7 = input("Are you feeling loss of taste or smell ? (y/n)")  # Loss taste
    while Q7 != 'y' and Q7 != 'n':
        Q7 = input('Please answer enter y as yes or n as no : ')
    Q8 = input("Are you feeling Sore throat ? (y/n)")  # Sore throat
    while Q8 != 'y' and Q8 != 'n':
        Q8 = input('Please answer enter y as yes or n as no : ')
    Q9 = input("Are you feeling Congestion or runny nose ? (y/n)")  # Congestion or runny nose
    while Q9 != 'y' and Q9 != 'n':
        Q9 = input('Please answer enter y as yes or n as no : ')
    Q10 = input("Are you feeling Nausea or vomiting ? (y/n)")  # Nausea or vomiting
    while Q10 != 'y' and Q10 != 'n':
        Q10 = input('Please answer enter y as yes or n as no : ')
    Q11 = input("Are you feeling Diarrhea ? (y/n)")  # Diarrhea
    while Q11 != 'y' and Q11 != 'n':
        Q11 = input('Please answer enter y as yes or n as no : ')

    patient_specifications.append([{'Name': name}, {'Age': age}, {'Sex': sex_int}, {'Fever Degree': Q1}, {'Cough': Q2}
                                      , {'Breath shortness': Q3}, {'Fatigue': Q4}, {'Body ache': Q5}, {'Headache': Q6}
                                      , {'Loss taste': Q7}, {'Sore throat': Q8}, {'Nose congestion': Q9}
                                      , {'Nausea or vomiting': Q10}, {'Diarrhea': Q11}])

    merged = list(itertools.chain(*patient_specifications))
    print(merged)
    print("Please wait. Machine is learning ...")

    # if Q1 == 'n':
    #     Q1 = 0
    # else:
    #     Q1 = 1
    if Q2 == 'n':
        Q2 = 0
    else:
        Q2 = 1
    if Q3 == 'n':
        Q3 = 0
    else:
        Q3 = 1
    if Q4 == 'n':
        Q4 = 0
    else:
        Q4 = 1
    if Q5 == 'n':
        Q5 = 0
    else:
        Q5 = 1
    if Q6 == 'n':
        Q6 = 0
    else:
        Q6 = 1
    if Q7 == 'n':
        Q7 = 0
    else:
        Q7 = 1
    if Q8 == 'n':
        Q8 = 0
    else:
        Q8 = 1
    if Q9 == 'n':
        Q9 = 0
    else:
        Q9 = 1
    if Q10 == 'n':
        Q10 = 0
    else:
        Q10 = 1
    if Q11 == 'n':
        Q11 = 0
    else:
        Q11 = 1

    merged_str = " ".join(str(x) for x in merged)

    admin_mail = 'mahshahab@gmail.com'
    password = "Shahab1374!"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Self Assessment Results"
    msg['From'] = str(Header('support@mshahabedin.ir', 'UTF-8', 50, 'M.Shahabedin'))
    msg['To'] = admin_mail

    # Create the body of the message (a plain-text and an HTML version).
    text = "New record is registered following below:"
    html = f"""\
        <html>
          <head></head>
          <body>
            <p>Hi there, A new record is registered by following below: </p>
            <em>Name: {patient.name}, </em>
            <em>Age: {patient.age}, </em>
            <em>Sex: {patient.sex}, </em>
            <em>Fever-Degree: {Q1}, </em>
            <em>Cough: {Q2}, </em>
            <em>Breath-Shortness: {Q3}, </em>
            <em>Fatigue: {Q4}, </em>
            <em>Body-Ache: {Q5}, </em>
            <em>Head-Ache: {Q6}, </em>
            <em>Loss-Taste: {Q7}, </em>
            <em>Sore-Throat: {Q8}, </em>
            <em>Nose-Congestion: {Q9}, </em>
            <em>Nausea or Vomiting: {Q10}, </em>
            <em>Diarrhea: {Q11}</em>
          </body>
        </html>
        """

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    server = smtplib.SMTP('mail.mshahabedin.ir: 26')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

    # msg = MIMEMultipart()
    # message = "New suspected case detected as below :" + merged_str
    # password = "Shahab1374!"
    # msg['From'] = "support@mshahabedin.ir"
    # msg['To'] = "mahshahab@gmail.com"
    # msg['Subject'] = "New patient record registered"
    #
    # # add in the message body
    # msg.attach(MIMEText(message, 'plain'))
    #
    # # create server
    # server = smtplib.SMTP('mail.mshahabedin.ir: 26')
    #
    # server.starttls()
    #
    # # Login Credentials for sending the mail
    # server.login(msg['From'], password)
    #
    # # send the message via the server.
    # server.sendmail(msg['From'], msg['To'], msg.as_string())
    #
    # server.quit()
    #
    # print("Your information have been sent to server successfully")

    patients_id_list = []
    patients_age_list = []
    patients_sex_list = []
    patients_fever_list = []
    patients_cough_list = []
    patients_breath_shortness_list = []
    patients_fatigue_list = []
    patients_body_ache_list = []
    patients_head_ache_list = []
    patients_loss_taste_list = []
    patients_sore_throat_list = []
    patients_nose_congestion_list = []
    patients_nausea_list = []
    patients_diarrhea_list = []
    patients_result = []
    patients_age_list_int = []
    patients_sex_list_int = []
    patients_fever_list_int = []

    r = requests.get("http://mshahabedin.ir/suspected_covid")
    soup = BeautifulSoup(r.text, 'html.parser')

    val_id = soup.find_all("td", {"class": "patient_id"})
    for i in range(0, len(val_id)):
        patients_id_list.append(val_id[i].string)

    val_age = soup.find_all("td", {"class": "patient_age"})
    for i in range(0, len(val_age)):
        patients_age_list.append(val_age[i].string)

    val_sex = soup.find_all("td", {"class": "patient_sex"})
    for i in range(0, len(val_sex)):
        patients_sex_list.append(val_sex[i].string)

    val_fever = soup.find_all("td", {"class": "patient_fever"})
    for i in range(0, len(val_fever)):
        patients_fever_list.append(val_fever[i].string)

    val_cough = soup.find_all("td", {"class": "patient_cough"})
    for i in range(0, len(val_cough)):
        if len(val_cough[i]) == 0:
            patients_cough_list.append(0)
        else:
            patients_cough_list.append(1)

    val_breath = soup.find_all("td", {"class": "patient_breath_shortness"})
    for i in range(0, len(val_breath)):
        if len(val_breath[i]) == 0:
            patients_breath_shortness_list.append(0)
        else:
            patients_breath_shortness_list.append(1)

    val_fatigue = soup.find_all("td", {"class": "patient_fatigue"})
    for i in range(0, len(val_fatigue)):
        if len(val_fatigue[i]) == 0:
            patients_fatigue_list.append(0)
        else:
            patients_fatigue_list.append(1)

    val_body_ache = soup.find_all("td", {"class": "patient_body_ache"})
    for i in range(0, len(val_body_ache)):
        if len(val_body_ache[i]) == 0:
            patients_body_ache_list.append(0)
        else:
            patients_body_ache_list.append(1)

    val_head_ache = soup.find_all("td", {"class": "patient_head_ache"})
    for i in range(0, len(val_head_ache)):
        if len(val_head_ache[i]) == 0:
            patients_head_ache_list.append(0)
        else:
            patients_head_ache_list.append(1)

    val_loss_taste = soup.find_all("td", {"class": "patient_loss_taste"})
    for i in range(0, len(val_loss_taste)):
        if len(val_loss_taste[i]) == 0:
            patients_loss_taste_list.append(0)
        else:
            patients_loss_taste_list.append(1)

    val_sore_throat = soup.find_all("td", {"class": "patient_sore_throat"})
    for i in range(0, len(val_sore_throat)):
        if len(val_sore_throat[i]) == 0:
            patients_sore_throat_list.append(0)
        else:
            patients_sore_throat_list.append(1)

    val_nose_congestion = soup.find_all("td", {"class": "patient_nose_congestion"})
    for i in range(0, len(val_nose_congestion)):
        if len(val_nose_congestion[i]) == 0:
            patients_nose_congestion_list.append(0)
        else:
            patients_nose_congestion_list.append(1)

    val_nausea = soup.find_all("td", {"class": "patient_nausea"})
    for i in range(0, len(val_nausea)):
        if len(val_nausea[i]) == 0:
            patients_nausea_list.append(0)
        else:
            patients_nausea_list.append(1)

    val_diarrhea = soup.find_all("td", {"class": "patient_diarrhea"})
    for i in range(0, len(val_diarrhea)):
        if len(val_diarrhea[i]) == 0:
            patients_diarrhea_list.append(0)
        else:
            patients_diarrhea_list.append(1)

    result = soup.find_all("p", {"class": "result"})
    for i in range(0, len(result)):
        patients_result.append(result[i].string)

    for i in range(0, len(patients_age_list)):
        patients_age_list_int.append(int(patients_age_list[i]))

    for i in range(0, len(patients_sex_list)):
        if patients_sex_list[i] == ' زن ':
            patients_sex_list_int.append(0)
        else:
            patients_sex_list_int.append(1)

    for i in range(0, len(patients_fever_list)):
        patients_fever_list_int.append(int(patients_fever_list[i]))

    Symptoms_list = [
        'age', 'sex', 'fever', 'cough', 'breath shortness', 'fatigue', 'body ache', 'head ache', 'los taste',
        'sore throat', 'nose congestion', 'nausea', 'diarrhea', 'result'
    ]

    patients_results_en = []
    for i in range(0, len(patients_result)):
        if patients_result[i] == 'مثبت':
            patients_results_en.append("positive")
        else:
            patients_results_en.append("negative")

    with open('records.csv', "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        # writer.writerow(Symptoms_list)
        for i in range(0, len(patients_result)):
            writer.writerow([patients_age_list_int[i],
                             patients_sex_list_int[i],
                             patients_fever_list_int[i],
                             patients_cough_list[i],
                             patients_breath_shortness_list[i],
                             patients_fatigue_list[i],
                             patients_body_ache_list[i],
                             patients_head_ache_list[i],
                             patients_loss_taste_list[i],
                             patients_sore_throat_list[i],
                             patients_nose_congestion_list[i],
                             patients_nausea_list[i],
                             patients_diarrhea_list[i],
                             patients_results_en[i]])

    x = []
    y = []

    with open('records.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        for line in data:
            x.append(line[0:13])
            y.append(line[13])

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x, y)

    new_data = [[age, sex_int, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11]]
    answer = clf.predict(new_data)
    print('Result: ' + answer[0])
    print('To see more details, you can check your email inbox')

    # requests.get("http://mshahabedin.ir/new_patient/28/0/37/0/1/0/0/0/1/0/0/0/1/0")
    # requests.get("http://mshahabedin.ir/new_patient/"+str(age)+'/'+str(sex_int)+'/'+str(Q1)+'/'+str(Q2)+'/'+str(Q3)+'/'+
    #              str(Q4)+'/'+str(Q5)+'/'+str(Q6)+'/'+str(Q7)+'/'+str(Q8)+'/'+str(Q9)+'/'+str(Q10)+'/'+str(Q11)+'/'+str(answer[0]))

    binary_result = 0
    if (answer[0] == 'negative'):
        binary_result = 0
    elif (answer[0] == 'positive'):
        binary_result = 1

    # print(str("http://mshahabedin.ir/new_patient/"+str(age)+'/'+str(sex_int)+'/'+str(Q1)+'/'+str(Q2)+'/'+str(Q3)+'/'
    #           +str(Q4)+'/'+str(Q5)+'/'+str(Q6)+'/'+str(Q7)+'/'+str(Q8)+'/'+str(Q9)+'/'+str(Q10)+'/'+str(Q11)+'/'+str(binary_result)))

    # Post to DataBase
    requests.get(str("http://mshahabedin.ir/new_patient/" + str(age) + '/' + str(sex_int) + '/' + str(Q1) + '/' + str(
        Q2) + '/' + str(Q3) + '/'
                     + str(Q4) + '/' + str(Q5) + '/' + str(Q6) + '/' + str(Q7) + '/' + str(Q8) + '/' + str(
        Q9) + '/' + str(Q10) + '/' + str(Q11) + '/' + str(binary_result)))

    # new_data_merged = list(itertools.chain(*new_data))

    y_true = [Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11]
    y_pred = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    precision = precision_score(y_true, y_pred, average='micro')
    # print(precision)

    user_email = patient.mail
    password = "Shahab1374!"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Self Assessment Results"
    msg['From'] = str(Header('support@mshahabedin.ir', 'UTF-8', 50, 'M.Shahabedin'))
    msg['To'] = user_email

    # Create the body of the message (a plain-text and an HTML version).
    text = "Dear " + patient.name + ' Hello and greetings;\n Your information was recorded as follows: '
    html = f"""\
    <html>
      <head></head>
      <body>
        <p>
            Dear {patient.name} Hello and greetings;
        </p>
        <p>
            Your information was registered as following: 
        </p>
        <h4>User Specification</h4>
        <p>Name: {patient.name}, &nbsp;  Age: {patient.age}, &nbsp; Gender: {patient.sex}</p>
        <h4>Symptoms</h4>
        <p>Fever-Degree: {Q1}, &nbsp; Cough: {Q2}, &nbsp; 
Breath-Shortness: {Q3}, &nbsp; Fatigue: {Q4}, &nbsp; Body-Ache: {Q5}, &nbsp; Head-Ache: {Q6}, &nbsp; Loss-Taste: {Q7}
, &nbsp; Sore-Throat: {Q8}, &nbsp; Nose-Congestion: {Q9}, &nbsp; Nausea or Vomiting: {Q10}, &nbsp; Diarrhea: {Q11}</p>
        <hr>
        <p>As according the data which achieved by tens cases which registered on our database, it seems the result 
of your situation must be <b>{answer[0]}</b>. It's obvious machine result can't be deterministic and only medical 
experiment can announce the definite result</p>
<p>Also your registered symptoms show exists about <b>{int(precision * 100)}%</b> equality with all positive symptoms 
there</p> 
      </body>
    </html>
    """

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    server = smtplib.SMTP('mail.mshahabedin.ir: 26')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()


print()
print('Designed & Developed by %s' % ('\033[1m' + 'M.Mahdi Shahabedin'))
print("© All Rights Reserved")
print()

mainFunction()
