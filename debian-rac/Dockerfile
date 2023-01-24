FROM debian as debian-rac
ADD ./../bootstrap-rac.sh /bootstrap-rac.sh
#ADD https://raw.githubusercontent.com/APN-Pucky/rolling-ansible-container/master/bootstrap-rac.sh /bootstrap-rac.sh
RUN chmod +x /bootstrap-rac.sh && /bootstrap-rac.sh && rm /bootstrap-rac.sh 