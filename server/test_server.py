from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from main import speech_to_latex

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')


@app.route('/process_audio', methods=['GET', 'POST'])
def process():
    # we dont care about security for now
    if request.method == 'POST':
        f = request.files['audio_input']
        f.save('audio.wav')

        (wit_result, wolfram_interpretation, preprocessed, image_name) = speech_to_latex('audio')
        return render_template('result.html', wit_result=wit_result,
                               wolfram_interpretation=wolfram_interpretation,
                               preprocessed=preprocessed,
                               latex=image_name)


@app.route('/get_latex/<filename>')
def get_image(filename):
    return send_file(filename, mimetype='image/png')


@app.route('/run_with_sample')
def run_with_sample():
    (wit_result, wolfram_interpretation, preprocessed, image_name) = speech_to_latex('../audio_input')

    return render_template('result.html', wit_result=wit_result,
                           wolfram_interpretation=wolfram_interpretation,
                           preprocessed=preprocessed,
                           latex=image_name)
