import smtplib 
import csv

def mail(all_sid, message):
	mecha="students.csv" #A csv file with two columns as id and email 

	students = {}
	with open(mecha, 'r') as data:
		for line in csv.reader(data):
			students[line[0]] = line[1]

	sender_email = "sender_email_address" 
	sender_pwd = "sender_email_address_password" 

	for sid in all_sid: 
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		s.starttls() 
		s.login(sender_email, sender_pwd) 
		s.sendmail(sender_email, students[sid], message) 
		s.quit() 

def main():
	all_sid = [] #Put all the id in this list to which you want to send email
	message = "mail_message"
	mail(all_sid, message)

if __name__ == "__main__":
	main()