1. Create a virtual environment and activate it
2. pip install -r requirements.txt
3. set your project id and location in my_first_agent/.env
4. Authenticate to Gcloud and set the project
gcloud auth login --update-adc
gcloud config set project <you-project-id>
5. From cloud_api_registry folder run "adk web"
