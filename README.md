# 📧 Email Automation System

A Python application that automates sending personalized emails with optional attachments, sourcing recipient data from a Google Sheet. Designed for scalability and ease of use, this tool is ideal for outreach campaigns, newsletters, and more.

---

## 🚀 Features

* **Google Sheets Integration**: Fetches recipient data (Name, Email, Company) directly from a specified Google Sheet.
* **Personalized Emails**: Crafts individualized messages using recipient details.
* **Attachment Support**: Optionally includes attachments in emails.
* **Secure Authentication**: Utilizes environment variables and supports Gmail App Passwords for enhanced security.
* **User-Friendly Interface**: Built with `pywebview` for a native GUI experience.

---

## 📋 Prerequisites

* Python 3.6 or higher
* A Gmail account with [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) enabled
* A Google Cloud project with:

  * **Google Sheets API** enabled
  * **Google Drive API** enabled
* A service account with access to the target Google Sheet

---

## 🔧 Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/email-automation-system.git
   cd email-automation-system
   ```

2. **Set Up a Virtual Environment** (Optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:

   * Rename `.env.example` to `.env`.
   * Populate `.env` with your credentials:

     ```env
     YOUR_EMAIL=your_email@gmail.com
     YOUR_PASSWORD=your_app_password
     GOOGLE_SHEET_URL=https://docs.google.com/spreadsheets/d/your_sheet_id/edit?usp=sharing
     ATTACHMENT_PATH=path/to/your/attachment.pdf  # Optional
     ```

5. **Set Up Google Service Account**:

   * Create a service account in your Google Cloud project.
   * Download the `credentials.json` file and place it in the project root.
   * Share your Google Sheet with the service account's email address.

---

## 🚀 Usage

Run the application:

```bash
python main.py
```

The script will:

1. Authenticate with Google Sheets and Gmail.
2. Retrieve recipient data from the specified Google Sheet.
3. Send personalized emails to each recipient, including attachments if specified.

---

## 📝 Customization

* **Email Template**: Modify the `body` variable in `main.py` to change the email content.
* **Subject Line**: Adjust the `subject` variable to suit your campaign.
* **Attachment**: Update the `ATTACHMENT_PATH` in your `.env` file to include different files.

---

## 📁 Project Structure

```
email-automation-system/
├── main.py
├── credentials.json
├── .env
├── requirements.txt
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

* [gspread](https://github.com/burnash/gspread) for Google Sheets API integration
* [yagmail](https://github.com/kootenpv/yagmail) for simplified Gmail SMTP handling
* [pywebview](https://github.com/r0x0r/pywebview) for the GUI interface
