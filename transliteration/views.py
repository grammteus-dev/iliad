
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse

from .constants import transliteration_data

def index(request):
  return render(request, 'transliteration/index.html')

def chunkify(text):
  chunks = []
  chunk = ''
  count = 0
  for character in text:
    chunk += character
    if count == 3:
      chunks.append(chunk)
      chunk = ''
      count = 0
    else:
      count += 1

  if chunk:
    chunks.append(chunk)

  return chunks

def parse_greek(data):
  if 'text' not in data:
    return {
      'error': 'Incorrect request data',
    }

  text = data.get('text')

  if not text:
    return {
      'error': 'No data'
    }

  chunks = chunkify(text)

  characters = []
  for chunk in chunks:
    if len(chunk) != 4:
      return {
        'error': 'Malformed data "{}"'.format(chunk)
      }

    if chunk not in transliteration_data:
      return {
        'error': 'Character not found "{}"'.format(chunk)
      }

    characters.append(transliteration_data.get(chunk))

  return {
    'response': characters,
  }

@csrf_exempt
def greek(request):

  data = json.loads(request.body)

  parsed_data = parse_greek(data)

  response = JsonResponse(parsed_data)

  response["Access-Control-Allow-Origin"] = "http://localhost:3000"
  response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
  response["Access-Control-Max-Age"] = "1000"
  response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"

  return response
