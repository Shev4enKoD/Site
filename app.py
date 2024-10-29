from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'URL отсутствует'}), 400

    try:
        # Запуск yt-dlp для получения прямого URL к видео
        result = subprocess.run(['yt-dlp', '-f', 'best', '-g', url], capture_output=True, text=True, check=True)
        video_url = result.stdout.strip()
        return jsonify({'videoUrl': video_url})
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске yt-dlp: {e.stderr}")
        return jsonify({'error': 'Ошибка при получении видео', 'details': e.stderr}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
