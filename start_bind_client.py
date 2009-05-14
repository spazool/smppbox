#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os,getopt
import sb_bind_client.sb_bind_client as bind_client

# append SDK path
sys.path.append("./sb_smpp_sdk/")

__version = "0.1"

#default_args
options = {}
options["host"]=""
options["port"]=-1
options["system_id"]=""
options["password"]=""
options["system_type"]="cpa"
options["enquire_link_interval"]=60

options["server_port"]=-1
options["server_timeout"]=60

options["pidfile"]=""
options["logfile"]=""
options["loglevel"]=1
options["daemon"]=0


def usage():
    res = """SMPP BOX Component. sb_bind_client ver. %s
Использование: start_bind_client.py [КЛЮЧ]
Пример: start_bind_client.py -H smppserver.org -P 4000 -S 5000 --system-id="guest" --password="sicret"

Общие:
  -h, --help		    Показать помощь и выйти 

Насройка соединения:
  -H, --remote-host=HOST    Указать хост удаленного сервера для соединение
  -P, --remote-port=PORT    Указать порт на удаленном сервере для соединения
      --system-id=SYSTEMID  Указать идентификатор системы для аудентификации
      --password=PWD        Указать пароль для аудентификации  
      --system-type=ST      Установить параметр SYSTEM_TYPE (по умолчанию = cpa)
  -t, --enqlink-timeout=60  Установить время переспроса enquire_link (по умолчанию = 60 сек)

Настройка сервера:
  -S, --server-port=PORT    Указать порт для соединения служб
  -T, --server-timeout=60   Время ожидания комманд соединения служб
  
Дополнительные параметры запуска:
  -d, --daemon		    Запускать клиент в режиме демона
  -p, --pidfile=file.pid    Указать фаил для сохранения идентификатора процесса
  -l, --logfile=file.log    Указать фаил журнала (если не указан то в system_out)
  -v, --loglevel=level      Указать степень журналирования данных (0-отладка 1-Оповещения 2-Только ошибки) (
			    (по умолчанию 1)
""" % __version
    print res

# read args
try:                                
    opts, args = getopt.getopt(sys.argv[1:], "hH:P:t:S:T:dp:l:", ["help", "remote-host=","remote-port=","system-id=","password=","system-type=","enqlink-timeout=","server-port=","server-timeout=","daemon","pidfile=","logfile="]) 
except getopt.GetoptError:           
    usage()                          
    sys.exit(2)
    
for opt, arg in opts:
    if opt in ("-h","--help"):
	usage()
	sys.exit()
    elif opt in ("-H","--remote-host"):
	options["host"]=arg
    elif opt in ("-P","--remote-port"):
	try:
	    options["port"] = int(arg)
	except:
	    print "Ошибка указания порта!"
	    sys.exit(2)
    elif opt == "--system-id":
	options["system_id"] = arg
    elif opt == "--password":
	options["password"] = arg
    elif opt == "--system-type":
	options["system_type"] == arg
    elif opt in ("-t","--enqlink-timeout"):
	try:
	    options["enquire_link_interval"]=int(arg)
	except:
	    print "Ошибка указания времяни enquire_link"
	    sys.exit(2)
    elif opt in ("-S","--server-port"):
	try:
	    options["server_port"]=int(arg)
	except:
	    print "Ошибка указания порта служб"
	    sys.exit(2)
    elif opt in ("-T","--server-timeout"):
	try:
	    options["server_port"]=int(arg)
	except:
	    print "Ошибка указания времяни ожидания комманд служб"
	    sys.exit(2)
    elif opt in ("-d","--daemon"):
	options["daemon"]=1
    elif opt in ("-p","--pidfile"):
	try:
	    options["pidfile"]=arg
	    open(arg,"w").write(os.getpid());
	except:
	    print "Ошибка указания PID-файла"
	    sys.exit(2)
    elif opt in ("-l","--logfile"):
	options["logfile"]=arg
    elif opt in ("-v","--loglevel"):
	try:
	    options["loglevel"]=int(arg)
	except:
	    print "Ошибка указания loglevel"
	    sys.exit(2)

# проверяем необходимый минимум заполненных полей
if (options["host"]==""):
    print "Ошибка: Не указан хост удаленного сервера."
    sys.exit(2)

if (options["port"]==-1):
    print "Ошибка: Не указан порт удаленного сервера."
    sys.exit(2)

if (options["system_id"]==""):
    print "Ошибка: Не указан system_id."
    sys.exit(2)

if (options["server_port"]==-1):
    print "Ошибка: Не указан порт служб."
    sys.exit(2)


# Запустим сервер	
    bind_client.start(options)