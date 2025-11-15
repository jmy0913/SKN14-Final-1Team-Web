import os
import requests
from dotenv import load_dotenv
import logging

from internal.utils.sllm import SLLM_API_URL

load_dotenv()
logger = logging.getLogger(__name__)

LLM_API_URL = os.getenv("SLLM_API_URL")


url = LLM_API_URL + "/api/v1/chat2"
headers = {"Content-Type": "application/json"}


def run_llm(user_input, config_id, image=None, chat_history=None):

    data = {"user_input": user_input, "config_id": config_id, "image": image, "chat_history": chat_history}

    response = requests.post(url, headers=headers, json=data)
    res = response.json()

    answer = res['response']

    return answer
