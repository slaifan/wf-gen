FROM ymuski/nginx-quic

COPY ./src/ /etc/nginx/
CMD [ "bash", "-c", "-l", "nginx", "-g", "daemon", "off"]
# "&&", "bash", "-c", "-l", "nginx", "-c", "/etc/nginx/", "&&", "bash", "-c", "-l", "nginx", "-s", "reload"]
