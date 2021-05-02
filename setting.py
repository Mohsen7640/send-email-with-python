from jinja2 import Environment, FileSystemLoader
import os


path = os.path.dirname(__file__)
env = Environment(
    loader=FileSystemLoader(f'{path}/templates/')
)

template = env.get_template('email.html')
render = template.render(
    currency={'BTC': 12, 'USD': 3.5}
)
