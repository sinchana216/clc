from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Student Application Form</title>
    </head>
    <body>
        <h1>Student Application Form</h1>
        <form action="/submit" method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required><br>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br>

            <!-- Add more form fields as needed -->

            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Process form data here
        name = request.form['name']
        email = request.form['email']
        # Add more form fields as needed

        # Perform any backend processing here

        return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Success</title>
        </head>
        <body>
            <h1>Application Submitted Successfully</h1>
            <p>Thank you, {name}, for submitting your application!</p>
        </body>
        </html>
        '''

if __name__ == '__main__':
    app.run(debug=True)
