FROM python:3

ADD mac.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

ENV mac ''
ENV api_key ''

CMD python ./mac.py -m ${mac} -k ${api_key}