#!/usr/bin/env python3
import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print:
    - The HTTP status code
    - The title of each post
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print response status code
    print(f"Status Code: {response.status_code}")

    # If request successful, parse JSON and print post titles
    if response.status_code == 200:
        posts = response.json()  # Convert JSON to Python list/dicts
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch all posts and save the id, title, and body fields
    into a CSV file called posts.csv
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # If request successful, save data into CSV file
    if response.status_code == 200:
        posts = response.json()

        # Convert each post into a simplified dictionary
        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        # Write CSV file
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_posts)

