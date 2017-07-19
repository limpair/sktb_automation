# -*- coding: UTF-8 -*-
import sqlite3, time, datetime, debug
import os
class DataBaseControl(object):
    def __init__(self):
        debug.message('连接数据库', os.path.basename(__file__))
        self.open()

    def open(self):
        self.conn = sqlite3.connect('oms.db')
    
    def close(self):
        if(self.conn != None):
            self.conn.close()
            debug.message('关闭数据库', os.path.basename(__file__))
    
    def save(self, obj):
        if(self.conn == None):
            self.open()
        self.conn.execute('insert into osm (skname,name,time,activity,account) values("' + obj['skname'] + '","' + obj['name'] + '", "' + obj['passtime'] + '", "' + obj['activity'] + '","' + obj['account'] + '")')
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
            self.conn.execute('insert into osm (skname,name,time,activity,account) values("' + obj['skname'] + '","' + obj['name'] + '", "' + obj['passtime'] + '", "' + obj['activity'] + '","' + obj['account'] + '")')
        
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
            result['skname'] = row[1]
            result['name'] = row[2]
            result['time'] = row[3]
            result['activity'] = row[4]
            result['account'] = row[5]
            result['mktime'] = time.mktime(time.strptime(row[3], '%Y-%m-%d %H:%M:%S'))
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
            res['skname'] = row[1]
            res['name'] = row[2]
            res['time'] = row[3]
            res['activity'] = row[4]
            res['account'] = row[5]
            res['mktime'] = time.mktime(time.strptime(row[3], '%Y-%m-%d %H:%M:%S'))
            result.append(res)
        # self.conn.commit()
        return result
    def saveRemark(self, obj, TYPE):
        if(self.conn == None):
            self.open()
        if TYPE == 0:
            self.conn.execute('INSERT INTO tb_remarks(taskId,title,link,order_num,time,account,tbuser) VALUES("' + obj['taskId'] + '","' + obj['title'] + '","' + obj['link'].encode('utf-8') + '","' + obj['order_num'].encode('utf-8') + '","' + obj['time'] + '","' + obj['account'].encode('utf-8') + '","' + obj['tbuser'].encode('utf-8') + '")')
        elif TYPE == 1:
            self.conn.execute('INSERT INTO remarks(taskId,title,link,order_num,time,account,tbuser) VALUES("' + obj['taskId'] + '","' + obj['title'] + '","' + obj['link'].encode('utf-8') + '","' + obj['order_num'].encode('utf-8') + '","' + obj['time'] + '","' + obj['account'].encode('utf-8') + '","' + obj['tbuser'].encode('utf-8') + '")')
        self.conn.commit()
    
    def getRemarks(self, account):
        orders = []
        cursor = self.conn.execute('SELECT * FROM tb_remarks WHERE account="' + account.encode('utf-8') + '" AND time like "%' + datetime.datetime.now().strftime('%Y-%m-%d') + '%"')
        for row in cursor:
            orders.append({'link':row[3], 'order':row[4], 'title':row[2]})
        return orders
    
    def getOrder(self, account, order):
        if(self.conn == None):
            self.open()
        cursor = self.conn.execute('select * from orders where account = "' + account + '" and order_num = "' + order + '"')
        res = []
        for row in cursor:
            result = {}
            result['id'] = row[0]
            result['title'] = row[1]
            result['link'] = row[2]
            result['order'] = row[3]
            result['time'] = row[4]
            result['account'] = row[5]
            res.append(result)
        return res
    def listOrder(self, account):
        if(self.conn == None):
            self.open()
        cursor = self.conn.execute('select * from orders where account = "' + account + '" AND time like "%' + datetime.datetime.now().strftime('%Y-%m-%d') + '%"')
        res = []
        for row in cursor:
            result = {}
            result['id'] = row[0]
            result['title'] = row[1]
            result['link'] = row[2]
            result['order'] = row[3]
            result['time'] = row[4]
            result['account'] = row[5]
            res.append(result)
        return res
    def saveOrder(self, obj, TYPE):
        if(self.conn == None):
            self.open()
        if TYPE == 0:
            self.conn.execute('INSERT INTO orders (title,link,order_num,time,account) VALUES("' + obj['title'] + '","' + obj['link'] + '","' + obj['order_num'] + '","' + obj['time'] + '","' + obj['account'] + '")')
        elif TYPE == 1:
            self.conn.execute('UPDATE orders SET time="' + obj['time'] + '" WHERE id=' + str(obj['id']))
        self.conn.commit()
if __name__ == '__main__':
    DataBaseControl()