from os import listdir, walk
import zipfile
from os.path import abspath, dirname, join
from jinja2 import Environment, FileSystemLoader

class Image:
	def __init__(self, src, number):
		self.src = src
		self.number = number

def generate_page():
	src_path = dirname(abspath(__file__))
	public_path = abspath(join(src_path, '..', 'public'))
	images_path = abspath(join(public_path, 'images'))
	zip_path = abspath(join(public_path, 'ReckerWeddingPictures.zip'))

	images = []
	i = 1
	for file in sorted(listdir(images_path)):
		if file != '.gitignore':
			images.append(Image(file, i))
			i = i + 1

	env = Environment(loader=FileSystemLoader(src_path))
	template = env.get_template('template.html')

	with open(join(public_path, 'index.html'), "wb") as file:
		file.write(template.render(images=images))

	zipper(images_path, zip_path)


def zipper(dir, zip_file):
    zip = zipfile.ZipFile(zip_file, 'w', compression=zipfile.ZIP_DEFLATED)
    root_len = len(abspath(dir))
    for root, dirs, files in walk(dir):
        archive_root = abspath(root)[root_len:]
        for f in files:
        	if f != '.gitignore':
	            fullpath = join(root, f)
	            archive_name = join(archive_root, f)
	            print f
	            zip.write(fullpath, archive_name, zipfile.ZIP_DEFLATED)
    zip.close()
    return zip_file

if __name__ == '__main__':
	generate_page()
