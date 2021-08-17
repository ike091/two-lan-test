"""Two nodes with a router in the middle"""

import geni.portal as portal
import geni.rspec.pg as pg
import geni.rspec.emulab as emulab
import geni.rspec.igext as igext

# Create a portal object,
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

CENTOS7_IMG = 'urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD'

# Create some user-configurable parameters
pc.defineParameter('public_ip_count', 'The number of additional public IPs to allocate', portal.ParameterType.INTEGER, 2)

# TODO: validate parameters
params = pc.bindParameters()

# Gateway node
node_gw = request.RawPC('gw')
node_gw.disk_image = CENTOS7_IMG
node_gw.setFailureAction('nonfatal')
iface0 = node_gw.addInterface('eth0', pg.IPv4Address('192.168.1.3','255.255.255.0'))
iface1 = node_gw.addInterface('eth1', pg.IPv4Address('10.10.1.3','255.255.255.0'))

# Node in
node_in = request.RawPC('in')
node_in.disk_image = CENTOS7_IMG
node_in.setFailureAction('nonfatal')
iface2 = node_in.addInterface('eth0', pg.IPv4Address('10.10.1.2','255.255.255.0'))

# Node out
node_out = request.RawPC('out')
node_out.disk_image = CENTOS7_IMG
node_out.setFailureAction('nonfatal')
iface3 = node_out.addInterface('eth0', pg.IPv4Address('192.168.1.2','255.255.255.0'))

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

# Request a pool of dynamic publically routable ip addresses - pool name cannot contain underscores - hidden bug
addressPool = igext.AddressPool('addressPool', int(params.public_ip_count))
request.addResource(addressPool)

# Print the generated rspec
pc.printRequestRSpec(request)
