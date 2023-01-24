

# Download and seed the image
python3 rac.py --image apnpucky/python-rac-playbook-test:latest --seed debian --playbook site.yaml 
# Don't seed the image again nothign should happen here loop this to debug
python3 rac.py --image apnpucky/python-rac-playbook-test:latest --playbook site.yaml
# Third times a charm
python3 rac.py --image apnpucky/python-rac-playbook-test:latest --flatten --push --playbook site.yaml 
