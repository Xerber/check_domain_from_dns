## Details what he does:
on the Internet provider, there was a task to block access to some sites and, 
accordingly, a task appeared to check if the domain is actually blocked on several dns. 
This script runs through a file with domains, makes a list and checks nslookup through the specified dns list

If you want to run my script, you will need to install requirements
```
pip install -r requirements.txt
```
and write your data to the config.py