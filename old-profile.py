"""Sets up two VMs on two separate LANs"""

#
# NOTE: This code was machine converted. An actual human would not
#       write code like this!
#

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal object,
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Node node-0
node_0 = request.XenVM('node-0')
node_0.Site('Site 2')
iface0 = node_0.addInterface('interface-0', pg.IPv4Address('192.168.1.1','255.255.255.0'))

# Node node-1
node_1 = request.XenVM('node-1')
iface1 = node_1.addInterface('interface-1', pg.IPv4Address('10.10.1.1','255.255.255.0'))

# Link link-0
link_0 = request.Link('link-0')
link_0.addInterface(iface0)
link_0.addInterface(iface1)


# Print the generated rspec
pc.printRequestRSpec(request)

