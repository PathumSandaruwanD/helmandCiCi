#base images
FROM python:3.11-slim

#copy app code to the container
WORKDIR /app

COPY app/ ./app/

#install dependancies
RUN pip install --no-cache-dir -r app/requirements.txt 

#expose the port 5001
EXPOSE 5001 

# Step 6: Set environment variable for Flask app
ENV FLASK_APP=app/app.py

# Step 7: Load environment variables from .env
# Use python-dotenv in app.py — no special command needed here

# Step 8: Run the app
CMD ["python", "app/app.py"]
