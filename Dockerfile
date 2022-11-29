# 1. Base image
FROM python:3.8

# 2. install java and download chrome
RUN apt-get update && \
     apt-get install -y openjdk-11-jdk-headless

# 3. set ENV variable
ENV JAVA_HOME  /usr/lib/jvm/java-11-openjdk-amd64/

# 4. Install requirements
RUN pip3 install pyspark==3.2.1

# 5. Copy files 
COPY ./ .

#  6 Remove Dockerfile from Container
RUN rm Dockerfile
RUN rm Dockerfile.bak
