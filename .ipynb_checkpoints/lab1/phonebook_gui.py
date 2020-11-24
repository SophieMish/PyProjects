from flask import Flask
import jinja2

app = Flask(__name__)


@app.route('/')
def hell():
    templateLoader = jinja2.FileSystemLoader(searchpath=".")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "tamplate1.j2"
    template = templateEnv.get_template(TEMPLATE_FILE)
    return template.render(tittle='Hello', header='Header', body='Body')

