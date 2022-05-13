# start by pulling the python image
FROM python:3.8-alpine

# copy the requirements file into the image
COPY requirements.txt /app/requirements.txt

COPY run.sh /app/run.sh

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt
RUN chmod a+x run.sh

# copy every content from the local file to the image
COPY appexample /app

# configure the container to run in an executed manner
# ENTRYPOINT [ "python" ]

CMD ["./run.sh" ]