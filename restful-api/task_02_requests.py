#!/usr/bin/env python3
import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print the status code
    and the title of each post.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # If request was successful, parse and print titles
    if response.status_code == 200:
        posts = response.json()  # Parse JSON response into Python list/dict
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch all posts and save them to a CSV file called posts.csv
    containing id, title, and body.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # If request was successful, save to CSV
    if response.status_code == 200:
        posts = response.json()

        # Structure the list of dictionaries
        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        # Write to CSV using DictWriter
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_posts)
