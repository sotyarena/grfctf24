FROM alpine:3.13

WORKDIR /home/bortus/

COPY . .

RUN apk update
RUN apk add --no-cache socat gcc musl-dev libc6-compat
RUN gcc chall.c -o chall -no-pie -fno-stack-protector

CMD ["socat", "-dd", "TCP4-LISTEN:2000,fork,reuseaddr", "EXEC:./chall,pty,echo=0,raw,iexten=0"]
