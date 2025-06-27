FROM python:3.14.0a3-bookworm
ADD app /swtich-router-parser/app/
ADD requirements.txt /swtich-router-parser/
ADD run.py /swtich-router-parser/
WORKDIR /swtich-router-parser
RUN pip install -r requirements.txt

EXPOSE 8008

CMD ["python3", "run.py"]


