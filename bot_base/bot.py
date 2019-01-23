from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import web

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Database connection
db = web.database(
    dbn = 'mysql',
    host = 'localhost',
    db = 'demo_bot00',
    user = 'utec',
    pw = 'utec.2019',
    port = 3306
    )

#Samm17_bot 
token = ''

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    username = update.message.from_user.username
    update.message.reply_text('Hola {} usa estos comandos:\n/info llave #busca_informacion'.format(username))

def help(bot, update):
    username = update.message.from_user.username
    update.message.reply_text('Hola {} usa estos comandos:\n/info llave #busca_informacion'.format(username))

def search(update):
    text = update.message.text.split()
    username = update.message.from_user.username
    try:
        id_producto = int(text[1]) # cast para convertir str a int
        print "Send info to {}".format(username)
        print "Key search {}".format(id_producto)
        result = db.select('productos', where='id_producto=$id_producto', vars=locals())[0]
        print result
        respuesta =  str(result.producto) + ", " + str(result.existencias) + ", " + str(result.precio)
        #response = "Sending Info " + str(result[0]) + ", " + str(result[1]) + ", " + str(result[2])
        #print response
        update.message.reply_text('Hola {}\nEsta es la informacion que buscas:\n{}'.format(username, respuesta))
    except Exception as e:
        print "Error: " + str(e.message)
        update.message.reply_text('La llave {} es incorreta'.format(id_producto))

def info(bot, update):
    search(update)

def echo(bot, update):
    update.message.reply_text(update.message.text)
    print update.message.text
    print update.message.date
    print update.message.from_user
    print update.message.from_user.username
    
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

    
def main():
    try:
        print 'S.A.M.M. init token'
        
        updater = Updater(token)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        print 'S.A.M.M. init dispatcher'

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("info", info))        

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))

        # log all errors
        dp.add_error_handler(error)

        # Start the Bot
        updater.start_polling()

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        print 'S.A.M.M. ready'
        updater.idle()
    except Exception as e:
        print "Error 100: ", e.message

if __name__ == '__main__':
    main()
