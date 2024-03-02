from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/updates')
def get_updates():
    try:
        repository_owner = 'your_username'
        repository_name = 'your_repository'

        response = requests.get(f'https://api.github.com/repos/{repository_owner}/{repository_name}/releases')
        releases = response.json()
        updates = [{
            'name': release['name'],
            'tag_name': release['tag_name'],
            'body': release['body'],
            'published_at': release['published_at']
        } for release in releases]

        return jsonify(updates)
    except Exception as e:
        return jsonify({'error': 'Failed to fetch updates. Please try again later.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
