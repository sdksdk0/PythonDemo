import sys
import MySQLdb


class TransferMoney(object):
    def __init__(self,conn):
        self.conn=conn

    def transfer(self,source_acctid,target_acctid,money):

       try:
        self.check_acct_available(source_acctid)
        self.check_acct_available(target_acctid)
        self.has_enough_money(source_acctid,money)
        self.reduce_money(source_acctid,money)
        self.add_money(target_acctid,money)
        self.conn.commit()
       except Exception as e:
        self.conn.rollback()
        raise e



if __name__=='__main__':
    source_acctid=sys.argv[1]
    target_acctid=sys.argv[2]
    money=sys.argv[3]

    conn=MySQLdb.Connect(host='127.0.0.1',user='zp',passwd='a',db='mysqlforpython')
    tr_money=TransferMoney(conn)

    try:
        tr_money.transfer(source_acctid,target_acctid,money)
    except Exception as e:
        print "异常"+str(e)
    finally:
        conn.close()