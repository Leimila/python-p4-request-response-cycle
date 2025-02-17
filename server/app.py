import os
from flask import Flask, request, current_app, g, make_response, redirect, abort

app = Flask(__name__)

# Before request hook to set global path variable
@app.before_request
def set_app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')  # Get the host from request headers
    appname = current_app.name  # Get the application name from Flask
    
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''
    
    response = make_response(response_body, 200)  # Create an HTTP response with status code 200
    return response

@app.route('/custom-status')
def custom_status():
    return "This request was accepted but not yet processed.", 202  # Custom status code 202

@app.route('/redirect-example')
def redirect_example():
    return redirect('https://www.example.com')  # Redirect to example.com

@app.route('/error/<string:stage_name>')
def get_name(stage_name):
    fake_database = ['Elton John', 'Freddie Mercury', 'David Bowie']  # Simulated database
    if stage_name not in fake_database:
        abort(404)  # Return 404 if the name isn't found
    return f'<h1>{stage_name} is a known stage name!</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
