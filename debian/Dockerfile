ARG IMAGE=debian-rac-demo
FROM ${IMAGE} as debian-rac-demo
ADD https://raw.githubusercontent.com/APN-Pucky/rolling-ansible-container/master/bootstrap-rac.sh /bootstrap-rac.sh
RUN chmod +x /bootstrap-rac.sh && /bootstrap-rac.sh && rm /bootstrap-rac.sh 
COPY ansible /ansible/
RUN ansible-playbook -i localhost, --connection=local  /ansible/site.yaml && rm -r /ansible

#FROM debian as debian-rac-demo
#COPY --from=build / / 