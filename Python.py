from jinja2 import Environment, FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('template.j2')

# Load data from YAML file
with open('interfaces.yml', 'r') as f:
    interfaces = yaml.safe_load(f)

cisco_config = template.render(data={"interfaces": interfaces})

with open('config.txt', 'w') as f:
    f.write(cisco_config)