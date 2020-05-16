from nslookup import Nslookup
import logging
from config import dnslist, name_file


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

f1=[]

with open(name_file, encoding='utf-8') as file:
  for i in file:
    f1.append(i.strip('\n'))

for dns in dnslist:
  for domain in f1:
    domain = domain.encode('idna')
    domain = domain.decode('utf-8')
    dns_query = Nslookup(dns_servers=[dns])
    ips_record = dns_query.dns_lookup(domain)
    if '127.0.0.1' not in ips_record.answer:
      domain = domain.encode('idna')
      domain = domain.decode('idna')
      logging.warning(f'{domain}:{dns}')
    else: pass
