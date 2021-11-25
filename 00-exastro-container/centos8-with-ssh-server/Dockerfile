FROM centos:8

# Update root CA
RUN --mount=type=secret,id=extra-root-ca \
if [ -f /run/secrets/extra-root-ca ]; then \
    cp /run/secrets/extra-root-ca /usr/share/pki/ca-trust-source/anchors/extra-root-ca.crt; \
    update-ca-trust; \
fi

RUN dnf -y install openssh-server
RUN echo 'root:password' | chpasswd

ENTRYPOINT ["/sbin/init"]
