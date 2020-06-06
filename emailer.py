# Title: Sending Emails in Python With SMTP
# Author: Esther Vaati
# Date: January 1st, 2018
# Availability: https://code.tutsplus.com/tutorials/sending-emails-in-python-with-smtp--cms-29975


import smtplib
import email.message
server = smtplib.SMTP('smtp.gmail.com:587')

def send_email(sender, reciever, potential_tweet, sender_password):
	email_content = "Potential Tweet: " + potential_tweet +  """
	<html>
	<head>

	   <title>Your Twitter Post is ready</title>
	   <style type="text/css">
		a {color: #d80a3e;}
	  body, #header h1, #header h2, p {margin: 0; padding: 0;}
	  #main {border: 1px solid #cfcece;}
	  img {display: block;}
	  #top-message p, #bottom p {color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }
	  #header h1 {color: #ffffff !important; font-family: "Lucida Grande", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; }
	  #header p {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 12px;  }
	  h5 {margin: 0 0 0.8em 0;}
		h5 {font-size: 18px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }
	  p {font-size: 12px; color: #444444 !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; line-height: 1.5;}
	   </style>
	</head>
	<body>
	<table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"><tr><td>

	<table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
		<tr>
		  <td>
		    <table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="8fb3e9">
		      <tr>
		        <td width="570" align="center"  bgcolor="#d80a3e"><h1>It has been 3 Days! If you still want to post your tweet, login to our site to do so.</h1></td>
		      </tr>
		    </table>
		  </td>
		</tr>
	  </table>
	  <table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center">
		<tr>
		  <td align="center">
		    <p>Design better experiences for web & mobile</p>
		    <p><a href="#">Unsubscribe</a> | <a href="#">Tweet</a> | <a href="#">View in Browser</a></p>
		  </td>
		</tr>
	  </table><!-- top message -->
	</td></tr></table><!-- wrapper -->

	</body>
	</html>

	"""

	msg = email.message.Message()
	msg['Subject'] = 'Do you still want to Post your Tweet?'


	msg['From'] = sender
	msg['To'] = reciever
	password = sender_password
	msg.add_header('Content-Type', 'text/html')
	msg.set_payload(email_content)

	s = smtplib.SMTP('smtp.gmail.com: 587')
	s.starttls()

	# Login Credentials for sending the mail
	s.login(msg['From'], password)

	s.sendmail(msg['From'], [msg['To']], msg.as_string())
	return
