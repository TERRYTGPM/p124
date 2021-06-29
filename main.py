from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "c": "8826084333",
        "name": "jotaro"
    },
    {
        "c": "1234567890",
        "name": "naruto"
    }
]

@app.route("/data", methods={"POST"})

def e():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        }, 30000)
    
    contact = {
        "c": contacts[-1]["c"]+1, 
        "name": request.json("name"),
    }

    contacts.append(contact)

    return jsonify({
        "status": "sucess",
        "message": "task added succesfully"
    })

@app.route("/get-data")

def gt():
    return jsonify({
        "data": contacts
    })

if __name__ == "__main__":
    app.run()