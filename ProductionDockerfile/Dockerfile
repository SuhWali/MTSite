# Use an official Python runtime based on Debian bookworm as a parent image
FROM python:3.12-slim-bookworm

# Add user that will be used in the container
RUN useradd -ms /bin/bash wagtail

# Set environment variables
# - Force Python stdout and stderr streams to be unbuffered
# - Set PORT variable for Gunicorn
# - Disable pip's cache to reduce image size
ENV PYTHONUNBUFFERED=1 \
    PORT=8000 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install system dependencies required by Wagtail, Django, and image processing
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    libssl-dev \
    # For Wand/ImageMagick
    libmagickwand-dev \
    # For OpenCV
    libgl1 \
    # Cleanup to reduce image size
    && rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /app

# Install the application server
RUN pip install "gunicorn==20.1.0"

# Copy requirements file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the source code of the project into the container
COPY --chown=wagtail:wagtail . /app/

# Create media and static directories with proper ownership
RUN mkdir -p /app/media /app/static \
    && chown -R wagtail:wagtail /app

# Use user "wagtail" to run the build commands and the server itself
USER wagtail

# Collect static files
RUN python manage.py collectstatic --noinput --clear

# Set up entrypoint script
COPY --chown=wagtail:wagtail docker-entrypoint.sh /usr/local/bin/
USER root
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
USER wagtail

# Expose the port the app runs on
EXPOSE 8000

# Use the entrypoint script to run commands
ENTRYPOINT ["docker-entrypoint.sh"]

# Start Gunicorn with appropriate settings for production
CMD ["gunicorn", "MTSites.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]