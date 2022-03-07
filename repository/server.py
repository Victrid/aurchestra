#! env python3
from wsgiref.simple_server import make_server
from manage.packagehandler import PackageHandler

import falcon

from manage.updatehandler import RepositoryHandler

app = falcon.API()

app.add_route('/package', PackageHandler())
app.add_route('/repository', RepositoryHandler())

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()