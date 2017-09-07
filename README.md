# InstagramApiSample

# Receiving an access_token
https://api.instagram.com/oauth/authorize/?client_id=CLIENT-ID&redirect_uri=REDIRECT-URI&response_type=token&scope=public+basic_content+likes+comments

# Get the most recent media published by the owner of the access_token.
https://api.instagram.com/v1/users/self/media/recent/?access_token=ACCESS-TOKEN
