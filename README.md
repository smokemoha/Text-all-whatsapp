# WhatsApp Auto Messaging Bot  

## **Overview**  
This project is a **Python-based WhatsApp bot** that automates the process of sending messages to multiple recipients using **WhatsApp Web**. The bot is useful for **marketing, customer outreach, and business communications**, enabling bulk messaging without manual effort.  
---
## **How It Works**  
✅ Uses **PyWhatKit** to send automated messages via **WhatsApp Web**.  
✅ Supports **bulk messaging** with a predefined list of phone numbers.  
✅ Custom **message scheduling** to prevent spam detection.  
✅ Ensures **efficient message delivery** by adding a delay between messages.  
--
## **Installation & Setup**  
### **1️⃣ Prerequisites**  
Ensure you have the following installed:  
- **Python 3.8+** → [Download Python](https://www.python.org/downloads/)  
- **Google Chrome** (Required for WhatsApp Web)  
- **WhatsApp Web Linked to Your Phone** , ,
### **2️⃣ Install Required Dependencies**  
Run the following command to install the required libraries:  
pip install pywhatkit,
3️⃣ Clone the Repository
git clone https://github.com/smokemoha/whatsapp-bot.git
cd whatsapp-bot,
4️⃣ Configure the Bot
Open the script (whatsapp_bot.py) and modify the phone_numbers list with the numbers you want to message.
Update the message_text with the content you wish to send.
How to Run the Script,
Run the following command to start sending messages:
python whatsapp_bot.py,
Once executed:
The script will open WhatsApp Web in your browser.
It will automatically send messages to each recipient in the list.
Each message will be sent with a 1-minute delay to avoid spam detection.
