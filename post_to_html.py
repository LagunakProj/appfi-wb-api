# import requests
from fpdf import FPDF
# from email.message import EmailMessage
# import smtplib
from json2html import *
import json



# url_json = 'https://reqres.in/api/users'
# url_post = 'http://127.0.0.1:5000/translator'


# info_json = requests.get(url_json).text
# post_info = requests.post(url_post, json= info_json)



def create_pdf(info):
    # infoFromJson = json.loads(info)
    print(json2html.convert(json = info))   
    # output = r"C:\Users\PC\workspace\our-wep-api\Outpu32.pdf"
    # pdf = FPDF()
    # pdf.set_auto_page_break(auto=True, margin= 100)
    # pdf.add_page()
    # pdf.set_font('helvetica', 'BIU', 16)
    # pdf.cell(0, 10, info, ln=True)
    # pdf.output(output)
    # send_mail(output)


def send_mail(pdf):
    sender = 'mailtestharri@gmail.com'
    password = 'A1234567A'

    msg = EmailMessage()

    ### set the subject ###
    msg['Subject'] = "Test Mail"

    msg['From'] = sender
    ### set the receiver mail account ###
    msg['To'] = 'jokanac666@civikli.com'
    ### set the mail body ###
    msg.set_content('Hi this is a test mail with the pdf')

    with open(pdf, 'rb') as f:
        file_data = f.read()
        file_name = f.name

        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)