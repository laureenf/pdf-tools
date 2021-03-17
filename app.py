from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_wtf import FlaskForm
from wtforms import MultipleFileField
from pdf_tools import merge, rotate, watermark

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/merge_pdf', methods=['GET', 'POST'])
def merge_pdf():
    if request.method == 'POST':
        files = request.files.getlist("files")
        if len(files) > 1:
            merge(files)
        return send_file('output.pdf', as_attachment=True)
    return render_template('pdf/merge_pdf.html', error_msg=None)

@app.route('/split_pdf', methods=['GET', 'POST'])
def split_pdf():
    return render_template('pdf/split_pdf.html')

@app.route('/rotate_pdf', methods=['GET', 'POST'])
def rotate_pdf():
    if request.method == 'POST':
        pdf = request.files['file']
        degree = int(request.form.get('degreeOfRotation'))
        rotate(pdf, degree)
        return send_file('output.pdf', as_attachment=True)
    return render_template('pdf/rotate_pdf.html')

@app.route('/watermark_pdf', methods=['GET', 'POST'])
def watermark_pdf():
    if request.method == 'POST':
        pdf = request.files['file']
        watermark_file = request.files['watermark_file']
        pages = request.form.get('typeOfWatermark')
        watermark(pdf, watermark_file, pages)
        return send_file('output.pdf', as_attachment=True)
    return render_template('pdf/watermark_pdf.html')

@app.route('/word_to_pdf', methods=['GET', 'POST'])
def word_to_pdf():
    return render_template('pdf/word_to_pdf.html')

@app.route('/pdf_to_word', methods=['GET', 'POST'])
def pdf_to_word():
    return render_template('pdf/pdf_to_word.html')

if __name__ == '__main__':
    app.run(debug=True)
