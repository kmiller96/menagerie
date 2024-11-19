FROM docker:dind

# Install python
RUN apk update && apk upgrade
RUN apk add python3 

# Add script
WORKDIR /app
COPY script.py script.py
CMD ["python", "script.py"]