import asyncio
import telegram
import requests
import whisper


def download_file(URL):
	response = requests.get(URL)
	with open('voice.ogx', 'wb') as f:
		f.write(response.content)

model = whisper.load_model("large")

def trans(file_path):
	result = model.transcribe(file_path)
	return result["text"]
	

async def main():
	bot = telegram.Bot(os.environ.get('BOT_KEY'))
	async with bot:
	
		update = await bot.get_updates()
		new_update = last_update = update[-1]['update_id']
	
		while True:
			update = await bot.get_updates()
			new_update = update[-1]['update_id']

			if new_update != last_update:
				voice = update[-1]['message']['voice']
				#text = update[-1]['message']['text']
				chat_id = update[-1]['message']['chat']['id']
	
				if voice != None:
					voice_file = await bot.getFile(voice['file_id'])
					download_file(voice_file['file_path'])
					transcription = trans('voice.ogx')
					await bot.send_message(text=transcription, chat_id=chat_id)
					
				last_update = new_update


if __name__ == '__main__':
	asyncio.run(main())
