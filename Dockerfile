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
RUN apt-get update && apt-get install -y zbar-tools
#RUN python stable_diffuse.py --qr_source="www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=sami-alashabi"
#RUN python stable_diffuse.py --image_to_combine="https://images.adsttc.com/media/images/6267/770d/3e4b/3133/c100/006d/slideshow/takawo.jpg" --prompt="tulips, windmill, netherlands"
ENTRYPOINT [ "python","stable_diffuse.py" ]
#ENTRYPOINT ["tail", "-f", "/dev/null"]
