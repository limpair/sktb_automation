import datetime
def log(line, message, info, filename=''):
    debug = open('debug_log.txt', 'a')
    if message=='':
        debug.write(filename + ',line:' + line + ',error:' + info + ',time:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    else:
        debug.write(filename + ',line:' + line + ',error:' + message + ',time:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    debug.close()
