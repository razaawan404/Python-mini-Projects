import requests
import urllib
import re


url = "https://books.toscrape.com/"

def main():


    response = requests.get(url)

    if response != "":

        extracting_links(response.text)
        extracting_emails(response.text)
        extracting_forms(response.text)

    else:

        print("No Response")

def extracting_links(response):

    print("[Links]")

    links = re.findall(r'href="([^"]+)"', response)

    if response == "":

        print("(none found)")


    if len(links) == 0:

        print("(none found)")


    for link in links:
    
        print(link)

    print()

def extracting_emails(response):

    print()
    print("[Emails]")


    if response == "":

        print("(none found)")

    emails = re.findall(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}', response)

    if len(emails) == 0:

        print("(none found)")


    for email in emails:

        print(email)

    print()

def extracting_forms(response):

    print("[Forms]")

    if response == "":

        print("(none found)")

    

    print()

main()