from flask import Flask, request, jsonify
from flask_cors import CORS,cross_origin
import re
from calc import calc
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['POST','GET'])
@cross_origin()
def receive_expression():
    data = request.get_json()  # Get the JSON data from the request
    expression = data.get('expression').strip()  # Extract the 'expression' value from the JSON data
    if (expression[-1].isdigit() or expression[-1] ==')') and (expression[0].isdigit() or expression[0] =='(' or expression[0] == '+' or expression[0] == '-'): 
        list_expr = re.split(r'(\+|-|\*|/|\(|\))', expression)
        list_expr = [i for i in list_expr if i.strip()] 
        res,steps= calc(list_expr.copy())
        print(res,steps)
        # for i in range(len(steps)):
        #     r.append(eval(steps[i]))
        # steps[i] = steps[i] + " = " + str(r)
    else:
        res = "Invalid Expression"

    result = {
        'result': res, 
        'steps': steps
    }
    return jsonify(result)  # Return the result as JSON
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the app