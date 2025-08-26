import clamd

def scan_file(filepath):
    cd = clamd.ClamdUnixSocket() # Connect to ClamAV daemon via Unix socket caz daemon already running

    try:
        result = cd.scan(filepath)
        if result[filepath][0] == 'OK':
            return {'status': 'clean'}
        else:
            return {'status': 'infected', 'details': result[filepath][1]}
    except Exception as e:
        return {'status': 'error', 'details': str(e)}