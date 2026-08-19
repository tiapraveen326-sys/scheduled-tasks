from datetime import datetime
import pandas
import random
import smtplib
import os

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

birthdays_DataFrame = pandas.read_csv('birthdays.csv')

birthdays_dict = birthdays_DataFrame.to_dict(orient='records')
today = datetime.today()

current_year = today.year
current_month = today.month
current_day = today.day

# 3. If today matches a birthday, pick a random letter

for birthday in birthdays_dict:
    if current_year == birthday["year"] and current_month == birthday["month"] and current_day == birthday["day"]:

        letter_name = "letter_" + str(random.randint(1, 3)) + ".txt"

        with open("./letter_templates/" + letter_name, "r") as file:
            content = file.read()
            new_content = content.replace("[NAME]", birthday["name"])

        # Get email and password from GitHub Secrets
        my_email = os.environ.get("MY_EMAIL")
        password = os.environ.get("MY_PASSWORD")

        # 4. Send the letter generated in step 3

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)

            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday["email"],
                msg=f"Subject: Happy Birthday!\n\n{new_content}"
            )
