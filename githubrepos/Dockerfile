FROM python
WORKDIR app
COPY *.py requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT python github_repos.py