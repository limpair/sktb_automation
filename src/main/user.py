import sqlite
import sktb
import time

def getByName(obj):
    cont = sqlite.DataBaseControl()
    cursor = cont.conn.execute('select * from account where tbusername="' + obj['tu'].encode('utf-8') + '" and skusername="' + obj['su'].encode('utf-8') + '"')
    res = []
    for row in cursor:
        result = {}
        result['id'] = row[0]
        result['tbusername'] = row[1]
        result['tbpassword'] = row[2]
        result['skusername'] = row[3]
        result['skpassword'] = row[4]
        res.append(result)
        # self.conn.commit()
    cont.close()
    return res

def getAccount(obj):
    cont = sqlite.DataBaseControl()
    cursor = cont.conn.execute('select * from account where tbusername="' + obj['tu'].encode('utf-8') + '" or skusername="' + obj['su'].encode('utf-8') + '"')
    res = []
    for row in cursor:
        result = {}
        result['id'] = row[0]
        result['tbusername'] = row[1]
        result['tbpassword'] = row[2]
        result['skusername'] = row[3]
        result['skpassword'] = row[4]
        res.append(result)
        # self.conn.commit()
    cont.close()
    return res

def saveAccount(obj):
    cont = sqlite.DataBaseControl()
    res = getByName(obj)
    if len(res) == 1:
        cont.conn.execute('UPDATE account SET tbpassword="' + obj['tp'] + '",skpassword="' + obj['sp'] + '" WHERE tbusername="' + obj['tu'].encode('utf-8') + '" and skusername="' + obj['su'].encode('utf-8') + '"')
    else:
        cont.conn.execute('INSERT INTO account(tbusername,tbpassword,skusername,skpassword) VALUES("' + obj['tu'].encode('utf-8') + '","' + obj['tp'] + '","' + obj['su'].encode('utf-8') + '","' + obj['sp'] + '")')
    cont.conn.commit()
    cont.close()
    
def autoLogin(driver, obj):
    result = False
    result = sktb.loginShikee(driver, obj['skusername'], obj['skpassword'])
    time.sleep(2)
    result = sktb.loginTaobao(driver, obj['tbusername'], obj['tbpassword'])
    return result
