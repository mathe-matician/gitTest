import os 
from flask import Flask

app = Flask(__name__)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename is not None:
            path = os.path.join(app.root_path, endpoint, filename)
            values['ts'] = int(os.stat(path).st_mtime)
    return url_for(endpoint, **values)
