From python:3.9.6-buster

ENV APP_HOME=/opt/app
WORKDIR $APP_HOME

RUN apt-get update && \
    apt-get install -y \
        python3-opencv

RUN python -m pip install --upgrade pip && \
    pip install \
        argparse \
        opencv-python

COPY . .

# ENTRYPOINT ["bash"]

ENTRYPOINT ["/usr/local/bin/python","detect.py", "--image"]
CMD ["man1.jpg"]
