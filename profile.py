"""This is a trivial example of a gitrepo-based profile; The profile source code and other software, documentation, etc. are stored in in a publicly accessible GIT repository (say, github.com). When you instantiate this profile, the repository is cloned to all of the nodes in your experiment, to `/local/repository`. 

This particular profile is a simple example of using a single raw PC. It can be instantiated on any cluster; the node will boot the default operating system, which is typically a recent version of Ubuntu.

Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item. 
"""

# TODO: Create loops and arrays to remove redundent code

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# Add a raw PC to the request.
node1 = request.XenVM("node-1")
node2 = request.XenVM("node-2")
node3 = request.XenVM("node-3")
node4 = request.XenVM("node-4")

# Add interfaces for each node
nodeInterface1 = node1.addInterface("if1")
nodeInterface2 = node2.addInterface("if2")
nodeInterface3 = node3.addInterface("if3")
nodeInterface4 = node4.addInterface("if4")

# Add components for each interface for LAN
nodeInterface1.component_id = "eth1"
nodeInterface2.component_id = "eth2"
nodeInterface3.component_id = "eth3"
nodeInterface4.component_id = "eth4"

# Setting their local IPs and default gateways and assigning them to each interface
nodeInterface1.addAddress(pg.IPv4Address("192.168.1.1", "255.255.255.0"))
nodeInterface2.addAddress(pg.IPv4Address("192.168.1.2", "255.255.255.0"))
nodeInterface3.addAddress(pg.IPv4Address("192.168.1.3", "255.255.255.0"))
nodeInterface4.addAddress(pg.IPv4Address("192.168.1.4", "255.255.255.0"))

#Link the LAN
link = request.LAN("lan")

#Apply the interfaces of each node to the LAN
link.addInterface(nodeInterface1)
link.addInterface(nodeInterface2)
link.addInterface(nodeInterface3)
link.addInterface(nodeInterface4)

# Set the OS image to CentOS7 64bit as a URN to node.disk_image property
node1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
node2.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
node3.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
node4.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"

#Public ID Address for node1
node1.routable_control_ip = True

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
