
# FastAPI + MongoDB API Setup Guide

This guide walks you through setting up a FastAPI API with MongoDB on Ubuntu 22.04, using a conda environment and PDM for Python dependency management.

## Prerequisites
- Ubuntu 22.04
- Conda (Miniconda or Anaconda)
- Git

## 1. Clone the Repository
```bash
git clone <your-repo-url>
cd personal-project
```

## 2. Create and Activate Conda Environment
```bash
conda env create -f environment.yml
conda activate fastapi-env
```

## 3. Install PDM in Conda Environment
```bash
pip install pdm
```


## 4. Initialize PDM and Install Dependencies
```bash
pdm init -n
pdm add fastapi uvicorn motor pydantic
```

### Using requirements.txt with PDM
PDM can export dependencies to a `requirements.txt` file for compatibility with other tools:
```bash
pdm export -o requirements.txt --without-hashes
```
If you update dependencies with PDM, remember to also update `requirements.txt` using the above command.

## 5. Install MongoDB Client (Shell) on Ubuntu 22.04
Follow the official MongoDB installation guide:
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/

Quick steps:
```bash
wget -qO - https://pgp.mongodb.com/server-6.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org-shell
```

## 6. (Optional) Install MongoDB Server
```bash
sudo apt-get install -y mongodb-org
sudo systemctl start mongod
sudo systemctl enable mongod
sudo systemctl status mongod
```

## 7. Configure Environment Variables
Edit `.env` or set environment variables for MongoDB connection, e.g.:
```
MONGO_URL=mongodb://localhost:27017
```

## 8. Start the FastAPI Application
Use PDM script:
```bash
pdm run start
```
Or directly:
```bash
uvicorn app.main:app --reload
```

## 9. API Usage
- Open Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Test CRUD endpoints for `/items`.

## 10. Project Structure
```
app/
	main.py
	api/
		item.py
	models/
		item.py
	db/
		base.py
	core/
		config.py
tests/
environment.yml
pyproject.toml
README.md
.gitignore
```

## 11. Troubleshooting
- If MongoDB is not running, start it: `sudo systemctl start mongod`
- Check MongoDB status: `sudo systemctl status mongod`
- If you get connection errors, verify your `MONGO_URL` and MongoDB server status.

## 12. Additional Notes
- All dependencies are managed via conda and PDM; no `.venv` is used.
- For development, use the conda environment (`fastapi-env`) for all commands.

---
For more details, see the official documentation:
- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/docs/manual/)
- [PDM](https://pdm-project.org/)
