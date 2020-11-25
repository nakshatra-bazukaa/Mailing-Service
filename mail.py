import smtplib 
import csv

mecha="students.csv" #A csv file with two columns as id and email 

students = {}
with open(mecha, 'r') as data:
	for line in csv.reader(data):
		students[line[0]] = line[1]

all_sid = [] #Put all the id in this list to which you want to send email

sender_email = "sender_email_address" 
sender_pwd = "sender_email_address_password" 
message = "mail_message"

for sid in all_sid: 
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login(sender_email, sender_pwd) 
	s.sendmail(sender_email, students[sid], message) 
	s.quit() 