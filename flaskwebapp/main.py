from noodles.templates import create_app
# installed flask, flask login, flask sql alchemy using terminal
# the init file within website>templates makes the websites folder
# a python package
# runs everything within init

# note - import error prior to adding .templates  suffix

app = create_app(__name__) # added __name__ to get around error

if __name__ == '__main__':
    # only if we run this file, not import,
    # will this line be executed
    app.run(debug=True)
    # runs flask app, sorts web server


