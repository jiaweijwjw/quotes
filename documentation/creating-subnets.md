# Segmenting your home network using subnets vs VLANs

Guide on how to isolate the RPI in its own subnet which is separated from the main subnet which all the other devices in the home network connects to.

## Description

The home network has to be split up into smaller subnets to isolate the RPI from the main subnet where all the other devices are for security reasons. Devices on the main subnet should still be able to SSH into the RPI on the isolated subnet but the RPI should not be able to see the other devices on the main subnet. The RPI should also not be able to alter / configure anything on the route. 

The documentations here are just brief and simple for the sake of understanding the decisions made in the network setup for this project. For more detailed explanations on the concepts of networking and subnetting in general, take a look at [networkchuck](https://www.youtube.com/@NetworkChuck "networkchuck youtube profile")'s [subnetting playlist](https://www.youtube.com/playlist?list=PLIhvC56v63IKrRHh3gvZZBAGvsvOhwrRF "networkchuck subnetting playlist") on youtube.

The concept of subnets and VLANs is similar in the sense that they both split our main network into 2 different networks. The difference is the subnetting does it physically by introducing routers for each new subnet within the main subnet (devices within one router will contain devices with a specific range of IP addresses) while VLANs can be created virtually just by added an ethernet switch to an existing router (if the router doesnt already have the VLAN capability).

## DDNS
WAN IP stands for Wide Area Network IP and this is the public IP address that is assigned to the home router by your ISP (your internet service provider, such as Singtel, Starhub etc). This public IP address that is assigned to you is usually dynamic (DHCP on the ISP side). This mean that people who want to connect to your home network do not have a fixed IP address which they can search for. You can request for a fixed / static public IP address from you ISP but that would usually come at additional cost.  

A solution to this would be to use DDNS services. What these services would do is that they would provide you with a fixed domain name which the users can remember and use to connect to your network and they will also handle the changing of your public IP address for you. Notice that they are providing you with 2 services:  
1. DNS service by providing you with an easy to remember domain name for visitors to your network. Users would not want to be remembering numbers just to connect to your network / use your services.
2. The D (dynamic) in DDNS by helping you to manage your dynamic public IP address that is always changing.

I am using [No-IP](https://www.noip.com/ "No-IP homepage") (free) for my DDNS service. The DUC app is running on my Windows PC which will update no-ip whenever my public IP address changes. Port forwarding must be setup on the router to 

## IP Addressing
IP address is like the ID number used to verify devices on any network. There is only one public address that is being used in your home network and that is the public IP address that is assigned to your edge router via your ISP (As there is not enough IP addresses in IPv4). Everything else within your home network is considered to be within a private network and hence is using a private IP address. Your public IP address is unique worldwide, no one would have the same public IP address as you. But if you look at the private address that your devices have within your own home network, they could be the same number as the private IP address that your friend is having in their own home network too.   

You can check the network interface information on your device by running the command `ifconfig` in unix systems or `ipconfig` in windows. So all your devices within your private network will have to pass through the router which will do NAT (Network Address Translation) to 'convert' your private to public IP address and vice versa so that your devices within your private network can actually communicate the the internet with other devices. Within your home network, the router is also the one that does DHCP to assign a dynamic private IP address to your connected devices. (similar to how your ISP uses DHCP to assign a dynamic public IP address to your router / home network). In your own private network however, you can assign static private IP addresses to specific devices as you desire.

## Subnet
The netmask portion of out network tells us how many hosts can we have. If we take a look at the number of 0s in the netmask, that tells use the number of bits which can be used for our hosts.
> By default, the netmask is 255.255.255.0 which is 11111111.11111111.11111111.00000000 whereby 8 bits can be used for our hosts in a single subnet. This means that we have 2^8 private addresses available for use in the home network. This type of netmask which leaves 8bits for the hosts is also usually know as the /24 subnet, whereby 24 is the number of bits representing the network bits.

To increase the number of hosts, we can use a /23 subnet for example (255.255.254.0 / 11111111.11111111.11111110.00000000) to leave 9 bits for the hosts which can accomodate up to 512 IP addresses. To decrease the number of hosts, use lesser number of host bits and more network bits.

## VLAN
To separate my network into 2 parts, I will be adding a network ethernet switch to my main router. Configurations to the Firewalls have to be done so that devices on the main network VLAN will still be able to reach the RPI (via SSH) but the RPI should not be able to connect to devices in the other VLAN.