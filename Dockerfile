FROM python:latest

RUN mkdir /app
COPY stablediffusionqrcode /app
COPY pyproject.toml /app
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN pip3 install xformers

RUN chmod +x stable_diffuse.py
# RUN apt-get install libzbar-dev
#RUN python stable_diffuse.py --qr_source="www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=sami-alashabi"

ENTRYPOINT ["tail", "-f", "/dev/null"]
