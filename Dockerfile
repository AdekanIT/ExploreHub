FROM python:latest

COPY . /ExploreHub

WORKDIR . ExploreHub

RUN pip install -r req.txt

CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=7887"]