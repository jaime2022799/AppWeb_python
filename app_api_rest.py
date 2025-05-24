from flask import Flask , jsonify , request

app = Flask(__name__)

stores = [

    {
        'name': 'hermosa tienda',
        'items': [

            {
                'name': 'flores',
                'price': 100
            }
        ]
    },
    {

        'name': 'hermosa tienda 2',
        'items': [

            {
                'name': 'libros',
                'price': 100
            }
        ]


    }

]

@app.route('/store/<string:name>')

def get_store(name):
    for store in stores:
        if(store['name']==name):
            return jsonify(store['name'])
    return jsonify({'mensaje': 'tienda no encontrada'})


@app.route('/store/<string:name>/item')

def get_store_items(name):
    for store in stores:
        if(store['name']==name):
            return jsonify(store['items'])
    return jsonify({'mensaje': 'tienda no encontrada'})

@app.route('/store', methods=['POST'])
def create_store():
    req_data = request.get_json()
    new_store={
        'name': req_data['name'],
        'items': [

        ]
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>/item', methods=['POST'])
def create_store(name):
    for store in stores:
        if(store['name']==name):
            req_data = request.get_json()
            new_item = {
                'name':req_data['data'],
                'price':req_data['price']
            }

@app.route('/')

def home():
    return "hey"

app.run(port=8000)
