#! env python3
import falcon

from manage.packagehandler import PackageHandler
from manage.updatehandler import RepositoryHandler

app = falcon.API()

app.add_route('/package', PackageHandler())
app.add_route('/repository', RepositoryHandler())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()
