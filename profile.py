"""Two nodes with a router in the middle"""

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

# Node gw
node_gw = request.RawPC('gw')
node_gw.component_id = 'urn:publicid:IDN+utah.cloudlab.us+node+hp044'
node_gw.hardware_type = 'xl170'
node_gw.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU16-64-STD'
node_gw.setFailureAction('nonfatal')
iface0 = node_gw.addInterface('eth0', pg.IPv4Address('10.1.2.3','255.255.255.0'))
iface1 = node_gw.addInterface('eth1', pg.IPv4Address('10.1.1.3','255.255.255.0'))

# Node in
node_in = request.RawPC('in')
node_in.component_id = 'urn:publicid:IDN+utah.cloudlab.us+node+hp047'
node_in.hardware_type = 'xl170'
node_in.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU16-64-STD'
node_in.setFailureAction('nonfatal')
iface2 = node_in.addInterface('eth0', pg.IPv4Address('10.1.1.2','255.255.255.0'))

# Node out
node_out = request.RawPC('out')
node_out.component_id = 'urn:publicid:IDN+utah.cloudlab.us+node+hp048'
node_out.hardware_type = 'xl170'
node_out.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU16-64-STD'
node_out.setFailureAction('nonfatal')
iface3 = node_out.addInterface('eth0', pg.IPv4Address('10.1.2.2','255.255.255.0'))

# Link in-link
link_in_link = request.Link('in-link')
link_in_link.trivial_ok = True
link_in_link.addInterface(iface2)
link_in_link.addInterface(iface1)

# Link out-link
link_out_link = request.Link('out-link')
link_out_link.trivial_ok = True
link_out_link.addInterface(iface3)
link_out_link.addInterface(iface0)

request.setRoutingStyle('static')

# Print the generated rspec
pc.printRequestRSpec(request)
