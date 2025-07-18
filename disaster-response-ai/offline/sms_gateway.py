from twilio.rest import Client
from typing import List

class SMSGateway:
    def __init__(self):
        self.client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))
    
    def send_alert(self, phone_numbers: List[str], message: str):
        for number in phone_numbers:
            self.client.messages.create(
                body=message,
                from_="+1234567890",
                to=number
            )
    
    def parse_ussd(self, ussd_code: str):
        # Example: *123*1# → "Report flood"
        _, _, emergency_type = ussd_code.split("*")
        return {
            "1": "flood",
            "2": "fire",
            "3": "earthquake"
        }.get(emergency_type, "unknown")