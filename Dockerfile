# Use the official Python 3.12 image
FROM python:3.12

# Set the working directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ghostscript \
    libpq-dev \
    gcc \
    && apt-get clean

# Upgrade pip
RUN pip install --upgrade pip

# Copy the application code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create the required media upload directory
# RUN mkdir -p /usr/src/app/media/uploads /usr/src/app/static

# Collect static files (use a temporary default database to avoid issues)
# RUN python manage.py collectstatic --noinput --settings=mcc.settings

# Expose the application port
EXPOSE 8000

# Run the application server using gunicorn
CMD ["gunicorn", "kct_portal.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]