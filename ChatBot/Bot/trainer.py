from chatbot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer=ChatterBotCorpusTrainer(chatbot)
trainer.train(
	"./knowledge/ai.yml",
	"./knowledge/botprofile.yml",
	"./knowledge/computers.yml",
	"./knowledge/conversations.yml",
	"./knowledge/emotion.yml",
	"./knowledge/food.yml",
	"./knowledge/gossip.yml",
	"./knowledge/greetings.yml",
	"./knowledge/health.yml",
	"./knowledge/history.yml",
	"./knowledge/humor.yml",
	"./knowledge/literature.yml",
	"./knowledge/money.yml",
	"./knowledge/movies.yml",
	"./knowledge/politics.yml",
	"./knowledge/psychology.yml",
	"./knowledge/science.yml",
	"./knowledge/sports.yml",
	"./knowledge/trivia.yml",
	"./knowledge/conversationstel.yml"
)

def brain(user_input):
	response = chatbot.get_response(user_input)
	return response

