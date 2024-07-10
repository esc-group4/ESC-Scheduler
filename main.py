# entrypoint for docker and cron, everytime it runs, it ACCESS DB, check records, if fulfill conditions, run send_email() and send_message()

# TODO : Is there a need to queue emails/whatsapp messages? Is there an effective way to queue emails/whatsapp messages? will a message queue be helpful in this scenario or overkill?
# TODO : Will need to update database once emails/whatsapp messages are sent


def main():
    # connect to the db
    # query for emails/phone numbers that has start_date beyond threshold
    # filter for valid emails and phone numbers, in case data was changed to some invalid forms.
    # maybe do some storage for the invalid records.
    # input email list and phone list to the relevant functions
    return None
