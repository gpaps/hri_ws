import sys
import requests

# Input data acquisition
CB_HEADER = {'Content-Type': 'application/json'}
selection_port = '2620'
selection_address = '25.28.181.178'  # custom_hamachi IP
selection_port_CB = '1026'
selection_address_CB = '25.45.111.204'

# subscription
msg_FORTH_HRI = "{" \
      "    \"description\": \"FORTH-U20a\",\n" \
      "    \"subject\": {\n" \
      "        \"entities\":\n" \
      "        [{\n" \
      "            \"idPattern\": \"forth.hri.*\",\n" \
      "            \"typePattern\": \".*\"\n" \
      "        }],\n" \
      "        \"conditions\": {\n" \
      "            \"attrs\": []\n" \
      "        }\n" \
      "    },\n" \
      "    \"notification\": {\n" \
      "        \"http\": {\n" \
      "            \"url\": \"http://25.28.181.178:2620/\",\n" \
      "            \"method\": \"POST\",\n" \
      "            \"headers\": {\n" \
      "                \"Content-Type\": \"application/json\"\n" \
      "            }\n" \
      "        }\n" \
      "    }\n}"

# subscription
msg_FORTH_ScenePerception = "{" \
       "    \"description\": \"FORTH-U20b\",\n" \
       "    \"subject\": {\n" \
       "        \"entities\":\n" \
       "        [{\n" \
       "            \"idPattern\": \"FORTH.ScenePerception.*\",\n" \
       "            \"typePattern\": \".*\"\n" \
       "        }],\n" \
       "        \"conditions\": {\n" \
       "            \"attrs\": []\n" \
       "        }\n" \
       "    },\n" \
       "    \"notification\": {\n" \
       "        \"http\": {\n" \
       "            \"url\": \"http://25.28.181.178:2620/\",\n" \
       "            \"method\": \"POST\",\n" \
       "            \"headers\": {\n" \
       "                \"Content-Type\": \"application/json\"\n" \
       "            }\n" \
       "        }\n" \
       "    }\n}"

# subscription
msg_FHOE = "{" \
       "    \"description\": \"FORTH-U20c\",\n" \
       "    \"subject\": {\n" \
       "        \"entities\":\n" \
       "        [{\n" \
       "            \"idPattern\": \"FHOOE.Orchestrator.*\",\n" \
       "            \"typePattern\": \".*\"\n" \
       "        }],\n" \
       "        \"conditions\": {\n" \
       "            \"attrs\": []\n" \
       "        }\n" \
       "    },\n" \
       "    \"notification\": {\n" \
       "        \"http\": {\n" \
       "            \"url\": \"http://25.28.181.178:2620/\",\n" \
       "            \"method\": \"POST\",\n" \
       "            \"headers\": {\n" \
       "                \"Content-Type\": \"application/json\"\n" \
       "            }\n" \
       "        }\n" \
       "    }\n}"

CB_BASE_URL = "http://{}:{}/v2/".format(selection_address_CB, selection_port_CB)  # url send notification

# Log("INFO", "Send subcription")
# Log("INFO", msg)

#
#
# This is to subscribe. It is performed ONLY ONCE for each subscription.
#
#

# FORTH HRI
response = requests.post(CB_BASE_URL + "subscriptions/", data=msg_FORTH_HRI, headers=CB_HEADER)  # send request to Context Broker
if response.ok:  # positive response, notification accepted
    print("CB response -> status " + response.status_code.__str__())
else:  # error response
    print("CB response -> " + response.text)

# Forth_ScenePerception
response1 = requests.post(CB_BASE_URL + "subscriptions/", data=msg_FORTH_ScenePerception, headers=CB_HEADER)
if response1.ok:  # positive response, notification accepted
    print("CB response1 -> status " + response1.status_code.__str__())
else:  # error response
    print("CB response1 -> " + response1.text)

# FHOE
response2 = requests.post(CB_BASE_URL + "subscriptions/", data=msg_FHOE, headers=CB_HEADER)
if response2.ok:  # positive response, notification accepted
    print("CB response1 -> status " + response2.status_code.__str__())
else:  # error response
    print("CB response1 -> " + response2.text)
