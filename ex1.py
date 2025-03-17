import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# 1. Fetch data from a supermarket API (example URL)
def fetch_supermarket_data():
    url = "http://demo5644627.mockable.io/mydata"  # Replace with your supermarket API URL
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()  # Assuming the API returns JSON data
    else:
        print("Failed to fetch data.")
        return []

# 2. Create shopping cart summary
def generate_shopping_cart(products, items_to_buy):
    cart = []
    total_price = 0.0

    for product in products:
        if product['id'] in items_to_buy:
            cart.append(product)
            total_price += product['price']
    
    return cart, total_price

# 3. Prepare the email content
def create_email_content(cart, total_price):
    content = "Your Supermarket Shopping Cart Summary\n\n"
    for item in cart:
        content += f"{item['name']} - ${item['price']}\n"
    
    content += f"\nTotal Price: ${total_price:.2f}\n"
    content += f"\nThank you for shopping with us!\n"
    return content

# 4. Send the email
def send_email(subject, body, to_email):
    from_email = "nandu13123@gmail.com"  # Replace with your email
    password = "rfsh ckvo ezxb ppcd"  # Replace with your email password

    # Create MIME message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send email using SMTP
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # For Gmail (use your SMTP server if different)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

# Main program logic
def main():
    # Simulating a list of items you want to buy (by ID)
    items_to_buy = [1, 3, 5]  # Example: product IDs you want to purchase

    # Fetch data from the supermarket API
    products = fetch_supermarket_data()
    
    if not products:
        return


    cart, total_price = generate_shopping_cart(products, items_to_buy)

  
    email_content = create_email_content(cart, total_price)

    
    subject = f"Supermarket Cart Summary - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    recipient_email = "dd1347089@gmail.com"  # Replace with recipient email
    send_email(subject, email_content, recipient_email)

if __name__ == "__main__":
    main()
