import pywhatkit    
phone_number = "+919725265524"  # Replace with the actual phone number and country code
message_content = "Msg sent through coding bot"  # Message to be sent
waiting_time = 10  # Seconds to wait before sending

pywhatkit.sendwhatmsg_instantly(phone_number, message_content, waiting_time)