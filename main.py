"""
1. Пользователь запускает игру.
2. Пользователь видит вопрос
    'whats is the english "<слово по русски>"'
    '1. <Вариант ответа>'
    '2. <Вариант ответа>'
    '3. <Вариант ответа>'
    '4. <Вариант ответа>'
3. Пользователь вводит с клавиатуры 1-4
4. Если мы угадали, то отображаем правильный ответ 'Correct'
4а. Если мы не угадали, то отображаем правильный ответ <Правильный ответ>
5. Повторяем пока пользователь не вышел из игры    
"""

import random
from dict import diction
from cgitb import text
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import Filters
from telegram import ReplyKeyboardMarkup

SECRET = "5487139694:AAFPfZQ8-s54iEuQR-9r6VYFgFLTgRfdmkU"


def generate_question():
        answers = random.sample(list(diction.keys()), 4)
        question = random.choice(answers)

        correct_answer = diction[question]
        translated_answers = [diction[answer] for answer in answers]
        return translated_answers, question, correct_answer

def start(update, context):
    answers, question, correct_answer = generate_question()
    keybord = ReplyKeyboardMarkup.from_column(answers, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id = update.effective_chat.id, text = f'Whats is the english "{question}"', reply_markup=keybord)

    context.user_data['correct'] = correct_answer

def answer_question(update, context):
    chat_id = update.effective_chat.id
    text = update.effective_message.text

    correct_answer = context.user_data['correct']

    if correct_answer == text:
        context.bot.send_message(chat_id = chat_id, text = 'Correct')
    else:
        context.bot.send_message(chat_id = chat_id, text = f"Wrong answer \nCorrect answer '{correct_answer}'")
        
    start(update, context)


bot = Updater(token = SECRET)
bot.dispatcher.add_handler(CommandHandler('start', start))
bot.dispatcher.add_handler(MessageHandler(Filters.text, answer_question))
bot.start_polling()


"""
/start- Привет,name

"""