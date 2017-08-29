from hostsfile import HostsFile

if __name__ == '__main__':
	domain_list = open('domain-list.txt')
	hostsf = HostsFile()
	for host in map(lambda s: s.strip(), domain_list.readlines()):
		hostsf.block(host)

	domain_list.close()
