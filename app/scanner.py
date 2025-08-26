import clamd
#VM-IP = 'http://192.168.1.9'
def scan_file(filepath):
    cd = clamd.ClamdUnixSocket() # Use this if clamd is set up with a Unix socket
    #cd = clamd.ClamdNetworkSocket(host='192.168.1.9', port=3310, timeout=60) # Use this for network socket

    try:
        result = cd.scan(filepath)
        if result[filepath][0] == 'OK':
            return {'status': 'clean'}
        else:
            return {'status': 'infected', 'details': result[filepath][1]}
    except Exception as e:
        return {'status': 'error', 'details': str(e)}