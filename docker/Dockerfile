FROM ubuntu:22.04
EXPOSE 1729/tcp
RUN echo "deb https://repo.typedb.com/public/public-release/deb/ubuntu trusty main" > /etc/apt/sources.list.d/vaticle.list; apt update -y && apt install -y default-jre python3 python3-pip; python3 -m pip install requests==2.31.0 pyyaml==6.0.1
WORKDIR /typedb-sample-data
COPY docker/vaticle.gpg /etc/apt/trusted.gpg.d/vaticle.gpg
COPY docker/bootstrapper.py /typedb-sample-data
# We need the 'exec' before typedb server, or the SIGTERM from `docker stop` will not forwarded to it
CMD python3 -u bootstrapper.py && exec typedb server

# The below copies are for testing. Uncomment if re-creating the master container.
# COPY bootstrapper.yml /typedb-sample-data/__test/bootstrapper.yml
# COPY datasets /typedb-sample-data/__test

# To re-create the master container for version x.x.x:
#   `docker build  . -f docker/Dockerfile  --tag typedb-sample-data:x.x.x`
