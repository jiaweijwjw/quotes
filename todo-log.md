## To do list
- install kubernetes on ubuntu server
- install docker on ubuntu server
- install mariadb server on ubuntu server
- setup kubernetes cluster
- running mariadb in a docker container
- open the ports on ubuntu server to allow mariadb access

- setup isolated subnet for rpi4
- setup vpn to rpi4 with openVPN
- setup fixed ip address to a specific user from openvpn (for trusted users)
- test ssh connection to rpi4 via vpn (test using hotspot)
- test connection from main subnet to isolated subnet and vice versa
- Setup fail2ban to whitelist specific ip_addresses only (from main subnet and fixed ip from openvpn set above)
-
- use SSH key pairs instead of password
- how does ipaddressing whitelist work on fail2ban if my raspberrypi is located within my home network?
- setup vpn tunneling for ssh connections (allows host to access other devices but other users only access to ubuntu server)
- setup
- Migrate simple FastAPI code base
- Open up RPI4 publicly
- setup mypy and pylint
- setup jfrog artifactory
- setup a simple jenkins pipeline to rebuild fastapi everytime we push to github

## Work done logs

- Install Ubuntu server on RPI4
- Initial setup (README etc)
- Installed firewall on Ubuntu server to allow on SSH connections



## Important things to checkout
- how to back up my server after i do all these settings?
    - full system backup (will the image size be the same as the current system? how to verify?)
    - rsnapshot (similar to timemachine, using rsync and config to save at certain intervals)