from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('essfarbot',read_only=False,
                logic_adapters=[
                {
                    'import_path':'chatterbot.logic.BestMatch',
                    #'default_response':'Sorry I don\'t know what that means',
                    #'maximum_similarity_threshold':0.90                    
                }
                ])

list_to_train =[
    "hi",
    "hello, nice to meet you",
    "what's your name?",
    "Essfar Bot",
    "what can you do?",
    "All you want me to do",
    "Do you have kids?",
    "No I do not have any"
] # This list must have an even number of element

botCorpusTrainer = ChatterBotCorpusTrainer(bot)
#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)

botCorpusTrainer.train("chatterbot.corpus.english")

def index(request):
    return render(request,'blog/index.html')

def specific(request):
    list1 = [1,3,5,3]
    return HttpResponse(list1)

def getResponse(request):
    msg = request.GET.get('msg')
    botResponse = str(bot.get_response(msg))
    return HttpResponse(botResponse)

"""def article(request,article_id):
    return render(request,'blog\index.html',{'article_id':article_id})
"""