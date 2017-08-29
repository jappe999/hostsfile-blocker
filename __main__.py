from hostsfile import HostsFile

if __name__ == '__main__':
	domain_list = open('domain-list.txt')
	hostsf = HostsFile()

	""" If your hostsfile is somewhere different than /etc/hosts,
	    you can set it with the method below.
	"""
	# hostsf.set_hosts_file('')

	for host in map(lambda s: s.strip(), domain_list.readlines()):
		hostsf.block(host)

	domain_list.close()
