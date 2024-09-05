FROM ubuntu:22.04

WORKDIR /home/bortus/

COPY . .

RUN apt-get update \
&& apt-get install -y socat \
&& apt-get install -y gcc \
&& apt-get install -y gcc-multilib \
&& gcc chall.c -o chall -no-pie -fno-stack-protector -m32

CMD ["socat", "-dd", "TCP4-LISTEN:2000,fork,reuseaddr", "EXEC:./chall,pty,echo=0,raw,iexten=0"]
