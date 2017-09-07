import requests
import urllib

APP_ACCESS_TOKEN = '27390842.7b94363.eff319e8edc6461f88668480c04bc712'
BASE_URL = 'https://api.instagram.com/v1/'

def get_user_id(insta_username):
	request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
	print 'GET request_url : %s' % (request_url)
	user_info = requests.get(request_url).json()
	
	if user_info['meta']['code'] == 200:
		if len(user_info['data']):
			return user_info['data'][0]['id']
		else:
			return None
	else:
		print 'Status code other than 200 received!'
		exit()

id_var = get_user_id('pusongkranz')
print(id_var)

def get_own_post():
	request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') %(APP_ACCESS_TOKEN)
	print 'Requesting data from: %s' %(request_url)
	recent_post = requests.get(request_url).json()
	
	if recent_post['meta']['code'] -- 200:
		if len(recent_post['data']) > 0:
			#return recent_post['data'][0]['id']
			image_name = recent_post['data'][0]['id'] + ".jpg"
			image_url = recent_post['data'][0]['images']['standard_resolution']['url']
			caption = recent_post['data'][0]['caption']['text']

			print(image_url)
			print 'Caption: %s' %(caption)
			urllib.urlretrieve(image_url,image_name)
		else:
			print "No posts to show"
	else:
		print "Error"
			
	return None

get_own_post()

def get_users_post(username):
	user_id = get_user_id(username)
	
	request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') %(user_id, APP_ACCESS_TOKEN)
	print 'Request URL: %s' %(request_url)

	recent_post = requests.get(request_url).json()

	if recent_post['meta']['code'] -- 200:
		if len(recent_post['data']) > 0:
			return recent_post['data'][0]['id']
		else:
			print "No posts to show"
	else:
		print "Error: not 200"

	return None

print(get_users_post('pusongkranz'))

def get_hastag_post(hashtag):
	request_url = (BASE_URL + 'tags/%s/media/recent/?access_token=%s') %(hashtag, APP_ACCESS_TOKEN)
	print 'Requesting data from: %s' %(request_url)
	recent_post = requests.get(request_url).json()
	
	if recent_post['meta']['code'] -- 200:
		if len(recent_post['data']) > 0:
			#return recent_post['data'][0]['id']
			image_name = recent_post['data'][0]['id'] + ".jpg"
			image_url = recent_post['data'][0]['images']['standard_resolution']['url']
			caption = recent_post['data'][0]['caption']['text']

			print(image_url)
			print 'Caption: %s' %(caption)
			urllib.urlretrieve(image_url,image_name)
		else:
			print "No posts to show"
	else:
		print "Error"
			
	return None

print(get_hastag_post('coffee'))