import webapp2


class HelloWebApp2(webapp2.RequestHandler):
    """docstring for HelloWebApp2
    """

    def get(self):
        self.response.write('Hello WebApp 2!')


app = webapp2.WSGIApplication(
    [
        ('/', HelloWebApp2),
    ],
    debug=True
)


def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='36080')


if __name__ == '__main__':
    main()
