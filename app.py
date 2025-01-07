from flask import Flask, render_template, request, jsonify
from convert import word_to_rgb

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    word = request.json.get('word', '')
    if not word:
        return jsonify({'error': 'No word provided'}), 400
    
    rgb = word_to_rgb(word)
    hex_color = '#{:02x}{:02x}{:02x}'.format(*rgb)
    
    return jsonify({
        'word': word,
        'rgb': rgb,
        'hex': hex_color,
        'colorhexa_url': f'https://www.colorhexa.com/{hex_color[1:]}'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 