FROM debian
ADD ./bootstrap-rac.sh /bootstrap-rac.sh
#ADD https://raw.githubusercontent.com/APN-Pucky/rolling-ansible-container/master/bootstrap-rac.sh /bootstrap-rac.sh
RUN chmod +x /bootstrap-rac.sh && /bootstrap-rac.sh && rm /bootstrap-rac.sh 
RUN . ansible-env/bin/activate && ansible localhost --connection=local  --module-name ping && deactivate