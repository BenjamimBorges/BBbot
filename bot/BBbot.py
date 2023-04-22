import nltk
from nltk.chat.util import Chat, reflections

pares = [
	[
		r"oi|ola|hello!|hey",
		["ola","oi","hey!","hello"]
	],
	
	[
		r"qual seu nome?|qual é o seu nome?",
		["Meu nome é BBbot","Eu sou o BBbot!"]
	],
	
	[
		r"como você está?|como vai?|tudo bem?",
		["eu estou bem","muito bem","Graças a Deus bem"]
	],

	[
		r"adeus|tchau|bye|sayonara",
		["tchau","até mais!","até a proxima"]
	],
]

def BBbot():
	print("Ola sou o BBbot, como posso ajuda-lo hoje?")
	chat = Chat(pares, reflections)
	while True:
		try:
			resposta = chat.respond(input())
			print(resposta)
		except KeyboardInterrupt:
			break
BBbot()



