# AuctoArena: E-commerce Auction Site

## Description
AuctoArena is an e-commerce auction site built using the Django framework. This project allows users to post auction listings, place bids, comment on listings, and add listings to a "watchlist."

## Live Demo
Check out the live demo of the application deployed on Heroku: [AuctoArena Live Demo](https://auction-cloud-varun-a02a5113a697.herokuapp.com/)

## Getting Started
To run this project locally, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/VarunAggarwal1998/Auction-System.git
cd Auction-System
python manage.py runserver
```

## Tech Stack
- **Backend:** Python with Django web framework
- **Frontend:** Bootstrap for responsive UI
- **Database:** SQLite3 for local development
- **Deployment:** Heroku Cloud Platform

## Features
- **User Authentication:** Users can register, log in, and log out.
- **Auction Listings:** Users can create, view, and bid on active auction listings.
- **Bidding System:** Users can place bids on items, with validation for bid amounts.
- **Comments:** Users can comment on auction listings.
- **Watchlist:** Users can add or remove listings from their personal watchlist.
- **Categories:** Listings can be categorized, and users can view listings by category.
- **Admin Interface:** Admins can manage listings, bids, and comments through Django's admin panel.

## Specifications
The application includes several key features:

- **Models:** Separate models for auction listings, bids, and comments.
- **Create Listing:** Users can create new listings with titles, descriptions, starting bids, optional images, and categories.
- **Active Listings Page:** A default route to view all active listings with essential details.
- **Listing Page:** Detailed page for each listing, including bidding and commenting functionalities.
- **Watchlist:** A feature for users to maintain a list of favorite listings.
- **Categories:** Functionality to categorize listings and filter by categories.
- **Django Admin Interface:** An interface for site administrators to manage the site's content.

## Deployment
The project is deployed on Heroku, a cloud platform service. The deployment process involves setting up a Heroku app, configuring the environment, and deploying the code from the GitHub repository.

## Local Development
For local development, the project uses SQLite3 as the database. The Django development server can be used to run the application locally.

## Future Enhancements
- Implementing advanced bidding features.
- Enhancing the user interface and user experience.
- Adding payment gateway integration for auction settlements.


## Acknowledgments
- Django Documentation
- Bootstrap Framework
- Heroku Deployment Guides
