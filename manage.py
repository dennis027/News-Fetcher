from app import create_app
# from flask_script import Manager, Server
from flask_script import Manager, Server

# creating an app instance
app= create_app('development')

manager = Manager(app)
manager.add_command('server',Server)