#-*- coding: utf-8 -*-
import urllib.parse
import requests
import webbrowser
import socket
import json


auth_code = ""
print("###################################")
print("OAuth 2.0 for Mobile & Desktop Apps")
print("###################################")
# https://developers.google.com/identity/protocols/oauth2/native-app

print("\nStep 1.- Prerequisites on Google Cloud Console")
print("\tEnable APIs for your project")
print("\tIdentify access scopes")
print("\tCreate authorization credentials")
print("\tConfigure OAuth consent screen")
print("\t\tAdd access scopes and test users")

client_id = "103321140724-cbn5tvbn3ttbh683aaeslumm7b9kr7sa.apps.googleusercontent.com"
client_secret = "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"
scope = "https://www.googleapis.com/auth/calendar.readonly"

redirect_uri = "http://127.0.0.1:8090"

print("# Step 2: Send a request to Google's OAuth 2.0 server")
uri = "https://accounts.google.com/o/oauth2/v2/auth"
datos = { 'client_id': client_id,
          'redirect_uri': redirect_uri,
          'response_type': 'code',
          'scope': scope}
datos_encoded = urllib.parse.urlencode(datos)

print("\tOpenning browser...")
webbrowser.open_new ((uri +'?' + datos_encoded))

print("# Step 3: Google prompts user for consent")



