FROM ubuntu:20.04

RUN apt-get update && apt-get install -y bind9 && apt-get clean

COPY bind /etc/bind

EXPOSE 53/udp
EXPOSE 53/tcp

CMD ["named", "-g", "-c", "/etc/bind/named.conf"]
