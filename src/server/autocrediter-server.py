import os
import re
import json

from urllib.parse import urlparse, unquote
from http.server import BaseHTTPRequestHandler, HTTPServer

__basename__ = os.path.dirname(__file__)
AUTHOR_FILE = os.path.join(__basename__, '../../credited_authors.json')

def extractInformationFromHTMLCredit(htmlCredit):
	"""
	@htmlCredit: given htmlCredit by "https://www.flaticon.com/" when you're saving icon.
	@return (author, url)
	"""
	url = ''
	author = ''
	try:
		# extract url and author from htmlCredit
		url = re.findall(r'(?<=href=").*?(?=")', htmlCredit)[0]
		author = re.findall(r'(?<=title=").*?(?=")', htmlCredit)[0]
	except:
		pass
	return author, url

def appendCreditToAuthorFile(author, url):
	global AUTHOR_FILE
	data = { 'author': author, 'url': url }

	if not os.path.exists(AUTHOR_FILE):
		# make author file
		open(AUTHOR_FILE, 'a').close()
		print('[✓] Author file created.')

	with open(AUTHOR_FILE, 'r') as file:
		# append new credit to author file
		content = '\n'.join([line for line in file])
		with open(AUTHOR_FILE, 'w') as file:
			# intialise atuhors array
			if content:
				authors = json.loads(content)
			else:
				authors = []

			# author is already saved ?
			isAlreadySaved = False
			for savedAuthor in authors:
				if savedAuthor['author'] == author:
					isAlreadySaved = True
					print('[✓] "%s" is already saved.' % (author))

			if not isAlreadySaved:
				# append new author in author file
				authors.append(data)
				print('[✓] "%s" from "%s" is now saved.' % (author, url))

			file.write(json.dumps(authors) + '\n')

class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		print('[✓] Got request.')
		parsed_path = urlparse(self.path)
		query = parsed_path.query
		htmlCredit = query[1:]
		htmlCredit = unquote(htmlCredit)
		information = extractInformationFromHTMLCredit(htmlCredit)
		appendCreditToAuthorFile(*information)
		self.send_response(200)
	
	def log_message(self, format, *args):
		return

class Server():
	def __init__(self):
		self.PORT = 8080
		self.ADDRESS = 'localhost'
	
	def start(self):
		server = HTTPServer((self.ADDRESS, self.PORT), RequestHandler)
		server.serve_forever()

if __name__ == '__main__':
	server = Server()
	server.start()
