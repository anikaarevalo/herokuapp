from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/Hello World', methods=["POST", "GET"])

def hello_world():
  user = {'salary':'2500', 'bonus':'200', 'taxes':'400'}
  if user['salary'].isdigit() and user['bonus'].isdigit() and user['taxes'].isdigit():
    pay = int(user.get('salary')) + int(user.get('bonus')) - int(user.get('taxes'))
    return str(pay)
  else:
    return 'error : expected numbers, got strings.'
  if len(user.keys()) < 3:
    if 'salary' in user and 'bonus' in user:
      return 'error:'  f'3 fields expected {user.keys()}. Pls. include: taxes.'
    if 'salary' in user and 'taxes' in user:
      return 'error:' f'3 fields expected {user.keys()}. Pls. include: bonus.'
    if 'taxes' in user and 'bonus' in user:
      return 'error:' f'3 fields are expected {user.keys()}. Pls include: salary.'

if __name__ == '__main__':
   app.run(port=5000)