import smtplib

content = "Merhaba Zumrud-u Anka"

##  we connect gmail server.. #if we want to send email on gmail server, we must have gmail account..
mail = smtplib.SMTP("smtp.gmail.com",587) ## port number is 587 which gmail server used.

##  introduce ourself to gmail server
mail.ehlo()

##  This function encrypt our e-mail and password
mail.starttls()

##  We are connect to gmail server
mail.login("email_adres","sifre")

##  This function setting what we want to send e-mail from whom to who
mail.sendmail("whom@gmail.com","who@gmail.com",content)

