import conf

def has_valid_extension(filename):
    return filename.rsplit('.', 1)[0] in conf.ALLOWED_EXTENSIONS
