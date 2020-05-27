from nslookup import Nslookup
import logging
from config import dnslist, name_file


logging.basicConfig(format='%(message)s', level=logging.INFO)

f1=[]
with open(name_file, encoding='utf-8') as file:
  for domain in file:
    domain = domain.strip('\n').strip().encode('idna').decode('utf-8')
    f1.append(domain)
    f1.append('www.'+domain)


for dns in dnslist:
  dns_query = Nslookup(dns_servers=[dns])
  not_black=[]
  broken=[]
  for domain in f1:
    ips_record = dns_query.dns_lookup(domain)
    domain = domain.encode('idna').decode('idna')
    if len(ips_record.answer) > 0:
      if '127.0.0.1' not in ips_record.answer:
        not_black.append(domain)
      else: pass
    else:
      if domain not in broken:
        broken.append(domain)
      else: pass

  if len(broken)>0 or len(not_black)>0:
    logging.warning(f'{dns}')
    if len(not_black)>0:
      logging.warning(f'Finded {len(not_black)} unblocked domains')
      for black in not_black:
        logging.warning(f'nslookup {black} {dns}')
    if len(broken)>0:
      logging.warning(f'\nUnidentified {len(broken)} domains: Non-existent domain')
      for domain in broken:
        logging.warning(domain)
    logging.warning('#'*10)
