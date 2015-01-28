#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role
from flask.ext.script import Manager, Shell, Command, Option
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('LOLSS_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

class GunicornServer(Command):
    """Run app within Gunicorn"""

    def __init__(self, host='127.0.0.1', port=8000, workers=4):
        self.port = port
        self.host = host
        self.workers = workers

    def get_options(self):
        return (
            Option('-H', '--host',
                   dest='host',
                   default=self.host),

            Option('-p', '--port',
                   dest='port',
                   type=int,
                   default=self.port),

            Option('-w', '--workers',
                   dest='workers',
                   type=int,
                   default=self.workers),
        )

    def handle(self, app, host, port, workers):
        from gunicorn.base.app import Application

        class FlaskApplication(Application):
            def __init__(self, parser, opts, args):
                return {
                    'bind': '{0}:{1}'.format(host, port),
                    'workers': workers
                }

            def load(self):
                return app

        FlaskApplication().run()
        

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role) # Need to create the models so this can work

manager.add_command("shell", Shell(make_context=make_shell_context, use_ipython=True))
manager.add_command('db', MigrateCommand)
manager.add_command('gunicorn', GunicornServer())

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()

