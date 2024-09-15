import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Function to get a random image URL
def fetch_random_image_url():
    # Use Lorem Picsum to get a random image URL
    return "https://picsum.photos/600/400"

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to get a new random image and return puzzle data
@app.route('/get_image/<difficulty>')
def get_image(difficulty):
    try:
        # Fetch a random image URL
        image_url = fetch_random_image_url()
        
        # Set the number of pieces based on difficulty
        pieces = {'easy': 20, 'medium': 50, 'hard': 90}
        num_pieces = pieces.get(difficulty, 20)
        
        return jsonify({
            'image_url': image_url,
            'num_pieces': num_pieces
        })
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
