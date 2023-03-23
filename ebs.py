import requests

url = 'https://twitter.com/i/api/graphql/JoSgAVrSCdidOss_It5bxg/Followers'

headers = {
    'authorization': 'Bearer YOUR_BEARER_TOKEN',
    'content-type': 'application/json',
    'x-guest-token': 'YOUR_GUEST_TOKEN',
}

data = {
    "variables": {"userId": "YOUR_USER_ID", "count": 20, "cursor": "YOUR_CURSOR", "includePromotedContent": False, "withDownvotePerspective": False, "withReactionsMetadata": False, "withReactionsPerspective": False},
    "query": "query Followers($userId: ID!, $count: Int!, $cursor: String) {\n  user(userId: $userId) {\n    followers(count: $count, cursor: $cursor) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        id\n        name\n        screenName\n        profileImageUrl\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
}

response = requests.post(url, headers=headers, json=data)

print(response.json())
