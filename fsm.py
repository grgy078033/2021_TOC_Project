from transitions.extensions import GraphMachine

from utils import send_text_message

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    #------------------------------start-----------------------------------#
    def is_going_to_lobby(self, event):
        text = event.message.text
        return text.lower() == "開始"

    def on_enter_lobby(self, event):
        print("I'm entering lobby")

        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇您想要的服務：\n「音樂推薦」\n(途中皆可輸入「返回」以回到上一步)")
    #------------------------------state1-----------------------------------#
    def is_going_to_sharing(self, event):
        text = event.message.text
        return text.lower() == "音樂推薦"

    def on_enter_sharing(self, event):
        print("I'm entering sharing")

        reply_token = event.reply_token
        send_text_message(reply_token, "歡迎來到音樂推薦專區，請告訴我您的性別，以為您提供適合您的音樂(也可自由選擇~)：\n「男性」\n「女性」")
    #------------------------------state2-----------------------------------#
    def is_going_to_boy(self, event):
        text = event.message.text
        return text.lower() == "男生"

    def is_going_to_girl(self, event):
        text = event.message.text
        return text.lower() == "女生"

    def on_enter_boy(self, event):
        print("I'm entering boy")

        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇音樂速度:\n「輕快」\n「舒緩」")

    def on_enter_girl(self, event):
        print("I'm entering girl")

        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇音樂速度:\n「輕快」\n「舒緩」")
    #------------------------------state3-----------------------------------#
    def boy_to_fast(self, event):
        text = event.message.text
        return text.lower() == "輕快"
    def on_enter_boy_fast(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇音樂類型:\n「紓壓」\n「快樂」")
        
    def boy_to_slow(self, event):
        text = event.message.text
        return text.lower() == "舒緩"
    def on_enter_boy_slow(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇音樂類型:\n「放鬆」\n「安慰」")

    def girl_to_fast(self, event):
        text = event.message.text
        return text.lower() == "輕快"
    def on_enter_girl_fast(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇音樂類型:\n「紓壓」\n「快樂」")
        
    def girl_to_slow(self, event):
        text = event.message.text
        return text.lower() == "舒緩"
    def on_enter_girl_slow(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇音樂類型:\n「放鬆」\n「安慰」")
    #------------------------------state4-----------------------------------#
    def boy_fast_to_crazy(self, event):
        text = event.message.text
        return text.lower() == "紓壓"
    def on_enter_boy_fast_crazy(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "本週推薦 ： 血肉果汁機 - 深海洋\nhttps://reurl.cc/OpbNER \n輸入「返回」以重新選擇歌曲\n輸入「性別」以獲得更多類型歌曲\n輸入「大廳」以返回大廳")

    def boy_fast_to_happy(self, event):
        text = event.message.text
        return text.lower() == "快樂"
    def on_enter_boy_fast_happy(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "本週推薦 ： 恐龍的皮 - Jurassic ride\nhttps://reurl.cc/qODRk3 \n輸入「返回」以重新選擇歌曲\n輸入「性別」以獲得更多類型歌曲\n輸入「大廳」以返回大廳")
    
    def boy_slow_to_ease(self, event):
        text = event.message.text
        return text.lower() == "放鬆"
    def on_enter_boy_slow_ease(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "本週推薦 ： The.Fur - Julie\nhttps://reurl.cc/zMyaY0 \n輸入「返回」以重新選擇歌曲\n輸入「性別」以獲得更多類型歌曲\n輸入「大廳」以返回大廳")
    
    def boy_slow_to_comfort(self, event):
        text = event.message.text
        return text.lower() == "安慰"
    def on_enter_boy_slow_comfort(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "本週推薦 ： VOOID - 礦石\nhttps://reurl.cc/e652Db \n輸入「返回」以重新選擇歌曲\n輸入「性別」以獲得更多類型歌曲\n輸入「大廳」以返回大廳")
    
    def girl_fast_to_crazy(self, event):
        text = event.message.text
        return text.lower() == "紓壓"
    def on_enter_girl_fast_crazy(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "本週推薦 ： 海豚刑警 - 安平之光\nhttps://reurl.cc/bk6rly \n輸入「返回」以重新選擇歌曲\n輸入「性別」以獲得更多類型歌曲\n輸入「大廳」以返回大廳")

    def girl_fast_to_happy(self, event):
        text = event.message.text
        return text.lower() == "快樂"
    def on_enter_girl_fast_happy(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "本週推薦 ： 魏如萱 - Have a nice day\nhttps://reurl.cc/dXr3LD \n輸入「返回」以重新選擇歌曲\n輸入「性別」以獲得更多類型歌曲\n輸入「大廳」以返回大廳")
    
    def girl_slow_to_ease(self, event):
        text = event.message.text
        return text.lower() == "放鬆"
    def on_enter_girl_slow_ease(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "本週推薦 ： 洪申豪 - 金巴利\nhttps://reurl.cc/QjpqZq \n輸入「返回」以重新選擇歌曲\n輸入「性別」以獲得更多類型歌曲\n輸入「大廳」以返回大廳")
    
    def girl_slow_to_comfort(self, event):
        text = event.message.text
        return text.lower() == "安慰"
    def on_enter_girl_slow_comfort(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "本週推薦 ： 守夜人 - 我睡不著\nhttps://reurl.cc/Kp6W49 \n輸入「返回」以重新選擇歌曲\n輸入「性別」以獲得更多類型歌曲\n輸入「大廳」以返回大廳")
    #------------------------------back_conditions-----------------------------------#
    def is_backing_to_gender(self, event):
        text = event.message.text
        return text.lower() == "返回"
    def on_backing_gender(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "歡迎來到音樂推薦專區，請告訴我您的性別，以為您提供適合您的音樂(也可自由選擇~)：\n「男性」\n「女性」")
        
    def is_backing_to_speed(self, event):
        text = event.message.text
        return text.lower() == "返回"
    def on_backing_speed(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇音樂速度:\n「輕快」\n「舒緩」")
        
    def is_backing_to_fast_type(self, event):
        text = event.message.text
        return text.lower() == "返回"
    def on_backing_fast_type(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇音樂類型:\n「紓壓」\n「快樂」")
        
    def is_backing_to_slow_type(self, event):
        text = event.message.text
        return text.lower() == "返回"
    def on_backing_slow_type(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇音樂類型:\n「放鬆」\n「安慰」")

    def is_backing_to_choose_gender(self, event):
        text = event.message.text
        return text.lower() == "性別"
    def on_backing_choose_gender(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "歡迎來到音樂推薦專區，請告訴我您的性別，以為您提供適合您的音樂(也可自由選擇~)：\n「男性」\n「女性」")

    def is_backing_to_back_lobby(self, event):
        text = event.message.text
        return text.lower() == "大廳"
    def on_backing_back_lobby(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇您想要的服務：\n「音樂推薦」\n(途中皆可輸入「返回」以回到上一步)")

    def is_share_backing_to_lobby(self, event):
        text = event.message.text
        return text.lower() == "返回"
    def on_share_backing_lobby(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇您想要的服務：\n「音樂推薦」\n(途中皆可輸入「返回」以回到上一步)")
    