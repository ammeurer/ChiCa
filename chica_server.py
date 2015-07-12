from flask import Flask, request, redirect
import twilio.twiml


app = Flask(__name__)
numbers = ["+13618160814"]


@app.route("/", methods=['GET', 'POST'])
# def hello_world():
#     return 'Hello World!'

def hello_monkey():
	"""Respond to incoming requests."""

	resp = twilio.twiml.Response()
	from_number = request.values.get('From', None)
	# if from_number in numbers:
	return redirect("/registered-user")
	# else:
	# 	numbers.append(from_number)
	# 	with resp.gather(numDigits=12, action="/sign-up", method="POST") as g:
 # 			g.say("Welcome to ChiCa. ChiCa help you build a network of mothers who can exchange child care among eachother. To signup to the ChiCa community type in the number of your friend after the beep.")
 # 	return str(resp)

@app.route("/sign-up", methods=['GET', 'POST'])
def handle_key():
    """Handle key press from a user."""
 
    # Get the digit pressed by the user
    friend_number = request.values.get('Digits', None)
    numbers.append(friend_number)
    
    resp = twilio.twiml.Response()
        # Dial (310) 555-1212 - connect that number to the incoming caller.
        # If the dial fails:
    resp.say("Thank you for signing up! You are now part of the ChiCa community. We will now forward you to the main menu or your can hang up now.", voice="woman")
    return redirect("/registered-user")

@app.route("/registered-user", methods=['GET', 'POST'])
def request_care():
	resp = twilio.twiml.Response()
	with resp.gather(numDigits=1, action="/decision", method="POST") as g:
 		g.say("To request child care, press zero. To add a friend's number, press one.", voice="woman")
 	return str(resp)

@app.route("/decision", methods=['GET', 'POST'])
def decision():
	choice = request.values.get('Digits', None)
	if choice == "0":
		return redirect("/choose-day")
	elif choice == "1":
		return redirect("/add-friend")
	else:
		return redirect("/registered-user")

@app.route("/choose-day", methods=['GET', 'POST'])
def choose_day():
	resp = twilio.twiml.Response()

	with resp.gather(numDigits=1, action="/record-message", method="POST") as g:
 		g.say("If you need child care tomorrow, press zero. If you need child care the day after tomorrow, press one.", voice="woman")
 	return str(resp)

@app.route("/record-message", methods=['GET', 'POST'])
def record_message():
	choice = request.values.get('Digits', None)
	resp = twilio.twiml.Response()
	if choice == "0":
		resp.say("Tomorrow.")
		return str(resp)
	elif choice == "1":
		resp.say("Day after tomorrow.")
		return str(resp)
	else:
		resp.say("I am sorry, I did not understand.")
		return redirect("/choose-day")

@app.route("/add-friend", methods=['GET', 'POST'])
def add_friend():
	pass
if __name__ == "__main__":
    app.run(debug=True)