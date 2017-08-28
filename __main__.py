from hostsfile import HostsFile

hosts = [
'facebook.com',
'google.com'
]

if __name__ == '__main__':
	hostsf = HostsFile()
	for host in hosts:
		hostsf.block(host)
