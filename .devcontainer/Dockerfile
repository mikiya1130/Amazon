FROM python:3.8.5

ENV TZ Asia/Tokyo

RUN apt-get update && \
    apt-get -y install --no-install-recommends libgl1-mesa-dev

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp
