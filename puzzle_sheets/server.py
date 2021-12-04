import os
import tempfile
from flask import Flask, flash, request, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
from puzzle_sheets import puzzle_parser


UPLOAD_FOLDER = tempfile.TemporaryDirectory(suffix='_puzzle_sheets')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER.name
app.config['MAX_CONTENT_LENGTH'] = 10 * 1000  # 10 KB


@app.route('/', methods=['GET', 'POST'])
def process_puz():
    if request.method == 'GET':
        return '''
        <!doctype html>
        <title>Puzzle Sheets</title>
        <h1>Process PUZ File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Submit>
        </form>
        '''

    # POST
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and file.filename.upper().endswith('.PUZ'):
        filename = secure_filename(file.filename)
        tstamp = puzzle_parser.get_timestamp_str()
        puz_name = f'{tstamp}_{filename}'
        puz_path = os.path.join(app.config['UPLOAD_FOLDER'], puz_name)
        file.save(puz_path)

        puzzle = puzzle_parser.validate(puz_path)
        if puzzle is None:
            flash(f'Invalid file {file.filename}')
            return redirect(request.url)
        xlsx_name = puzzle_parser.get_xlsx_path(puz_name, include_timestamp=False)
        xlsx_path = os.path.join(app.config['UPLOAD_FOLDER'], xlsx_name)
        puzzle_parser.write_xlsx(puz_path, puzzle, xlsx_path)
        return send_from_directory(app.config['UPLOAD_FOLDER'], secure_filename(xlsx_name))