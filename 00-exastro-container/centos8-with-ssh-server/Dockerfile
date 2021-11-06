FROM centos:8

RUN dnf -y install openssh-server
RUN echo 'root:password' | chpasswd

ENTRYPOINT ["/sbin/init"]
