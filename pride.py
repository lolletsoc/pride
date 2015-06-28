from flask import Flask, make_response
from werkzeug.exceptions import BadRequest
import conf
from images import convert_image_with_vote
from utils import has_valid_extension


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = conf.MAXIMUM_FILE_SIZE

_FILE_NAME = "{vote}_{filename}"
CONTENT_DISPOSITION = "attachment; filename={}".format(_FILE_NAME)


@app.route('/pride', methods=['POST'])
def be_proud(request):
    vote = request.form.get('vote')
    if not vote:
        return BadRequest('A vote must be provided')

    image = request.files['image']
    if not has_valid_extension(image.filename):
        return BadRequest('File type is not supported')

    converted_image = convert_image_with_vote(image, vote)

    response = make_response(converted_image)
    response.headers["Content-Disposition"] = CONTENT_DISPOSITION.format(
        filename=converted_image.filename, vote=vote
    )

    return response

if __name__ == "__main__":
    app.run()
