FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

# Install MongoDB CLI tools
RUN wget -qO - https://www.mongodb.org/static/pgp/server-7.0.asc | sudo apt-key add - \
	&& echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list \
	&& apt-get update \
	&& apt-get install -y mongodb-mongosh \
	&& apt-get clean -y \
	&& rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install pymongo pandas jupyter black