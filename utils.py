# -*- coding: UTF-8 -*-
from datetime import datetime
import ast
import sqlite3, os, shelve
import datetime as d
import dbm
githubs = "https://github.com/JuniorMario/JarvisBot"
bitbucket = "https://bitbucket.org/JuniorMario/jarvisbot/src"
list_adm = [172480531, 178373108 ]
date = d.datetime.now()
date = str(date)
date = date.split('-')
ano = date[0]
mes = date[1]
dia = date[2]
dia = dia.split(' ')
dia = dia[0]
text_messages = {

    'comandos':
        u'Comandos Informativos:\n'
    	u'      /commands\n'
    	u'      /bot_users\n'
    	u'      /sobre\n'
    	u'      /code(DISABLE)\n'

    	u'🔎Comandos de Pesquisa🔎\n'
    	u'      /youtube\n'
    	u'      /pdf\n'
    	u'      /torrent\n'
    	u'      /linux\n'
    	u'      /app\n'
    	u'      /magnet\n'
    	u'      /9gag\n'
    	u'      /cot\n'
    	u'      /clima\n'
    	u'      /xkcd\n'
    	u'Comandos Term🖥:\n'
    	u'      /hash\n'
    	u'Group Utils:\n'
    	u'       /info\n'
    	u'       /regras\n'
    
        u'Comandos a Administração:\n'
        u'      /solicitar\n'
        u'      /sugestao\n'
        u'      /admin_commands',


    'comm':
        u'/def_regras\n'
        u'/regras\n'
}
sessao = []
opcoes = []
opc = []
def get_users(user):
    dbmess = shelve.open('userinfo.db')
    if ' ' in str(user):user.replace(' ','')
    if user in str(dbmess.keys()):
        id_r = dbmess[user]['id']
        print id_r
        return id_r
    else:
        return False
def sql():
  idss = []
  conn = sqlite3.connect('user.db')
  curs = conn.cursor()
  curs.execute('select username from users')
  usernames = str(curs.fetchall())
  curs.execute('select user_id from users')
  ids = curs.fetchall()
  dic = {'ids':ids, 'usernames':usernames}
  print dic
  return dic
def garg(message, comando):
    gar = str(message.text.encode('utf-8'))
    gar = gar.replace(comando, '')
    return gar

def log_erros(func, erro, mensagem):
    __CREDITOS__ = "Diego Bernades(@EXPL01T3R0) https://github.com/diego-bernardes/"
    arquivo_logs = open('Logs_de_erros.txt', 'w+')
    arquivo_logs.write('''
#Erro! Função {fun} {data}
Mensagem de erro:
{log_erro}
Mensagem que originou o erro:
{mensagem}
------------------------------------'''
                  .format(fun = func, data = str(datetime.today()), log_erro = erro,
                          mensagem = str(mensagem).encode('UTF-8', errors='ignore').decode('ASCII', errors='ignore')))

    arquivo_logs.close()


def log(dados_msg):
    global msg
    msg = dados_msg
    try:
        dados_msg = ast.literal_eval(str(dados_msg).encode('UTF-8', errors='ignore').decode('ASCII', errors='ignore'))
        if dados_msg['chat']['type'] == 'private': origem = 'Mensagem Privada'
        elif dados_msg['chat']['type'] == 'group': origem = 'Grupo'
        elif dados_msg['chat']['type'] == 'supergroup': origem = 'Super Grupo'
        else: origem = dados_msg['chat']['type']
        print('''
LOG: comando recebido
Comando: {comando}
Origem: {origem}
Titulo do chat: {nomechat}
ID do chat: {chatid}
Nome do remetente: {nome_usuario}
Username: {username}'''
              .format(comando = dados_msg['text'], origem = origem, nomechat = dados_msg['chat']['title'], chatid = dados_msg['chat']['id'],
                        nome_usuario = dados_msg['from_user']['first_name'] + dados_msg['from_user']['last_name'] if dados_msg['from_user']['last_name'] else dados_msg['from_user']['first_name'],
                          username = dados_msg['from_user']['username']))


    except Exception as erro:
        log_erros('LOG', erro, dados_msg)
        print('\n------------------------------------\nErro na função log, consulte o arquivo logs_de_erros,', datetime.today())

def insert_info(message):
  conn = sqlite3.connect('user.db')
  curs = conn.cursor()
  curs.execute("INSERT INTO users VALUES ('{}', {})".format(message.from_user.username, message.from_user.id))
  curs.execute('select * from users')
  print(curs.fetchall())
  conn.commit()
  conn.close()

def is_admin(msg):
    info = log(msg)
    user_id = msg.from_user.id
    if user_id in list_adm:
        return True
    else:
        return False
def stringando(arg):
    if type(arg) == list:
        compiled = "{}\n{}\n{}\n{}".format(arg[0], arg[1], arg[2], arg[3])
        return compiled
    else:
        pass
def formatlen(arg):
    if len(arg) > 4:
        count = 0
        finala = []
        for i in arg:
            if count <= 4:
                finala.append(arg[count])
            else:
                pass
        result = stringando(finala)
        return result
    elif len(arg) < 4:
        return arg
    else:
        pass

def start_m(title, adm, group_id):
    try:
    	conn = sqlite3.connect('group.db')
    	curs = conn.cursor()
    	title  = str(title.encode('utf-8')).replace(' ','')
    	if ' ' in adm:adm = adm.replace(' ','')
    	curs.execute('CREATE TABLE {} (adm char(500), group_id int(456))'.format(title))
    	curs.execute("INSERT INTO {} VALUES ('{}', {})".format(title, adm, group_id))
    	curs.execute('SELECT * FROM {}'.format(title))
    	x = curs.fetchall()
    	print(x)
        answer = "Usuário @{} adicionado como admin do grupo {}!".format(adm, title)
        conn.commit()
        conn.close()
    except:
        answer = "Deu ruim ai, reporte ao @Junior_Py."
    return answer
def query_verify(chat_id, name):
    conn = sqlite3.connect('group.db')
    curs = conn.cursor()
    curs.execute('select group_id from {}'.format(name))
    it = curs.fetchall()
    if str(chat_id) in str(it):
        return True
    else:
        return False
def out_dir():
    os.chdir('..')
    os.chdir('..')
    print(os.system('pwd'))
def join_dir(arg):
    os.chdir('distros/{}'.format(arg))
    print(os.system('pwd'))
def managers(title):
    conn = sqlite3.connect('group.db')
    curs = conn.cursor()
    if ' ' in title:title = title.replace(' ','')
    curs.execute('SELECT adm FROM {}'.format(title))
    adms = curs.fetchall()
    adms = str(adms).strip('] [ ').replace('u\'','@').strip('(').replace('\"','').strip(',').replace('\'','').replace(')','\n').replace(', (','').strip(',')
    curs.execute('SELECT group_id FROM {}'.format(title))
    ids = curs.fetchall()
    dic = {"adms":adms, "ids":ids}
    return dic
def is_group_admin(title, arg):
    if ' ' in arg: arg = arg.replace(' ','')
    answ = managers(title)
    if arg in str(answ['adms']):
        return True
    else:
        return False

def rules(message, rules):
  db = dbm.open('rules', 'c')
  arg = str(message.chat.id)
  if arg in str(db.keys()):
    db[arg] = rules
    answr = "*Regras atualizadas com sucesso.*"
    db.close()
  else:
    db[arg] = rules
    answr = "*Regras definidas*\n _{}_".format(rules)
    db.close()
  return answr
def rules_q(message):
  db = dbm.open('rules', 'r')
  print dbm.library
  res = []
  for key in db.keys():
    if str(message.chat.id) in key:
          print message.chat.id
          res.append(db[key])
    else:
      pass
  return res

def promote(title, adm, group_id):
    try:
        conn = sqlite3.connect('group.db')
        curs = conn.cursor()
        if ' ' in adm:adm = adm.replace(' ','')
        curs.execute("INSERT INTO {} VALUES ('{}', {})".format(title, adm, group_id))
        curs.execute('SELECT adm FROM {}'.format(title))
        adms = curs.fetchall()
        conn.commit()
        conn.close()
        print adms
        answr = "*Usuario {} promovido com sucesso!*".format(adm)
    except:
        answr = "*Ocorreu algum erro, retorne ao @Junior_Py*"
    return answr
def remove(title, adm, group_id):
    try:
        if ' ' in adm:adm = adm.replace(' ','')
        conn = sqlite3.connect('group.db')
        curs = conn.cursor()
        curs.execute("DELETE FROM {} WHERE adm = '{}'".format(title, adm))
        curs.execute('SELECT adm FROM {}'.format(title))
        adms = curs.fetchall()
        conn.commit()
        conn.close()
        print adms
        answr = "*Usuario {} removido com sucesso!*".format(adm)
    except:
        answr = "*Um erro ocorreu, reporte ao @Junior_Py*"
    return answr
def infosg(message):
    conn = sqlite3.connect('group.db')
    curs = conn.cursor()
    curs.execute('CREATE TABLE info (users char(500), user_id int (456), group_id int(456))')
    curs.execute("INSERT INTO info VALUES ('{}',{}, {})".format(message.from_user.username,int(message.from_user.id), int(message.chat.id)))
    curs.execute('SELECT * FROM info')
    x = curs.fetchall()
    print x
    conn.commit()
    conn.close()
def put_info(message):
    dbmess = shelve.open('userinfo.db')
    user_obj = {'username':message.from_user.username,'id': int(message.from_user.id), 'chat_id': int(message.chat.id)}
    if str(message.from_user.username) not in str(dbmess.keys()):
      keyr = str(message.from_user.username)
      dbmess[keyr] = user_obj
      print '{} n estava ainda'.format(str(message.from_user.username))
    else:
      pass
def broad():
    dbmess = shelve.open('userinfo.db')
    return dbmess
def get_ids(arg):
    ids = []
    for i in arg:
  	    ids.append(i.user.id)
    return ids
