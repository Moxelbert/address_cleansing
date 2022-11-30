# 1. Base image
FROM python:3.9

# 2. install java and the vi editor
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
