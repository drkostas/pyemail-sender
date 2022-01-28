# pip install pyemail-sender
import os
from pyemail_sender import GmailPyEmailSender, PyEmailSenderConfig, ColorLogger

# Setup Logger
log = ColorLogger(logger_name='Example', color='yellow')

# Load config
# email_conf = {'type': 'gmail',
#               'config': {'api_key': 'your api key', 'email_address': 'youremail@gmail.com'}}
# config_path = os.path.join('confs', 'conf.yml')
config_path = os.path.join('confs', 'conf_with_env_vars.yml')
config = PyEmailSenderConfig(config_src=config_path)
email_conf = config.get_pyemail_sender_config()
# Check for errors
if email_conf['type'] != 'gmail':
    raise Exception(f"{email_conf['type']} not yet supported!")
if email_conf['config']['api_key'] == 'GMAIL_API_KEY':
    raise Exception("You are trying to use environmental variables but they are not loaded!")
# Initialize handler
pymail = GmailPyEmailSender(config=email_conf['config'])
# Create a test file
with open('my_file.txt', 'w') as fp:
    fp.write('blank')

# -------- Examples -------- #
email_conf = email_conf['config']
# Send Simple Email
pymail.send_email(subject='A simple email',
                  to=[email_conf['email_address']],
                  text='Email body text goes here')
# Send HTML Email
pymail.send_email(subject='A simple HTML email',
                  to=[email_conf['email_address']],
                  html='<h1>Email body with HTML goes here</h1>')
# Send Email with all the arguments
pymail.send_email(subject='Email with all possible arguments',
                  sender=email_conf['email_address'],
                  to=[email_conf['email_address']],
                  cc=[email_conf['email_address']],
                  bcc=[email_conf['email_address']],
                  reply_to=email_conf['email_address'],
                  html='<h1>Test <b>HTML</b> body</h1>',
                  attachments=['my_file.txt'])

# Cleanup
os.remove('my_file.txt')
