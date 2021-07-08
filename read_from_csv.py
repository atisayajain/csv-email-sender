import csv
import num2words
from datetime import datetime
from validate_email import validate_email
import write_to_img
import send_email

# csv filename with path, will generate a log at 'filename - log.csv'
filename = ''

with open(filename + '.csv', newline='') as csvrfile:
    reader = csv.reader(csvrfile)
    with open(filename + ' - log.csv', 'w', newline='') as csvwfile:
        writer = csv.writer(csvwfile)
        row = list(reader)

        for r in row:
            # map values with csv columns
            name = r[0]
            club = r[1]
            email = r[2].lower()

            try:
                # create image for individual by passing values
                write_to_img.set(name, club, email)
                p = write_to_img.create()
                writer.writerow([name, email, p, 1])

                if send_email.msg['To']:
                    del send_email.msg['To']

                if validate_email(email):
                    send_email.msg['To'] = email

                    send_email.create_mail(name)
                    c = send_email.s_mail()

                    send_email.msg.clear_content()
                    writer.writerow([name, email, c])

                    # reset variables
                    name = ''
                    email = ''
                    club = ''
                    #receipt_no += 1
                else:
                    print('Email is not valid.') 
                    continue

            except Exception as e:
                print(e)
                writer.writerow([name, email, e])