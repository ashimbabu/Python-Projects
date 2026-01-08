import smtplib
from email.message import EmailMessage

print("===== Email Sender Application =====")

def send_email():
    sender_email = input("Enter your email: ")
    sender_password = input("Enter your app password: ")
    receiver_email = input("Enter receiver email: ")
    subject = input("Enter subject: ")
    message = input("Enter message: ")

    email = EmailMessage()
    email["From"] = sender_email
    email["To"] = receiver_email
    email["Subject"] = subject
    email.set_content(message)

    try:
        server = smtplib.SMTP("test@gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(email)
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print("Failed to send email!")
        print("Error:", e)

while True:
    print("\nMenu:")
    print("1. Send Email")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        send_email()
    elif choice == "2":
        print("Email Application closed.")
        break
    else:
        print("Invalid choice. Try again.")
