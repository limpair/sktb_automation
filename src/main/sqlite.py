# -*- coding: UTF-8 -*-
import sqlite3, time

class DataBaseControl(object):
    def __init__(self):
        print 'init'
        self.open()

    def open(self):
        self.conn = sqlite3.connect('E:\sktb_automation\src\main\oms.db')
    
    def close(self):
        if(self.conn != None):
            self.conn.close()
    
    def save(self, obj):
        if(self.conn == None):
            self.open()
        self.conn.execute('insert into osm (name,time,activity,account) values("' + obj['name'] + '", "' + obj['time'] + '", "' + obj['activity'] + '","' + obj['account'] + '")')
        self.conn.commit()
    
    def update(self, obj):
        if(self.conn == None):
            self.open()
        self.conn.execute('update osm set time = "' + obj['time'] + '" where id = ' + str(obj['id']))
        self.conn.commit()
    
    def delete(self, obj):
        if(self.conn == None):
            self.open()
        self.conn.execute('delete from osm where id = ' + str(obj['id']))
        self.conn.commit()
    
    def saveList(self, objs):
        if(self.conn == None):
            self.open()
        
        for obj in objs:
            self.conn.execute('insert into osm (name,time,activity,account) values("' + obj['name'] + '", "' + obj['time'] + '", "' + obj['activity'] + '","' + obj['account'] + '")')
        
        self.conn.commit()
    
    def updateList(self, objs):
        if(self.conn == None):
            self.open()
        for obj in objs:
            self.conn.execute('update osm set time = "' + obj['time'] + '" where id = ' + str(obj['id']))
        self.conn.commit()
    
    def deleteList(self, objs):
        if(self.conn == None):
            self.open()
        for obj in objs:
            self.conn.execute('delete from osm where id = ' + str(obj['id']))
        self.conn.commit()
    
    def getByName(self, name, account):
        if(self.conn == None):
            self.open()
        cursor = self.conn.execute('select * from osm where name = "' + name + '" and account = "' + account + '"')
        res = []
        for row in cursor:
            result = {}
            result['id'] = row[0]
            result['name'] = row[1]
            result['time'] = row[2]
            result['activity'] = row[3]
            result['account'] = row[4]
            result['mktime'] = time.mktime(time.strptime(row[2], '%Y-%m-%d %H:%M:%S'))
            res.append(result)
        # self.conn.commit()
        return res
    def list(self, account):
        if(self.conn == None):
            self.open()
        cursor = self.conn.execute('select * from osm where account = "' + account + '"')
        result = []
        for row in cursor:
            res = {}
            res['id'] = row[0]
            res['name'] = row[1]
            res['time'] = row[2]
            res['activity'] = row[3]
            res['account'] = row[4]
            res['mktime'] = time.mktime(time.strptime(row[2], '%Y-%m-%d %H:%M:%S'))
            result.append(res)
        # self.conn.commit()
        return result

if __name__ == '__main__':
    con=DataBaseControl()
    con.open()
    #obj['name'] + '", "' + obj['time'] + '", "' + obj['activity'] + '","' + obj['account']
    #con.save({'name':u'我a是人','time':'2017-07-05 11:54:52','activity':'Y10','account':'11111'})
    #print {'name': '我a是人','time':'2017-07-05 11:54:52','activity':'Y10','account':'11111'}
    print len(con.getByName(u'我是aaa人','11111'))
    con.close()
