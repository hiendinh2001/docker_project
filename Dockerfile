# syntax=docker/dockerfile:1 #tương thích với các version của docker


# My image inherits from the Python 3.12.1-bullseye image
FROM python:3.12.1-bullseye


#thư mục làm việc bên container
WORKDIR /app

RUN pip install PyMySQL

#host: your PC, laptop, cloud server, etc.
#Copy from host to container
COPY requirements.txt requirements.txt


#Run this command in the container
RUN pip3 install -r requirements.txt


#Copy from host to container
COPY . .

#Run this command in the container
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]