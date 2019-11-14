#!/usr/bin/env python3

if __name__ == '__main__':  # pragma: no cover
  import sys
  import xml.etree.ElementTree as ET

  if len(sys.argv)==1:
    print('Usage:\n',sys.argv[0],' <input_file>')
    exit(0)
  
  infile_name = sys.argv[1]
  tree=ET.parse(infile_name)
  root=tree.getroot()

# for child in root:
#   print(child.tag, child.attrib)

# for address in root.findall("./host/address"):
#   print(address.get('addr'))
#   
# for service in root.findall("./host/ports/port/service"):
#   print(service.get('version'))
#   
# for host in root:
#   for service in host.findall("ports/port/service"):
#     print(service.get('version'))
      
  for host in root:
    for address in host.findall('address'):
      ipaddr=str(address.get('addr'))
      for service in host.findall("ports/port/service"):
        ver=str(service.get('version'))
        if(ver.find("Ubuntu")!=-1):
          print(f"{ipaddr}:  Ubuntu")