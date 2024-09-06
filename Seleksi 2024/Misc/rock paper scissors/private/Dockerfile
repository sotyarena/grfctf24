FROM ubuntu:22.04

RUN apt-get update \
&& apt-get install -y socat \
&& apt-get install -y gcc \
&& apt-get install -y gcc-multilib \
&& useradd -m -s /bin/rbash nightfury \
&& chown root:root -R /home/ 

WORKDIR /home/nightfury

COPY . .

RUN gcc chall.c -o chall \
&& chmod 755 -R /home/nightfury 

USER nightfury

CMD ["socat", "-dd", "TCP4-LISTEN:2001,fork,reuseaddr", "EXEC:./chall,pty,echo=0,raw,iexten=0"]
