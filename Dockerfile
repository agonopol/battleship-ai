FROM tensorflow/tensorflow:latest-py3
ENV APP /battleship
ADD requirements.txt $APP/
RUN pip3 install -r $APP/requirements.txt
ADD . $APP
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
WORKDIR $APP