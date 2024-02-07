from flask import Flask, request, jsonify
from user import User

app = Flask(__name__)

# Dictionary to store user information
users = {
    "u1": User("u1", "User1", "user1@example.com", "1234567890"),
    "u2": User("u2", "User2", "user2@example.com", "9876543210"),
    "u3": User("u3", "User3", "user3@example.com", "1112223333"),
    "u4": User("u4", "User4", "user4@example.com", "4445556666")
}

# Split Equal Endpoint
@app.route('/split_equal', methods=['POST'])
def split_equal():
    try:
        data = request.get_json()
        payer_id = data['payer_id']
        payer_amount = data['payer_amount']
        participants = data['participants_details']
        
        # Calculate share per participant
        share = payer_amount / len(participants)
        
        # Update balances
        for participant in participants:
            participant_id = participant['participant_id']
            users[participant_id].put_owe(payer_id, share)
            users[payer_id].put_spend(participant_id, share)
        
        return jsonify({"message": "Expense split equally among participants"})
    except Exception as e:
        return jsonify({"Error": str(e)}), 404

# Split Exact Endpoint
@app.route('/split_exact', methods=['POST'])
def split_exact():
    try:
        data = request.get_json()
        payer_id = data['payer_id']
        payer_amount = data['payer_amount']
        participants = data['participants_details']

        # Validate total amount
        total_amount = 0

        for participant in participants:
            total_amount += participant['participant_amount']
        
        if(total_amount != payer_amount):
            return jsonify({"Error": "Total amount not matches to payer amount"}), 404
        
        for participant in participants:
            participant_id = participant['participant_id']
            amount = participant['participant_amount']

            users[participant_id].put_owe(payer_id, amount)
            users[payer_id].put_spend(participant_id, amount)
        
        return jsonify({"message": "Expense split with exact amounts among participants"}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 404

# Split Percentages Endpoint
@app.route('/split_percentages', methods=['POST'])
def split_percentages():
    try:
        data = request.get_json()
        payer_id = data['payer_id']
        payer_amount = data['payer_amount']
        participants = data['participants_details']

        # Validate total percentage
        total_percentage = 0

        for participant in participants:
            total_percentage += round(participant['participant_percentage'], 2)
        
        total_percentage = round(total_percentage)
        
        if(total_percentage != 100):
            return jsonify({"Error": "Total percantage exceeded to 100%"}), 404

        # Update users owe
        for participant in participants:
            participant_id = participant['participant_id']
            participant_percentage = round(participant['participant_percentage'], 2)

            amount = payer_amount*(participant_percentage/100)
            amount = round(amount)

            users[participant_id].put_owe(payer_id, amount)
            users[payer_id].put_spend(participant_id, round(amount))
        
        return jsonify({"message": "Expense split based on percentages among participants"}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 404


# Show Balences 
@app.route('/show_balance/<user_id>', methods=['GET'])
def show_balance(user_id):
    return jsonify({"message": f"User ID: {users[user_id]}"}), 200

if __name__ == '__main__':
    app.run(debug=True)
