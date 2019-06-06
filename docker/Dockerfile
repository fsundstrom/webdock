FROM python:2.7-alpine
ADD app /swtich-router-parser/app/
ADD requirements.txt /swtich-router-parser/
ADD run.py /swtich-router-parser/
WORKDIR /swtich-router-parser
RUN pip install -r requirements.txt

EXPOSE 8008

CMD ["./run.py"]


