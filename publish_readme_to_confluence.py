from atlassian import Confluence
import os

# Fetch environment variables
api_token = os.environ['CONFLUENCE_API_TOKEN']
base_url = os.environ['CONFLUENCE_BASE_URL']

# Initialize Confluence API client
confluence = Confluence(url=base_url, username='vaishnavvsri', password=api_token)

# Fetch README content from file
with open('README.md', 'r') as readme_file:
    readme_content = readme_file.read()

# Publish README to Confluence
page_title = 'My README Page'
space_key = '~62b4ef640c77011bdfde15dd'

page = confluence.create_page(space=space_key, title=page_title, body=readme_content)
print(f'Successfully published README to Confluence. Page ID: {page["id"]}')
