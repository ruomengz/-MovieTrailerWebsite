import webbrowser

class ACG():
	"""docstring for ACG"""
	def __init__(self, title, poster):	
		self.title = title
		self.poster = poster

		
class Animation(ACG):
	"""Inherient from ACG"""
	def __init__(self, title, poster, youtube_trailer, storyline):
		ACG.__init__(self, title, poster)
		self.trailer_youtube_url = youtube_trailer
		self.storyline = storyline

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)


class Comics(ACG):
	"""Inherient from ACG"""
	def __init__(self, title, poster, author, storyline):
		ACG.__init__(self, title, poster)
		self.author = author
		self.storyline = storyline

class Game(ACG):
	"""Inherient from ACG"""
	def __init__(self, title, poster, youtube_trailer, company):
		ACG.__init__(self, title, poster)
		self.trailer_youtube_url = youtube_trailer
		self.company = company

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)