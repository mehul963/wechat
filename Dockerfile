# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /config

# Copy the requirements.txt file to the container
COPY requirement.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy the Django project code to the container
COPY . .

# Expose the desired port (e.g., 8000)
EXPOSE 8000

# Set the entry point for the container (e.g., the Django development server)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
