# -*- coding: UTF-8 -*-
#!/usr/bin/python
import telebot, ast, types
from datetime import datetime
from telebot import types
import random, time, sqlite3, requests, datetime, crawler, hashlib, sys, os, glob, subprocess
from utils import *
bot = telebot.TeleBot('<TOKEN>')
bot.skip_pending = True
uptimef = datetime.today()
requests.packages.urllib3.disable_warnings()
@bot.message_handler(commands=['start', 'begin'])
def answer(message):
  infor = sql()
  if str(message.from_user.id) in str(infor['ids']):
    bot.send_message(message.chat.id, 'Você ja está inscrito no Jarvis, use /info para mais.')
  else:
    insert_info(message)
    bot.send_message(message.chat.id, '*Bem vindo ao Jarvis! Para informações use /info e para ver os comandos user /commands*', parse_mode="markdown")
@bot.message_handler(commands=['sugestao'])
def sugest(message):
	try:
		messageStriped = garg(message, "/suegestao")
		messageStriped = "*O usuario {} sugeriu {}*".format(message.from_user.username, messageStriped)
		log(message)
		if (str(message.chat.type) != 'private'):
			bot.reply_to(message, '*Esse comando está programado para funcionar somente em modo privado...*', parse_mode="markdown")
			block(message)
		else:
			bot.send_message('178373108', messageStriped, parse_mode="markdown")
	except:
		pass
@bot.message_handler(commands=['admin_commands'])
def sendo_ad_command(message):
  bot.send_message(message.chat.id, text_messages['comm'])
@bot.message_handler(commands=['info'])
def send_group_admins(message):
	if message.chat.type != 'private':
		adms = bot.get_chat_administrators(message.chat.id)
		admins = ""
		for i in adms:
			admins += '\n :' + i.user.first_name.encode('UTF-8', errors = 'ignore').decode('ASCII', errors = 'ignore') + " - " + "@" +  i.user.username
		bot.send_message(message.chat.id, " <b>|| Administradores ||</b> \n      🔰🔰🔰\n{}\n{}\n{}\n<b>Quantidade de usuarios {}</b>.".format("-"*40, str(admins).replace(':','🔰'), "-" * 40, bot.get_chat_members_count(message.chat.id)), parse_mode="html")
	else:
		bot.reply_to(message, 'Esse comando só funciona em grupos!')
@bot.message_handler(commands=['solicitar'])
def sol(message):
	try:
		bot.send_message('178373108', '*O usuario {} solicitou administração para o seu grupo.*'.format(message.from_user.username), parse_mode="markdown")
		bot.reply_to(message, '*Solicitação encaminhada ao* @Barionix', parse_mode="markdown")
		bot.send_message(message.from_user.id, '*Sua solicitação foi entregue ao ADM, ele responderá assim que possivel.*', parse_mode="markdown")
	except:
		send_error(message)
@bot.message_handler(commands=['sobre','about'])
def hi(message):
	infosql = sql()
	bot.send_message(message.chat.id, 'Hi, {}!\nSou Jarvis bot desenvolvido por @Junior_Py.\n👤Qt. de Usuarios: {}.👤\nPara ver os comandos use /help ou /commands'.format(message.from_user.username, len(infosql['ids'])))
@bot.message_handler(commands=['broadcast'])
def broadcasting(message):
	if is_admin(message):
		arg = garg(message, '/broadcast')
		broa = broad()
		listof = []
		for i in broa.keys():
			try:
				bot.send_message(broa[i]['id'], arg)
			except:
				print '{} não tem autorização'.format(broa[i]['username'])
				pass
	else:
		bot.reply_to(message, 'Somente admins podem usar este comando.')
@bot.message_handler(commands=['9gag'])
def send_gag(message):
	try:
		res = crawler.randGag()
		bot.send_message(message.chat.id, '<a href="{}">9gag</a>'.format(res), parse_mode="html")
	except:
		bot.reply_to(message, 'Erro ao enviar Gag')
@bot.message_handler(commands=['xkcd'])
def send_gag(message):
	try:
		res = crawler.randXK()
		print res
		bot.send_message(message.chat.id, '<a href="{}">XKCD</a>'.format(str(res)), parse_mode="html")
	except:
		bot.reply_to(message, 'Erro ao enviar tirinha.')
@bot.message_handler(commands=['clima'])
def send_clima(message):
	try:
		arg = garg(message, '/clima')
		res = crawler.send_weather(arg)
		tempera_max = res['main']['temp_max'] - 273.15
		tempera_min = res['main']['temp_min'] - 273.15
		bot.send_message(message.chat.id, "🏢Local:{}\n📡Coordenadas:Lat.{} - Long.{}.\n☁️Condição: {}\n🔺Maxima:{}\n🔻Minima:{}\n💧Umidade:{}".format(res['name'].encode('UTF-8', errors = 'ignore').decode('ASCII', errors = 'ignore'), res['coord']['lat'], res['coord']['lon'], res['weather'][0]['description'].encode('UTF-8', errors = 'ignore').decode('ASCII', errors = 'ignore'), tempera_max, tempera_min, res['main']['humidity']))
	except:
		bot.reply_to(message, 'Ocorreu um erro.')
@bot.message_handler(commands=['users_list', 'bot_users'])
def listu(message):
	try:
		infosql = sql()
		log(message)
		usuarios = []
		usuarios = str(infosql['usernames'])
		usuarios = usuarios.strip('] [ ').replace('u\'','@').strip('(').replace('\"','').strip(',').replace('\'','').replace(',)','\n').replace(', (','')
		bot.send_message(message.chat.id, 'Lista de Usuarios:\n{}'.format(usuarios))
	except:
		send_error(message)
@bot.message_handler(commands=['help', 'commands'])
def showCommands(message):
	bot.reply_to(message, text_messages['comandos'])

@bot.message_handler(commands=['torrent'])
def crw(message):
	try:
		arg = garg(message, '/torrent')
		res = crawler.torta(arg)
		titles = res['titles']
		appsf = res['linked']
		num = len(titles) - 1
		lin = len(appsf) - 1
		msg = bot.send_message(message.chat.id, "📱[{}]({})\n📱[{}]({})\n📱[{}]({})\n📱[{}]({})\n📱[{}]({})".format(titles[0], appsf[0], titles[1], appsf[1],titles[2], appsf[2],titles[3], appsf[3],titles[4], appsf[4]), parse_mode="markdown")
	except:
		bot.reply_to(message, 'Invalid Sintax. Use /torrent <pesquisa>')
@bot.message_handler(commands=['magnet', 'directtorrent'])
def torrentando(message):
	arg = message.text.encode('utf-8').replace('/magnet','')
	
	try:
		torr = crawler.torrents(arg)
		bot.reply_to(message, "Pesquisando por {}...".format(arg))
		magnets = torr['magnets']
		titles = torr['titles']
		res = "{}:\n\n{}\n\n{}:\n\n{}\n\n{}:\n\n{}".format(str(titles[0]), str(magnets[0]), str(titles[1]), str(magnets[1]), str(titles[2]), str(magnets[2]))
		with open('mag{}.txt'.format(message.from_user.username),'w+') as f:
			f.write(res)
		file = open('mag{}.txt'.format(message.from_user.username),"rb")
		bot.send_document(message.chat.id, file)
		file.close()
		os.sysem('rm mag{}.txt'.format(message.from_user.username))
	except:
		bot.reply_to(message, 'Pesquisa invalida.')
@bot.message_handler(commands=['cot'])
def send_cot(message):
	try:
		arg = garg(message, '/cot')
		arg = arg.split(' ')
		res = crawler.cota(arg[1]+arg[2])
		bot.send_message(message.chat.id, "*1 {} = {}*".format(arg[1], res.replace('[','').strip(']').strip('\'')), parse_mode="markdown")
	except:
		bot.reply_to(message, "Sintaxe invalida, use /cot MOEDA MOEDA\n_EX: /cot USD BRL_", parse_mode="markdown")
@bot.message_handler(commands=['hash'])
def md5(message):
	try:
		arg = str(message.text)
		arg = arg.strip('/md5')
		print(arg)
		h = hashlib.md5()
		h.update(arg)
		bot.reply_to(message, 'hash Gerada com sucesso:\n{}'.format(h.hexdigest()))
	except:
		bot.reply_to(message, 'Sintaxe invalida\nUse /hash string a ser transformada.')
@bot.message_handler(commands=['proxy'])
def proxys(message):
	bot.reply_to(message, 'Buscando Proxys recentes...')
	try:
		res = crawler.proxando()
		bot.send_message(message.chat.id, str(res))
	except:
		bot.reply_to(message, 'Deu ruim, reporta ao @Junior_Py pra ele corrigir...')
@bot.message_handler(commands=['app'])
def appzando(message):
	try:
	    arg = message.text[3:]
	    res = crawler.playSt(arg)
	    msg = bot.send_message(message.chat.id, res, parse_mode="markdown")
	except:
		bot.reply_to(message, "Sintaxe invalida, use /app <Nome do aplicativo>")
@bot.message_handler(commands=['youtube'])
def youtube(message):
	try:
		arg = str(message.text)
		result = crawler.pesquisa(arg)
		bot.reply_to(message, result, parse_mode="markdown")
	except IndexError:
		bot.reply_to(message, 'Sintaxe invalida!\nUse /youtube string a ser pesquisada.')

@bot.message_handler(commands=['linux'])
def linuxando(message):
	cid = message.chat.id
	mes = str(message.text)
	if message.chat.type == 'private':
	    markup = types.ReplyKeyboardMarkup(row_width=1)
	    distros = ['Debian', 'Arch', 'Open Suse', 'Ubuntu', 'Kali Linux', 'Linux Mint', 'Fedora']
	    for dist in distros:
			 markup.add( types.KeyboardButton(dist))
	    msg = bot.reply_to(message, 'Qual distro deseja?', reply_markup=markup)
	    bot.register_next_step_handler(msg, processit)
	else:
	 	bot.reply_to(message, '*Este comando está configurado para funcionar somente no privado.*', parse_mode="markdown")
def processit(message):
   	genderius = str(message.text)
   	join_dir(genderius.lower())
   	opc = glob.glob('*.torrent')
   	markup = types.ReplyKeyboardMarkup(row_width=1,one_time_keyboard=True)
   	for i in opc:
   		markup.add(types.KeyboardButton(i))
   	pick = bot.reply_to(message, 'Qual .torrent deseja?', reply_markup=markup)
   	bot.register_next_step_handler(pick, send_distro)
def send_distro(message):
   	fileTorrent = open(str(message.text), 'rb')
   	bot.send_document(message.chat.id, fileTorrent)
 	time.sleep(0.5)
	out_dir()
@bot.message_handler(commands=['def_regras'])
def def_rule(message):
  arg = garg(message, '/def_regras')
  adms = bot.get_chat_administrators(message.chat.id)
  ids = get_ids(adms)
  print ids
  if str(message.from_user.id) in str(ids):
	it = rules(message, arg)
	bot.reply_to(message, it, parse_mode="markdown")
  else:
    bot.reply_to(message, 'Você né admin desse grupo não moço.')
@bot.message_handler(commands=['regras'])
def def_rulesando(message):
  try:
    watch = rules_q(message)
    bot.reply_to(message, watch)
  except:
    bot.reply_to(message, 'Não há regras definidas nesse grupo.')
@bot.message_handler(commands=['pdf','apostila'])
def send_it(message):
	mess = str(message.text).strip('/pdf')
	try:
		bot.reply_to(message, 'Baixando...')
		pdf = crawler.apostilando(mess)
		bot.send_document(message.chat.id, pdf)
		mes = None
	except:
		bot.reply_to(message, 'Sua pesquisa é invalida ou não foi encotrado resultado.')

def send_it_shit(message):
	mes = str(message.text.encode('utf-8'))
	print mes
	if '😅' in mes: #copy and paste the emoji here...and if the user send that emoji you send the sticker that belongs him
		bot.reply_to(message, '😝')
		bot.send_sticker(message.chat.id, "BQADBAADAgAD8mXUBrMm-xSwdfnlAg")
	else:
		pass



@bot.message_handler(commands=['id'])
def id_(mensagem):
    log(mensagem)
    usernas = bot.get_chat_member(mensagem.chat.id, mensagem.from_user.id)

    try:
        bot.reply_to(mensagem,'''
INFO
ID: {id_user}
Seu Nome: {nome}
Username: @{username}
---------------------
Nome do Chat: {nome_grupo}
ID do Grupo:     {id_grupo}'''.format(nome = mensagem.from_user.first_name + mensagem.from_user.last_name if mensagem.from_user.last_name else mensagem.from_user.first_name,
                                    username = mensagem.from_user.username, id_user = mensagem.from_user.id, nome_grupo = mensagem.chat.title,
                                    id_grupo = mensagem.chat.id))
    except Exception as erro:
            log_erros('comando ID', erro, mensagem)
            print('\n------------------------------------\nErro na função ID, consulte o arquivo logs_de_erros,', datetime.today())

@bot.message_handler(func=lambda message: True)
def make_it_work(message):
	try:
		put_info(message)
	except:
		bot.send_message(178373108, 'Ei, Teve um erro aqui na função do count')

bot.polling()
'''
@bot.message_handler(commands=['kick'])
def kick_user(message):
	    arg = garg(message, '/kick')
	    argm = get_users(arg)
	    ids = get_ids(bot.get_chat_administrators(message.chat.id))
	    if str(message.from_user.id) in str(ids):bot.kick_chat_member(message.chat.id, int(argm))
	    
@bot.message_handler(commands=['search', 'pesquisa'])
def sear(message):
		arg = log(message)
		searc = str(message.text)
		searc = searc.strip('/search')
		res = crawler.bing(searc)
		print(res)
		bot.reply_to(message, res)

'''