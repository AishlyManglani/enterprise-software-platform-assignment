#code written by: syeda Nida and Amrutha

from mastodon import Mastodon

# Initialize the Mastodon client with your access token and instance URL
mastodon = Mastodon(
    client_id='rw79l1Zcmwh0k5s6ms-SyliaOSGKT_4a9FbJ-Dl5o50',
    client_secret='mz6oDXCDE1UKG7fQ3l4_EhVlcRXpwJSe2Hg0ED5gIjw',
    access_token='L27kAX-Z-Y0jzKQyc5IZgYQYncx29ZLVJrvVqrNSLo0',
    api_base_url='https://mastodon.social/'  # Replace with your instance
)

# Function to create a post
def create_post(status):
    post = mastodon.status_post(status)
    return post

# Function to retrieve a post by its ID
def retrieve_post(post_id):
    post = mastodon.status(post_id)
    return post

# Function to delete a post by its ID
def delete_post(post_id):
    mastodon.status_delete(post_id)
