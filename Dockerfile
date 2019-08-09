# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /curve_excercise

# Set the working directory to /curve_excercise
WORKDIR /curve_excercise

# Copy the current directory contents into the container at /curve_excercise
ADD . /curve_excercise/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

CMD ["./run_app.sh"]

EXPOSE 8080
