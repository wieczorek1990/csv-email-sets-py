import csv

def get_emails(filename):
  with open(filename) as fp:
    reader = csv.DictReader(fp)
    emails = map(lambda row: row['email'], reader)
  return set(emails)

a_emails = get_emails('a.csv')
b_emails = get_emails('b.csv')

print a_emails, b_emails
print a_emails - b_emails, b_emails - a_emails, a_emails | b_emails, a_emails & b_emails, a_emails ^ b_emails
