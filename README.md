# 2021_TOC_Project
Line Bothttps://github.com/grgy078033/2021_TOC_Project

## 功能
根據使用者的心情與喜好，推薦適合的音樂。  

## State層
state1 : start(開始)，剛加入官方帳號時，輸入開始，進入大廳。  
state2 : lobby(大廳)，列出各功能，目前只有音樂推薦這一個功能。  
state3 : 功能(音樂推薦)，進入到各功能中，此處是音樂推薦，會詢問使用者性別。  
state4 : 性別，根據性別推薦音樂，此時列出音樂的曲速，看使用者今天想聽快的歌還是慢的歌。  
state5 : 音樂曲速，此時列出對應音樂速度的音樂類型，如快歌對應到快樂。  
state6 : 音樂類型，選了音樂類型後即推薦本週推薦音樂。  

## FSM
![image](https://github.com/grgy078033/2021_TOC_Project/blob/master/fsm.png)

## 中途經歷之困難與解決辦法
Q1.在Verify Webhook時一直跑出timeout  
A1.要先把程式跑起來，並打開ngrok開始收聽port8000，即可success  

Q2.不擅長使用go_back()來回到上一個state  
A2.使用advanced()來實作回到上一個state的功能  

Q3.可使用graphviz自動產出fsm的code，但無法產出png檔  
A3.將產出來的fsm code，透過以下方式產出圖:  
	1.將以下的code "C:\Users\grgy0\Graphviz\bin\dot" -T png test.gv 1>fsm.png 2>error.txt 寫進一個記事本中，並將檔名改成bat檔  
	2.透過此bat執行檔產出fsm.png  
	3.將fsm.png手動丟入此Project的資料夾中，讓程式能夠去讀取圖片上的FSM，並實作其功能  