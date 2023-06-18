

# Download and seed the image
rac --image apnpucky/python-rac-playbook-test:latest --seed debian --playbook site.yaml 
# Don't seed the image again nothign should happen here loop this to debug
rac --image apnpucky/python-rac-playbook-test:latest --playbook site.yaml
# Third times a charm
rac --image apnpucky/python-rac-playbook-test:latest --flatten --push --playbook site.yaml 
