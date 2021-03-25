import re

from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_wtf import FlaskForm
from wtforms import MultipleFileField
from pdf_tools import merge, split, rotate, watermark, encrypt

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
    if request.method == 'POST':
        pdf = request.files['file']
        ranges = request.form.get('range')

        regexObj = re.compile(r'\d+-\d+|\d+')
        matches = regexObj.findall(ranges)
        range_list = []
        page_list = []
        for match in matches:
            if '-' in match:
                left, right = match.split('-')
                if left < right and int(left) > 0 and int(right) > 0:
                    range_list.append([int(left), int(right)])
            else:
                if int(match) > 0:
                    page_list.append(int(match))

        if range_list == [] and page_list == []:
            return render_template('pdf/split_pdf.html', error = 'Invalid range specification')
        else:
            split(pdf, range_list, page_list)
            return send_file('new.zip', as_attachment=True, mimetype='zip')
    
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

@app.route('/encrypt_pdf', methods=['GET', 'POST'])
def encrypt_pdf():
    if request.method == 'POST':
        pdf = request.files['file']
        password = request.form.get('password')
        encrypt(pdf, password)
        return send_file('output.pdf', as_attachment=True)
    return render_template('pdf/encrypt_pdf.html')

@app.route('/word_to_pdf', methods=['GET', 'POST'])
def word_to_pdf():
    return render_template('pdf/word_to_pdf.html')

if __name__ == '__main__':
    app.run(debug=True)