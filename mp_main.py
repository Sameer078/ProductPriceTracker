from tkinter import *
from tkinter import messagebox
import requests
import smtplib
from bs4 import BeautifulSoup


def check_internet():
    try:
        requests.get("https://google.com")

    except Exception:
        sho = Tk()
        sho.geometry("600x200")
        sho.maxsize(600,200)
        sho.minsize(600,200)
        sho.title("P.P.T.")
        Label(sho, text="PRODUCT PRICE TRACKER",
              font="comicsansms 13 bold", pady=15).place(relx=0.3, rely=0)
        Label(sho, text="Make sure you're connected to the internet!",
              font="comicsansms 13 bold", pady=15).place(relx=0.3, rely=0.4)
        img = PhotoImage(file='warn.png')
        img1 = img.subsample(4, 4)
        Label(sho, image=img1).place(height=100, width=100, relx=0.1, rely=0.3)
        sho.mainloop()
        quit()


def sendmail(product_name, URL, desired_price, price, ratings):
    '''Function called when the email needs to be sent '''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(emailvalue.get(), passwrdvalue.get())

    subject = f"Price down for {product_name}"
    body = f"The price for '{product_name}' is now {price} which is in your desired range, {desired_price}! And rating of product is {ratings}. Visit {URL} for more info."
    msg = f"Subject: {subject}\n\n{body}"
    msg1 = msg.encode()
    server.sendmail(emailvalue.get(), emailvalue.get(), msg1)
    messagebox.showinfo("SUCCESSFUL", "Mail has been Sent")
    server.quit()
    nxt1.destroy()


def amazon():
    try:
        URL = urlentry.get()
        desired_price = float(priceentry.get())
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        product_name = soup.find(id="productTitle").get_text().strip()
        price = float(soup.find("span", {"class": "a-price a-text-price a-size-medium apexPriceToPay",
                      "class": "a-offscreen"}).get_text().replace('₹', '').replace(',', ''))
        ratings = soup.find("span", {"class": "a-icon-alt"}).get_text()
        if price <= desired_price:
            sendmail(product_name, URL, desired_price, price, ratings)
        else:
            messagebox.showinfo("INFO", "Price is more than your range ")
            nxt1.destroy()

    except Exception as e:
        messagebox.showwarning("WARNING", "Please enter required details")


def flipkart():
    try:
        URL = urlentry.get()
        desired_price = float(priceentry.get())
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        product_name = soup.find(
            "span", {"class": "B_NuCI"}).get_text().strip()
        price = float(soup.find("div", {"class": "_30jeq3 _16Jk6d"}).get_text(
        ).replace(',', '').replace('₹', ''))
        ratings = soup.find('div', {"class": "_3LWZlK"}).get_text()
        if price <= desired_price:
            sendmail(product_name, URL, desired_price, price, ratings)
        else:
            messagebox.showinfo("INFO", "Price is more than your range :(")
            nxt1.destroy()

    except Exception as e:
        messagebox.showwarning("WARNING", "Enter required details")


def next2():

    nxt.destroy()
    global nxt1
    nxt1 = Tk()
    nxt1.geometry("500x250")
    nxt1.maxsize(500, 250)
    nxt1.minsize(500, 250)
    nxt1.title("AMAZON PRICE TRACKER")
    Label(nxt1, text="Please enter the product url and the desired price",
          font="comicsansms 10 italic", pady=15).place(relx=0.1, rely=0.2)
    url = Label(nxt1, text="URL")
    desired_price = Label(nxt1, text="Desired Price")
    url.place(relx=0.2, rely=0.4)
    desired_price.place(relx=0.2, rely=0.5)
    global urlentry, priceentry
    urlentry = Entry(nxt1, textvariable=urlVal)
    priceentry = Entry(nxt1, textvariable=priceVal)
    urlentry.place(relx=0.4, rely=0.4)
    priceentry.place(relx=0.4, rely=0.5)
    Button(nxt1, text="Submit", background = "gold", command=amazon).place(relx=0.7, rely=0.7)
    img = PhotoImage(file='ama.png')
    img1 = img.subsample(4, 4)
    Label(nxt1, image=img1).place(height=40, width=150, relx=0.3, rely=0.05)
    nxt1.mainloop()


def next3():
    nxt.destroy()
    global nxt1
    nxt1 = Tk()
    nxt1.geometry("500x250")
    nxt1.maxsize(500, 250)
    nxt1.minsize(500, 250)
    nxt1.title("FLIPKART PRICE TRACKER")
    Label(nxt1, text="Please enter the product url and the desired price",
          font="comicsansms 10 italic", pady=15).place(relx=0.1, rely=0.2)
    url = Label(nxt1, text="URL")
    desired_price = Label(nxt1, text="Desired Price")
    url.place(relx=0.2, rely=0.4)
    desired_price.place(relx=0.2, rely=0.5)
    global urlentry, priceentry
    urlentry = Entry(nxt1, textvariable=urlVal)
    priceentry = Entry(nxt1, textvariable=priceVal)
    urlentry.place(relx=0.4, rely=0.4)
    priceentry.place(relx=0.4, rely=0.5)
    Button(nxt1, text="Submit", background = "gold", command=flipkart).place(relx=0.7, rely=0.7)
    img = PhotoImage(file='f.png')
    img1 = img.subsample(2,2)
    Label(nxt1, image=img1).place(height=40, width=150, relx=0.3, rely=0.05)
    nxt1.mainloop()


def next1():
    if not emailentry.get():
        messagebox.showwarning("WARNING", "Please provide email id")
    elif not passwrdentry.get():
        messagebox.showwarning("WARNING", "Please provide password")
    else:
        root.destroy()

        global nxt
        nxt = Tk()
        nxt.geometry("1000x250")
        nxt.maxsize(1000, 250)
        nxt.minsize(1000, 250)
        nxt.title("PRODUCT PRICE TRACKER")
        img = PhotoImage(file='pt1.png')
        img1 = img.subsample(2,2)
        Label(nxt, image=img1).place(height=40, width=150, relx=0, rely=0.02)
        Label(nxt, text="Welcome to product price tracker!",
              font="comicsansms 13 bold", pady=15).place(relx=0.4, rely=0)
        Label(nxt, text=" A tool which you can use to track prices for a product on Amazon and Flipkart",
              font="comicsansms 13 bold", pady=15).place(relx=0.2, rely=0.2)
        Label(nxt, text=" Where to track price?",
              font="comicsansms 13 bold", pady=15).place(relx=0.2, rely=0.4)
        Radiobutton(nxt, text='Amazon',
                    variable=Sval, value=1, command=next2).place(relx=0.2, rely=0.6)
        Radiobutton(nxt, text='Flipkart',
                    variable=Sval, value=2, command=next3, tristatevalue=0).place(relx=0.2, rely=0.7)
        nxt.mainloop()


if __name__ == "__main__":
    check_internet()
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    root = Tk()
    Sval = StringVar()
    urlVal = StringVar()
    priceVal = StringVar()
    root.geometry("400x250")
    root.maxsize(400, 250)
    root.minsize(400, 250)
    root.title("P.P.T.")
    Label(root, text="PRODUCT PRICE TRACKER",
          font="comicsansms 13 bold", pady=15).place(relx=0.2, rely=0)

    email = Label(root, text="Email")
    password = Label(root, text="Password")

    email.place(relx=0.2, rely=0.3)
    password.place(relx=0.2, rely=0.4)

    emailvalue = StringVar()
    passwrdvalue = StringVar()

    emailentry = Entry(root, textvariable=emailvalue)
    passwrdentry = Entry(root, textvariable=passwrdvalue, show='*')

    emailentry.place(relx=0.4, rely=0.3)
    passwrdentry.place(relx=0.4, rely=0.4)

    Button(text="Submit", background = "gold", command=next1).place(relx=0.6, rely=0.6)
    root.mainloop()
