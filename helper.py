from os import getuid
import re

class Helper:
	@staticmethod
	def is_sudo():
		return (getuid() == 0)

	@staticmethod
	def get_file_content(path):
		file = open(path, 'r+')
		file_content = file.readlines()
		file.close()
		return file_content

	@staticmethod
	def append_to_file(path, content):
		file = open(path, 'a')
		file.write(content + "\n")
		file.close()

	@staticmethod
	def remove_from_file(path, content):
		file = open(path, 'r+')
		lines = file.readlines()
		file.close()
		new_content = [line for line in lines if line.strip() != content]

		file = open(path, 'w+')
		try:
			file.writelines(new_content)
			print('Removed %s' % (content, ))
		except Exception as e:
			print('Cannot remove from file:', e)
		finally:
			file.close()

	@staticmethod
	def search(data, regex):
		for row in data:
			match = re.match(regex, row.strip())
			if match:
				return (True, match.group(0), )

		return (False, None, )
