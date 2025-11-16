import os
import requests
from dotenv import load_dotenv
import logging

from internal.utils.sllm import SLLM_API_URL

load_dotenv()
logger = logging.getLogger(__name__)

LLM_API_URL = os.getenv("SLLM_API_URL")


url = LLM_API_URL + "/api/v1/chat2"
title_url = LLM_API_URL + "/api/v1/title"
title_url2 = LLM_API_URL + "/api/v1/title2"
suggest_url = LLM_API_URL + "/api/v1/suggest"


headers = {"Content-Type": "application/json"}


def run_llm(user_input, config_id, image=None, chat_history=None):

    data = {"user_input": user_input, "config_id": config_id, "image": image, "chat_history": chat_history}

    response = requests.post(url, headers=headers, json=data)
    res = response.json()

    answer = res['response']

    return answer


def title_llm(draft_title):

    data = {"first_content": draft_title}

    response = requests.post(title_url, headers=headers, json=data)
    res = response.json()

    title = res['title']

    return title


def title_llm2(draft_title, transcript):
    data = {"draft_title": draft_title, "transcript": transcript}

    response = requests.post(title_url2, headers=headers, json=data)
    res = response.json()

    title = res['title']

    return title


def suggest_llm(user_message, response, k: 5):
    data = {"user_q": user_message, "answer": response, "k": k}
    response = requests.post(suggest_url, headers=headers, json=data)
    res = response.json()

    suggestions = res['suggestions']
    return suggestions