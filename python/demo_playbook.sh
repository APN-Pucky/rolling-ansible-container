

# Download and seed the image
python3 rac.py --base debian --image apnpucky/python-rac-test --seed --playbook site.yaml 
# Don't seed the image again nothign should happen here loop this to debug
python3 rac.py --image apnpucky/python-rac-test --playbook site.yaml
# Third times a charm
python3 rac.py --base debian --image apnpucky/python-rac-test --flatten --push --playbook site.yaml 
