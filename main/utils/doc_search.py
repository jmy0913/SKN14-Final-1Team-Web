import os
import requests
from dotenv import load_dotenv
import logging

from internal.utils.sllm import SLLM_API_URL

load_dotenv()
logger = logging.getLogger(__name__)

LLM_API_URL = os.getenv("SLLM_API_URL")


query_url = LLM_API_URL + "/api/v1/query"


headers = {"Content-Type": "application/json"}


def query_search(q, k:5):
    data = {"q": q, "k": k}
    response = requests.post(query_url, headers=headers, json=data)
    res = response.json()

    rows = res['rows']
    return rows