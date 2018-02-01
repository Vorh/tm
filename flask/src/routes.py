from src import fl

@fl.route('/')
@fl.route('/index')
def index():
    return "Hello, World!"