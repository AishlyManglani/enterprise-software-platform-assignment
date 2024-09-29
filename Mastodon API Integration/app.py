#code written by: Aishly, Sheetal, syeda nida and Amrutha


from flask import Flask, render_template, request, redirect, url_for
from mastodon import Mastodon

app = Flask(__name__)

# Initialize Mastodon API with your credentials
mastodon = Mastodon(
    access_token='L27kAX-Z-Y0jzKQyc5IZgYQYncx29ZLVJrvVqrNSLo0',  # Replace with your actual access token
    api_base_url='https://mastodon.social/'  # Replace with your Mastodon instance URL
)

# Route to create a new post
@app.route('/', methods=['GET', 'POST'])
def index():
    post_id = None
    if request.method == 'POST':
        status = request.form['status']
        new_post = mastodon.status_post(status)  # This should work now
        post_id = new_post['id']  # Capture the post ID
        return render_template('index.html', post_id=post_id)  # Pass post ID to the template
    return render_template('index.html', post_id=post_id)

# Route to retrieve a post by ID
@app.route('/retrieve', methods=['GET'])
def retrieve():
    post_id = request.args.get('post_id')  # Get post ID from the query string
    post = mastodon.status(post_id)  # Fetch the specific post using the ID
    return render_template('retrieve.html', post=post)  # Render the post in a new template

# Route to delete a post by ID
@app.route('/delete', methods=['POST'])
def delete():
    post_id = request.form['post_id']  # Get post ID from the form
    mastodon.status_delete(post_id)  # Delete the post using the ID
    return redirect(url_for('index'))  # Redirect back to the home page

if __name__ == '__main__':
    app.run(debug=True)
