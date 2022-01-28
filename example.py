# pip install cloud-filemanager
import os
from cloud_filemanager import DropboxCloudManager, CloudConfig, ColorLogger

# Setup Logger
log = ColorLogger(logger_name='Example', color='yellow')

# Load config
# cloud_conf = {'type': 'dropbox', 'config': {'api_key': 'your api key'}}
# config_path = os.path.join('confs', 'conf.yml')
config_path = os.path.join('confs', 'conf_with_env_vars.yml')
config = CloudConfig(config_src=config_path)
cloud_conf = config.get_cloud_config()
# Check for errors
if cloud_conf['type'] != 'dropbox':
    raise Exception(f"{cloud_conf['type']} not yet supported!")
if cloud_conf['config']['api_key'] == 'DROPBOX_API_KEY':
    raise Exception("You are trying to use environmental variables but they are not loaded!")
# Initialize handler
dbx = DropboxCloudManager(config=cloud_conf['config'])
# Create a test file
with open('my_file.txt', 'w') as fp:
    fp.write('blank')

# -------- Examples -------- #
# Upload file
with open('my_file.txt', 'rb') as fp:
    file_to_upload = fp.read()
dbx.upload_file(file_bytes=file_to_upload, upload_path='/tests/my_file.txt', write_mode='overwrite')
# Show Cloud Files
log.info(f"List of files in the Cloud:\n{dbx.ls('/tests/')}")
# Download File
dbx.download_file(frompath='/tests/my_file.txt', tofile='my_file_downloaded.txt')
# Delete FIle
dbx.delete_file('/tests/my_file.txt')
# Show Cloud Files Again
log.info(f"List of files in the Cloud:\n{dbx.ls('/tests/')}")

# Cleanup
os.remove('my_file.txt')
os.remove('my_file_downloaded.txt')
