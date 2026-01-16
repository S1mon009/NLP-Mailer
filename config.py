# Gmail API Configuration
GMAIL_CREDENTIALS_FILE = 'credentials.json'
GMAIL_TOKEN_FILE = 'token.json'
GMAIL_SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

# Model Configuration
MODEL_PATH = 'email_model.pkl'
MIN_CONFIDENCE = 0.6

# Categories
CATEGORIES = [
    'Work',
    'Personal', 
    'Finance',
    'Shopping',
    'Social',
    'Promotions',
    'Spam',
    'Newsletters'
]

# Label Colors (for Gmail)
LABEL_COLORS = {
    'Work': {'backgroundColor': '#4986e7', 'textColor': '#ffffff'},
    'Personal': {'backgroundColor': '#16a765', 'textColor': '#ffffff'},
    'Finance': {'backgroundColor': '#f691b2', 'textColor': '#ffffff'},
    'Shopping': {'backgroundColor': '#fad165', 'textColor': '#000000'},
    'Social': {'backgroundColor': '#9fc6e7', 'textColor': '#000000'},
    'Promotions': {'backgroundColor': '#ff7537', 'textColor': '#ffffff'},
    'Spam': {'backgroundColor': '#ac2b16', 'textColor': '#ffffff'},
    'Newsletters': {'backgroundColor': '#cabdbf', 'textColor': '#000000'},
}

# Training Data
TRAINING_DATA = [
    {'subject': 'Meeting at 3pm', 'body': 'Team sync discussion', 'category': 'Work'},
    {'subject': 'Project deadline', 'body': 'Task completion milestone', 'category': 'Work'},
    {'subject': 'Quarterly review', 'body': 'Performance results', 'category': 'Work'},
    {'subject': 'Invoice ready', 'body': 'Payment due amount', 'category': 'Finance'},
    {'subject': 'Bank statement', 'body': 'Monthly statement account', 'category': 'Finance'},
    {'subject': 'Credit card bill', 'body': 'Balance payment', 'category': 'Finance'},
    {'subject': '50% off sale', 'body': 'Limited offer discount', 'category': 'Promotions'},
    {'subject': 'Member discount', 'body': 'Special offer coupon', 'category': 'Promotions'},
    {'subject': 'Flash sale', 'body': 'Hurry limited time', 'category': 'Promotions'},
    {'subject': 'Long time no see', 'body': 'Catch up coffee', 'category': 'Personal'},
    {'subject': 'Birthday party', 'body': 'Please join celebrate', 'category': 'Personal'},
    {'subject': 'Dinner plans', 'body': 'Meet restaurant tonight', 'category': 'Personal'},
    {'subject': 'Order shipped', 'body': 'Package tracking delivery', 'category': 'Shopping'},
    {'subject': 'Order confirmation', 'body': 'Purchase receipt items', 'category': 'Shopping'},
    {'subject': 'Return processed', 'body': 'Refund shipping label', 'category': 'Shopping'},
    {'subject': 'New followers', 'body': 'Social media notifications', 'category': 'Social'},
    {'subject': 'Friend request', 'body': 'Connection network profile', 'category': 'Social'},
    {'subject': 'Tagged in photo', 'body': 'Check picture post', 'category': 'Social'},
    {'subject': 'Weekly newsletter', 'body': 'Latest news articles', 'category': 'Newsletters'},
    {'subject': 'Daily digest', 'body': 'Summary today stories', 'category': 'Newsletters'},
    {'subject': 'Monthly roundup', 'body': 'Best articles month', 'category': 'Newsletters'},
    {'subject': 'Winner!!!', 'body': 'Click prize urgent', 'category': 'Spam'},
    {'subject': 'Make money fast', 'body': 'Work home easy', 'category': 'Spam'},
    {'subject': 'Account verification', 'body': 'Verify suspended click', 'category': 'Spam'},
]