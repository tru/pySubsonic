import web

urls = ('/rest/ping.view', 'ping')


def response(payload=None):
	ret = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\n"
	ret += "<subsonic-response xmlns=\"http://subsonic.org/restapi\" status=\"ok\" version=\"1.5.0\">\n"
	ret += "</subsonic-response>\n\n"
	return ret

class ping:
	def GET(self):
		return response()

app = web.application(urls, globals())


if __name__ == '__main__':
	app.run()


