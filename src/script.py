from os import listdir
from os.path import abspath, dirname, join
from jinja2 import Environment, FileSystemLoader

def generate_page():
	src_path = dirname(abspath(__file__))
	public_path = abspath(join(src_path, '..', 'public'))
	images_path = abspath(join(public_path, 'images'))

	images = []
	for file in listdir(images_path):
		images.append("images/" + file)

	env = Environment(loader=FileSystemLoader(src_path))
	template = env.get_template('template.html')

	with open(join(public_path, 'index.html'), "wb") as file:
		file.write(template.render(images=images))

if __name__ == '__main__':
	generate_page()
