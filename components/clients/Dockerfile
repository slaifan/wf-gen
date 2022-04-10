FROM ubuntu:20.04

RUN apt-get -y update && apt-get upgrade -y && apt-get install -y apt-transport-https

RUN apt-get update    
RUN apt-get install -y apt-utils debconf-utils dialog
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN echo "resolvconf resolvconf/linkify-resolvconf boolean false" | debconf-set-selections
RUN apt-get update
RUN apt-get install -y wireguard resolvconf iproute2

#COPY /home/slaifan/workspace/uni/honours/config/peer1/peer1.conf /etc/wireguard/wg0.conf

COPY ./peer1.conf /etc/wireguard/wg0.conf

RUN wg-quick up wg0

RUN ./capture.sh


