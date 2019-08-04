# NBA-Stats-SMS-Bot
Uses Twilio, NBA_Py, and Flask to give users NBA player's stats.

Requirements:
Python libraries:
Flask
requests
twilio.twiml.messaging_response import MessagingResponse
nba_py
pandas

Extras:
Twilio trial account
Ngrok

How it works:

I create a Python webserver with Flask. Then I use Ngrok to give the web server a link. I then use this link to connect my
Twilio number with my program. I do this through the Twilio Console and the Webhook function.

