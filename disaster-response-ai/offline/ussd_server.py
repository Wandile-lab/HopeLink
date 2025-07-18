from africastalking.Service import USSDService

ussd = USSDService(username="user", api_key="key")

@ussd.route("/emergency")
def handle_emergency(session_id, phone_number, input):
    if input == "1":
        return "CON Report flood location (lat,lon):"
    elif "," in input:
        lat, lon = map(float, input.split(","))
        save_emergency(lat, lon)
        return "END Help is coming!"