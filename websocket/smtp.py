import smtplib

# Gmail user credentials
gmail_user = 'bountyhunter2804@gmail.com'
gmail_password = 'Yvish*28'

# SMTP server details
smtp_server = "smtp.gmail.com"
smtp_port = 587


def send_email(recipient, subject, text):
    try:
        # Establish a connection to the SMTP server
        smtpserver = smtplib.SMTP(smtp_server, smtp_port)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(gmail_user, gmail_password)

        # Create the email header and content
        header = f"To: {recipient}\nFrom: {gmail_user}\nSubject: {subject}\n"
        message = header + "\n" + text

        # Send the email
        smtpserver.sendmail(gmail_user, recipient, message)
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the SMTP server connection
        smtpserver.close()


# Example usage
send_email("vishwaayuvaraj@gmail.com", "Subject", "This is the email text.")
