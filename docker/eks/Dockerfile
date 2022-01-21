#FROM harbor.infra.wish-cn.com/wish/wish-framework-portal/api-base:latest
FROM wish-framework-portal-base:latest
USER app
ADD . /home/app/wish-framework-portal
RUN pip --exists-action w --use-deprecated=legacy-resolver install -r /home/app/wish-framework-portal/app/backend/requirements

WORKDIR /home/app/wish-framework-portal/app/frontend
RUN sudo chmod 777 ./ ./*
RUN npm install

WORKDIR /home/app
RUN git clone https://github.com/Conan-shen/marlon-tools.git

USER root
ADD ./docker/wish-framework-portal.conf /etc/nginx/conf.d/

WORKDIR /home/app

CMD ["/bin/bash", "-c", "while true ; do sleep 3600; done"]
