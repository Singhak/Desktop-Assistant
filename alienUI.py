import wx 
import win32com.client as wincl
import startpoint
import productSearch as ps
import news
import joke

speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak('''Whokum maire aakaa, Alien at your service.''')
# GUI creation
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None,
						  pos=wx.DefaultPosition, size=wx.Size(450, 100),
						  style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
						  wx.CLOSE_BOX | wx.CLIP_CHILDREN,
						  title="ALIEN")
		panel = wx.Panel(self)

		ico = wx.Icon('boy.ico', wx.BITMAP_TYPE_ICO)
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
		query_text = self.txt.GetValue().lower()
		split_query = query_text.split()
		
		if(query_text.startswith('flipk') or query_text.startswith('amazo')):
			#search query for product on amazon or flipkart
			[ps.productSearch(q_str, query_text.lower()) for q_str in product_vendor if split_query[0].lower() in q_str.lower()]
		elif(split_query[0] in news_type):
			#search query for news	
			[news.newsFeeds(q_str) for q_str in news_type if split_query[0].lower() in q_str.lower()]
		elif("joke" in query_text):
			#search query for joke	
			my_joke = joke.tellAJoke()
			print(my_joke)
			speak.Speak(my_joke)
		elif("youtube" in query_text):
			#search query for youtube	
			you_tube_query = "+".join(query_text.lower().replace('youtube',"").split())
			webbrowser.open('')
		
		
		
# Trigger GUI
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
