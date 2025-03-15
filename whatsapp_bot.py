import pywhatkit as kit
import time
from datetime import datetime

# List of phone numbers (in international format)
phone_numbers = [
    
    '+2347064532361',
    '+2348131244269',
    '+2349067034298',
    '+2348133661602',
    '+2347064956853',
    '+2348066340150',
    '+2348034713472',
    '+2348104963503',
    '+2348132604160',
    '+2348050759338',
    '+2349036440065',
    '+2349122947174',
    '2347038210127',
    '+2348055762303',
    '+2348055762303',
    '+2348032854702',
    '+2348114302000',
    '+2347031878583',
    '+2347031151204',
    '+2347067108248',
    '+2348038304967',
    '+2348101109882',
    '2347062058939',
    '+2348112006500',
    '+2348112006500',
    '+2348169600536',
    '+2349160158208',
    '+2347087384070',
    '+2348072533742',
    '+2348072533742',
    '+2348105764442',
    '+2349132244171',
    '+2349037115940',
    '+2348075162401',
    '+2348032607421',
    '+2347061923392',
    '+2347044445375',
    '+2348039451050',
    '+2347067850835',
    '+2348023949916',
    '+2348112833348',
    '+2347032309725',
     '+2348105134263',
    '+2347053037068',
     '+2347063681449',
    '+2347038275747'
   
    

    
 
 
    

]

# Message to be sent
message_text = """Good day,
I hope you’re doing well! My name is Sadisu Mohammed, and I’m reaching out on behalf of At Adams Web & App Technologies Limited. I noticed your estate on Google Maps and saw that it currently doesn’t have a website. Our team specializes in web development, and we believe we can offer a solution that will greatly benefit your estate.
We understand that investing in a website might seem like a big step, but it’s an essential tool that can help your estate stand out and attract more clients. Here’s how a professional website can make a difference:
Why Your Estate Needs a Website:
- Increased Visibility – A website makes it easy for potential clients and investors to find your estate online.
- Build Credibility – A well-designed website presents your estate as a professional and trustworthy business.
- Showcase Properties – Display property listings with high-quality images and detailed descriptions, making it easier for visitors to explore your offerings.
- 24/7 Availability – Your website provides information to potential clients at any time, even outside business hours.
- Efficient Communication – Clients can easily reach out, inquire, or schedule visits directly from the website.
The Benefits of Investing in a Website:
- Cost-Effective Marketing – Unlike traditional advertising, a website works for you around the clock at a lower cost.
- Attract More Leads – A strong online presence will help you connect with more potential clients and close deals faster.
We truly believe that having a website is a smart investment for your estate’s growth and success. If you’re interested, we’d be happy to provide more details or answer any questions you might have.
Looking forward to the opportunity to assist you.
Best regards,
Sadisu Mohammed
At Adams Web & App Technologies Limited."""

# Send messages one by one
time_offset = 1  # Initial delay in minutes
for number in phone_numbers:
    try:
        print(f"Sending message to {number}...")


        # Get the current time
        now = datetime.now()

        # Calculate the sending time
        send_hour = now.hour
        send_minute = (now.minute + time_offset) % 60

        # Adjust the hour if minutes wrap around
        if now.minute + time_offset >= 60:
            send_hour = (send_hour + 1) % 24

        # Send message using WhatsApp Web
        kit.sendwhatmsg(number, message_text, send_hour, send_minute, wait_time=5)

        time_offset += 1  # Increment the delay by 1 minute for the next message

        time.sleep(5)  # Pause for 60 seconds to avoid spam detection

        print(f"Message sent to {number}!")

    except Exception as e:
        print(f"Failed to send to {number}: {str(e)}")

print("All messages have been sent!")
