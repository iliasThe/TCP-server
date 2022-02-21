import socket
import xml.etree.ElementTree as xml

client = socket.socket()
client.connect(('127.0.0.1',5000))

objects=[{'BBBB':1241, 'x':'*', 'NN':12, 'x':'*', 'HH':50, 'x':'*', 'MM':13, 'x':'*', 'SS':14, 'x':'*', 'zhq':111, 'x':'*', 'GG':66, 'x':'*', 'name':'CR'
          }]
root = xml.Element("objects")
for object in objects:
       child=xml.Element("object")
       root.append(child)
       nm = xml.SubElement(child, "BBBB")
       nm.text = str(object.get('BBBB'))
       nn = xml.SubElement(child, "NN")
       nn.text = str(object.get('NN'))
       hh=xml.SubElement(child, "HH")
       hh.text=str(object.get('HH'))
       mm = xml.SubElement(child, "MM")
       mm.text = str(object.get('MM'))
       ss = xml.SubElement(child, "SS")
       ss.text = str(object.get('SS'))
       zhq = xml.SubElement(child, "zhq")
       zhq.text = str(object.get('zhq'))
       gg = xml.SubElement(child, "GG")
       gg.text = str(object.get('GG'))
       cr = xml.SubElement(child, "CR")
       cr.text = object.get('CR')
tree = xml.ElementTree(root)
with open('testcase-ddd.xml', "wb") as fh:
       tree.write(fh)
tree = xml.ElementTree(file='testcase-ddd.xml')
print(object)
client.close()
