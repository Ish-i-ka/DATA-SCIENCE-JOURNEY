## Put and Delete
## Working with API's -- Json

from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial Data in to-do list
items = [
    {
        'id': 1,
        'name': 'item1',
        'description': 'This is item1'
    },
    {
        'id': 2,
        'name': 'item2',
        'description': 'This is item2'
    }
]

@app.route('/')
def home():
    return f"Welcome to my TO-DO LIST App"

#GET: Retrieve all items
@app.route("/items",methods=['GET'])
def get_items():
    return jsonify(items)

#GET: Retrieve a specific item based on id
@app.route("/items/<int:item_id>",methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item['id'] == item_id),None)       #using next we get the next item from the iterator, if there is no match then none returned
    if item is None:
        return jsonify({"Error":"Item not found"})
    return jsonify(item)

#POST: Create a new task
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:                  #checks wether the item is in json format or whether it has 'name' key
        return jsonify({"Error":"Item not found"})
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json["description"]
    }
    items.append(new_item)
    return jsonify(new_item)        #shows the new item added in json format

## PUT: Update an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"Error":"Item not found"})
    item['name'] = request.json.get('name',item['name'])        #in place of original 'name' new 'name' is updated by taking it from request.json
    item['description'] = request.json.get('description',item['description'])
    return jsonify(item)

##DELETE: del an item
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"result": "Item deleted"})


if __name__ == "__main__":
    app.run(debug=True)