# Exposing the RPI

Quick guide on Ubuntu server setup.

## Description
The hardware which I am using to host my Ubuntu server (headless) is the Raspberry Pi Model 4B (RPI4). It is hosted within in my own home. The purpose of hosting this server is to try out managing my own Linux server on actual hardware rather than inside a VM. There are some requirements which has to be follow to exposing the RPI4 publicly.

### Requirements (In order of priority):
1. Has to be safe and secure.
2. Able to manage it headlessly from within my own home network (Windows PC / Macbook) or remotely from anywhere with Macbook.
3. Allow trusted users to also connect to the server and use it.

## Implementation
* **Subnet segmentation**  
~~The subnet that the RPI4 is on will be isolated from the main subnet where all my other devices are connected to. This will be configured on the router. By default (usually), the separately subnets will not be able to communicate with each other. But it can be configured in such a way that the main subnet will still be able to connect to the RPI on the isolated subnet, but not the other way round. This is for the purpose of SSH-ing into the RPI for development stuff via my Windows PC / Macbook on the main subnet.~~

* **VLAN**
Subnetting requires >1 router which is not necessary to setup for a home environment. Instead, we will be using VLANs (Virtual LAN) instead, which can help us to separate our home network into 2 networks virtually rather than physically (subnetting). Only high end routers come with the VLAN (ethernet switch) capability. Else, we would have to buy an additional switch to implement the VLAN functionality.

* **VPN**  
VPN is a much more secure way for allowing users to 'come into' my network. In this case, the VPN will be setup on the RPI. How it works is that trusted users / my remote devices not connecting from the main subnet will have to establish a VPN connection with the RPI. It will first hit the router which is supposed to port forward the VPN initiation to the RPI. If the VPN connection is successful, the user's device can be thought of as being in the same network as the RPI. Hence the subnet segmentation above is also to prevent the users in this isolated subnet to access my other devices in the main network. Once the user is within the same network as the RPI, they can then SSH into the RPI4 (if they have the credentials). SSH-ing into the RPI4 would be for them to access any development services such as Jenkins / Database server being hosted on the RPI (Only for configuring the services, if just want to use the services, see below in the firewall section). 

* **Firewalls**  
Firewall (software) is setup such that currently only the SSH port is open for incoming traffic. If any other services is to be opened up for using directly, the respective ports will be opened up accordingly. Using directly means to just use whatever is currently already setup and running as a service, such as running the Jenkins CI/CD pipeline or accessing a Database. If want to configure these services, have to SSH into the linux server itself. A whitelist of IP address is also setup for access to the server itself. Hence trusted users who are connecting to the RPI via VPN should use the same VPN common name (on any of their devices) so as to be assigned a fixed IP address everytime they connect so as to be able to bypass the whitelist on the intrusion prevension system (Fail2ban). Also, if trusted users get themselves logged out due to other reaons (such as wrong password too many times), please contact me to be assigned a new IP address for your VPN.

* **External services (public)**  
External services such as API endpoints has to be exposed publicly. We cannot expect a user to require a VPN connection before being able to call an API. Hence we would have to expose a port on the router and forward it to the respective port on the RPI. The necessary precautions and protections have to be setup in this case. Trusted users will have to contact me with regards to forwarding any ports publicly.

## Diagram:
*To be added*

*... To be continued*