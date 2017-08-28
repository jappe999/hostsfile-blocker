from sys import exit
from helper import Helper

class HostsFile(Helper):
	def __init__(self):
		if not Helper.is_sudo():
			# Cannot alter hosts file without superuser permission
			print('Please execute as administrator.')
			exit()
		self.__file_path = "/etc/hosts"

	@staticmethod
	def __generate_lines(domain):
		ips = ('0.0.0.0', '::0')
		subdomains = ('', 'www.')
		lines = []
		for ip in ips:
			for subdomain in subdomains:
				full_domain = "".join((subdomain, domain))
				line = (ip, full_domain, )
				lines.append(line)

		return lines

	def __is_in_file(self, regex):
		file_content = Helper.get_file_content(self.__file_path)
		return Helper.search(file_content, regex)[0]

	@staticmethod
	def __get_regex(ip, domain):
		return "[\#]*%s[\t]*%s" % (ip, domain, )

	""" The user can set his own hostsfile
	    if needed.
	"""
	def set_hosts_file(self, path):
		self.__file_path = path

	def __get_lines(self, domain, action):
		lines = HostsFile.__generate_lines(domain)
		response = []
		for line in lines:
			try:
				regex = HostsFile.__get_regex(line[0], line[1])
				is_in_file = self.__is_in_file(regex)
				if is_in_file == action:
					response.append(line)
			except Exception as e:
				print("Exception:", e)
				return False

		return response

	def allow(self, domain):
		lines = self.__get_lines(domain, True)
		if lines:
			for line in lines:
				Helper.remove_from_file(self.__file_path, "\t".join(line))
		return True

	def block(self, domain):
		lines = self.__get_lines(domain, False)
		if lines:
			for line in lines:
				print('Appending %s to the hostsfile' % (line[1], ))
				# Append a new line to the hosts file
				Helper.append_to_file(self.__file_path, "\t".join(line))

