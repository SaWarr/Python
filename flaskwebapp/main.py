# installed flask, flask login, flask sql alchemy using terminal
from noodles import create_app
# the init file within website>templates makes the websites folder
# a python package
# runs everything within init

app = create_app()

if __name__ == '__main__':
    # only if we run this file, not import,
    # will this line be executed
    app.run(debug=True)
    # runs flask app, sorts web server


