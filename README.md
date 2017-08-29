# hostsfile-blocker
Block hosts with this simple pyhon library

## Dependencies
Just Python 3

## Usage
Execute \_\_main\_\_.py with admin rights. If you do not, you'll be notified to do so.
```
sudo python3 hostsfile-blocker
```
or
```
sudo python3 __main__.py
```
**Note:** Windows users, do not have to prefix the exectuion with _"sudo"_.

## Change the path to the hostsfile
If your hostsfile is located somewhere else than _/etc/hosts_, set the path to your hostsfile with the method _set_hosts_file_.  
  
### Windows hosts file
Usually the Windows hosts file is found under _C:\Windows\System32\drivers\etc\hosts_.

### MacOS hosts file
Usually the MacOS hosts file is found under _/private/etc/hosts_.

## Restrictions
Wildcards are not supported by the hostsfile
