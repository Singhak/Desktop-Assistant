import wx 
import win32com.client as wincl
import productSearch as ps
import news
import findJoke as joke
import youtube as ytb
import festival as fest
import wikipedia
import webbrowser
import speech as s
import weatherForcast as wf
import searchQuery as sq

speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak('Whokum maire aakaa, Alien at your service.')
# GUI creation
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None,
						  pos=wx.DefaultPosition, size=wx.Size(450, 100),
						  style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
						  wx.CLOSE_BOX | wx.CLIP_CHILDREN,
						  title="ALIEN")
		panel = wx.Panel(self)

		ico = wx.Icon('alien.ico', wx.BITMAP_TYPE_ICO)
		self.SetIcon(ico)

		my_sizer = wx.BoxSizer(wx.VERTICAL)
		lbl = wx.StaticText(panel, label="Sir. How can I help you?")
		my_sizer.Add(lbl, 0, wx.ALL, 5)
		self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(450, 30))
		self.txt.SetFocus()
		self.txt.Bind(wx.EVT_TEXT_ENTER, self.startSevices)
		my_sizer.Add(self.txt, 0, wx.ALL, 5)
		panel.SetSizer(my_sizer)
		self.Show()
	
	def startSevices(self, event):
		product_vendor = ['flipkart', 'amazon']
		news_type = ['sport', 'top', 'latest', 'world', 'gadget']
		query_text = self.txt.GetValue()
		if len(query_text) == 0:
			speak.Speak("Speak your order, please")
			query_text = s.getUserquery()
		if query_text != None and len(query_text) > 0:
			query_text = query_text.lower()
			split_query = query_text.split()
			print(query_text)
			if(query_text.startswith('flipk') or query_text.startswith('amazo')):
				#search query for product on amazon or flipkart
				[ps.productSearch(q_str, query_text) for q_str in product_vendor if split_query[0] in q_str]
			elif(split_query[0] in news_type):
				#search query for news	
				[news.newsFeeds(q_str) for q_str in news_type if split_query[0] in q_str]
			elif("joke" in query_text):
				#search query for joke	
				speak.Speak("Looking for a good joke for you")
				my_joke = joke.tellAJoke()
				print(my_joke)
				speak.Speak(my_joke)
			elif("youtube" in query_text):
				#search query for youtube	
				ytb.playYoutubeVideo(query_text)
			elif("when" in query_text) or ("festival" in query_text):
				#search query for festival	
				festival = fest.getfestivalTime(query_text)
				print(festival)
				speak.Speak(festival)
			elif("website" in query_text):
				#open any .com website
				if len(split_query) > 1:
					speak.Speak("opening "+ split_query[1])
					webbrowser.open('https://www.'+split_query[1]+'.com')
				else:
					speak.Speak("Tell name of website to open")
			elif('weather' in query_text):
				weather = wf.getWeatherReport(split_query[-1])
				if weather is not None:
					print(weather)
					speak.Speak(weather)
			else:
				speak.Speak('Searching for ' + query_text)
				whois = sq.search(query_text)
				print(whois)
				speak.Speak(whois)
				
					
		
# Trigger GUI
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
