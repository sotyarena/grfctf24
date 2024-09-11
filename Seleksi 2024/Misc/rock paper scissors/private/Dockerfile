FROM alpine:latest

WORKDIR /home/nightfury

RUN apk update \
&& apk add --no-cache socat gcc musl-dev libc6-compat bash \
&& ln -s /bin/bash /bin/rbash \
&& adduser nightfury -D -h /home/nightfury -s /bin/rbash \
&& chown root:root -R /home/ 

COPY . .

RUN gcc chall.c -o chall \
&& chmod 755 -R /home/nightfury

USER nightfury

CMD ["socat", "-dd", "TCP4-LISTEN:2001,fork,reuseaddr", "EXEC:./chall,pty,echo=0,raw,iexten=0"]
