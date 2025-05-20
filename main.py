import gspread
from oauth2client.service_account import ServiceAccountCredentials
import yagmail
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

YOUR_EMAIL = os.getenv("YOUR_EMAIL")
YOUR_PASSWORD = os.getenv("YOUR_PASSWORD")
GOOGLE_SHEET_URL = os.getenv("GOOGLE_SHEET_URL")
ATTACHMENT_PATH = os.getenv("ATTACHMENT_PATH")

# Check required env vars
if not all([YOUR_EMAIL, YOUR_PASSWORD, GOOGLE_SHEET_URL]):
    raise ValueError("One or more environment variables are missing!")

# 1. Authenticate Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# 2. Open Sheet and Get Data
sheet = client.open_by_url(GOOGLE_SHEET_URL).sheet1
data = sheet.get_all_records()

# 3. Email Setup
yag = yagmail.SMTP(YOUR_EMAIL, YOUR_PASSWORD)

# 4. Loop and Send Emails
for row in data:
    name = row.get("Name", "").strip()
    email = row.get("Email", "").strip()
    company = row.get("Company", "").strip()

    if not email:
        print(f"⚠️ Skipping row due to missing email: {row}")
        continue

    subject = f"Exciting Opportunity at {company or 'your company'}"
    body = f"""
    Hi {name or 'there'},

    I hope you're doing well! I wanted to reach out to you at {company or 'your organization'} with an exciting opportunity.

    Let me know if you'd like to chat more!

    Best regards,  
    Your Name
    """

    try:
        yag.send(
            to=email,
            subject=subject,
            contents=body,
            attachments=ATTACHMENT_PATH if ATTACHMENT_PATH and os.path.exists(ATTACHMENT_PATH) else None
        )
        print(f"✅ Email sent to {email}")
    except Exception as e:
        print(f"❌ Failed to send email to {email}: {e}")
