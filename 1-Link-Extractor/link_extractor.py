import requests
import urllib



url = "https://books.toscrape.com/"

def main():


    response = requests.get(url)

    if response != "":

        extracting_emails(response.text)
        extracting_forms(response.text)
        extracting_links(response.text)

    else:

        print("No Response")

def extracting_links(response):

    print("[Links]")

    if response == "":

        print("(none found)")

    print()

def extracting_emails(response):

    print("[Emails]")

    if response == "":

        print("(none found)")

    print()

def extracting_forms(response):

    print("[Forms]")

    if response == "":

        print("(none found)")

    print()

main()