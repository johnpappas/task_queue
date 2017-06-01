
PROJECT_FILE_NAME='APP_NAME'
DELIMITER='_'

def get_app_name_prefix():
    with open(PROJECT_FILE_NAME, 'r') as myfile:
        app_name=myfile.read().replace('\n', '')
    return app_name + DELIMITER