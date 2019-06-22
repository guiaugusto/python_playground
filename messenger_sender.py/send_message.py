from datetime import datetime
import requests

class SendMessage():
    def telegram_message(self, message):
        pass

    def telegram_parse_message(self, message, parse):
        pass

    def get_messenger(self, bot_id, sender_id, welcome_message):
        messengers_list = ['Telegram', 'Messenger']

        response = {}

        response = self.check_telegram_user(bot_id, sender_id, welcome_message)


    def get_actual_day(self):
        day = datetime.now()
        return day.strftime('%d')

    def check_telegram_user(self, bot_id, sender_id, welcome_message):
        response = requests.post(
            f'https://api.telegram.org/bot{bot_id}/sendMessage',
            data={
                'chat_id': sender_id,
                'text': welcome_message
            }
        )

        return response

    def check_facebook_user(self, bot_id, sender_id, welcome_message):
        pass
