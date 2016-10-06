import media
import fresh_tomatoes

kiminona = media.Animation("Your Name",
							"http://m.niusnews.com/upload/imgs/default/16AprW/0407yourname/1.jpg",
							"https://www.youtube.com/watch?v=k4xGqY5IDBE",
							"The movie starts off with the main male character, Taki Tachibana and the main female character, Mitsuha Miyamizu waking up to normal lives, however they can't help but feel the sensation of losing something important to them.")
FFXV = media.Game("Final Fantasy XV",
				  	"http://img1.gtimg.com/comic/pics/hv1/74/147/2045/133013684.jpg",
					"https://www.youtube.com/watch?v=zNL_yRUMx9g",
					"SQUARE ENIX")
onepiece = media.Animation("One Piece Film Gold",
							"https://i.ytimg.com/vi/NmyGak3l12Y/maxresdefault.jpg",
							"https://www.youtube.com/watch?v=7zaKkTRs8Q8",
							"The Straw Hat Pirates are taking on Gild Tesoro, one of the richest men in the world.")
fresh_tomatoes.open_movies_page([kiminona,onepiece,FFXV])
