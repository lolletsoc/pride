from flask import Flask, send_file, request
from werkzeug.exceptions import BadRequest
import conf
from images import convert_image_with_vote
from utils import has_valid_extension


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = conf.MAXIMUM_FILE_SIZE

FILE_NAME = "{vote}_{filename}"


@app.route('/pride', methods=['POST'])
def be_proud():
    vote = request.form.get('vote')
    if not vote:
        return BadRequest('A vote must be provided')

    image = request.files['image']
    if not has_valid_extension(image.filename):
        return BadRequest('File type is not supported')

    converted_image = convert_image_with_vote(image, vote)

    response = send_file(converted_image,
                         as_attachment=True,
                         attachment_filename=FILE_NAME.format(
                             vote='no', filename=image.filename
                         ))

    return response

if __name__ == "__main__":
    app.run(debug=True)
