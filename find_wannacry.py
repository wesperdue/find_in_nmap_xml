#!/usr/bin/env python3

if __name__ == '__main__':  # pragma: no cover
  import sys
  import xml.etree.ElementTree as ET
  import os.path

  if len(sys.argv)==1:
    print('Usage:\n',sys.argv[0],' <input_file>')
    exit(0)

  for x in range(1,len(sys.argv)):
    infile_name = sys.argv[x]
    if os.path.isfile(infile_name):
      tree=ET.parse(infile_name)
      root=tree.getroot()
        
      for host in root:
        for address in host.findall('address'):
          ipaddr=str(address.get('addr'))
          for script in host.findall('hostscript'):
            # print(f"{ipaddr}:  Wannacry")
            print(ipaddr)
              
    else:
      print("Error: File "+infile_name+" not found")