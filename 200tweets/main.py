#imports
import wsgiref.handlers
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
import sys
sys.path.insert(0, 'tweepy.zip')
import tweepy

#Handler classes
class MainPage(webapp.RequestHandler):
	def get(self):
		# Accessing url
		user = self.request.get("user")
		
		if user != '': 
		#Accessing tweepy (used my own access key)
			CONSUMER_KEY = 'M3VWcyQ7NyJ1hy6yR2FtQ'
			CONSUMER_SECRET = 'GAin1ygqcIl3E4nrolGv5J1kuEjPinjTSaQUrYrY90E'
			ACCESS_KEY = '396277518-tx1GBAqD6tncKPyUpLAY8KKe936rlRAgUdWLFVT3'
			ACCESS_SECRET = 'H6GBUexeISCDvtbEsikFv8f7AMk1GwMYlklPkC1SM'
		
			auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
			auth.set_request_token(ACCESS_KEY, ACCESS_SECRET)
	
			api = tweepy.API(auth)
		
		#getting statuses
			tweets = []
			for status in api.user_timeline(user, count = 200):
   				tweets.append(status)
   			
   		#writing them to webpage
			self.response.out.write(
				template.render('main.html', {'user': user, 'tweets': tweets}))	
			
	#if url is in incorrect format shows error
		else:
			self.response.out.write(
				template.render('input.html', {'query': user}))

	def post(self):
		user = self.request.get('user')
		add_url = '?user='+user
		self.redirect(add_url)	
		
		
#Main function
def main():
    application = webapp.WSGIApplication([
        (r'.*', MainPage)], debug=True)
    run_wsgi_app(application)

# Run the WSGI application
if __name__ == '__main__':
    main()
