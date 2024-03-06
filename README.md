# Bookfinder

Third Milestone Project for the Web Development course offered by Code Institute. Currently a book recommendations site.

## Table of Contents
1. [UX](#ux)
	- [Project Goals](#project-goals)
	- [User Goals](#user-goals)
	- [User Stories](#user-stories)
	- [Design Choices](#design-choices)
2. [Planning](#planning)
	- [Wireframes](#wireframes)
3. [Future Additions](#future-additions)
4. [Testing](#testing)
	- [Bugfixes](#bugfixes)
5. [Technologies Used](#technologies-used)
6. [Deployment](#deployment)
7. [Credit](#credit)

## UX

### Project Goals

Bookfinder will be a site where users can upload book recommendations. Books will be grouped by author and by genre, making it easy to find books of a particular genre (fantasy, sci-fi, romance, comedy, non-fiction, and so on), as well as by author.

### User Goals

- Simple design.
- Visually appealing.

### User Stories

- As a user, I want a way to find books by the same author.
- As a user, I want a way to find books of the same genre.
- As a user, I want ...
- As a user, I want ...
- As a user, I want ...
- As a user, I want ...

### Design Choices

#### Interface
Overall description.

![Home page.](docs/page-display.png)

The site shifts to accommodate several screen sizes while keeping the same basic layout.

![Tablet screen, 768px wide.](docs/tablet-display.png)

On smaller screens...

![Mobile screen, 425px wide.](docs/mobile-l-display.png)

#### Colours
![Palette](docs/palette.png)
- `#000000` is used for ...
- `#000000` is used for ...
- `#000000` is used for ...
- `#000000` is used for ...
- `#000000` is used for ...

## Planning

### Wireframes
I have used MS Paint to sketch out a basic wireframe for the site:
![Wireframe](docs/wireframe.png)

## Future Additions
- ?

## Testing

<!-- The site has been tested extensively to ensure the best user experience across multiple screen sizes.

The developer used **W3C CSS Validation Service** and **W3C Markup Validation Service** to check the validity of the HTML and CSS. -->

### Testing Process

<!-- In order to make sure the site renders acceptably across several screen sizes, I made liberal use of the DevTools offered by Google Chrome, as well as testing load times, mobile and desktop, with the Lighthouse Chrome extension.

![Testing main page desktop version.](docs/lighthouse-test-desktop.png)

![Testing main page mobile version.](docs/lighthouse-test-mobile.png) -->

### User Stories Testing

As a user of the site, I want: 
- 1
	- a
	- b

### Bugfixes
- **Problem:** ...
	- **Solution:** ...

## Technologies Used

### Building
- [HTML5](https://developer.mozilla.org/en-US/docs/Learn/HTML)
- [CSS53](https://developer.mozilla.org/en-US/docs/Learn/CSS)
    - [Materialize](https://materializecss.com/)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Python](https://docs.python.org/3/)
    - [Flask](https://flask.palletsprojects.com/en/3.0.x/)
    - [SQL-Alchemy](https://docs.sqlalchemy.org/en/20/)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [psycopg2](https://www.psycopg.org/docs/) (required to work with PostgreSQL)

### Testing
- [Lighthouse](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk)

### Validation
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input)
- [W3C Markup Validation](https://validator.w3.org/#validate_by_input)

## Deployment
Deploy to GitHub Pages or a similar website hosting and rendering service. The html files can also be opened from local storage (this requires downloading all files in a dedicated folder; this can be done with the git pull command).

To deploy this site to Heroku from [its GitHub repository](https://github.com/cosmicCode42/CI-MP3), the following steps were taken.

1. Log in to Heroku.
2. 

At the moment of submitting the milestone project, the development branch and main branch are identical.

### How to run the project locally

To clone this project from GitHub:

1. Follow this link to [its GitHub repository](https://github.com/cosmicCode42/pattern-MP3).
2. Under the Code dropdown menu in the Code section, you can copy the HTTPS link or download a ZIP.
3. A copied link can be used to make a pull request using Git Bash. 
	1. Change the current working directory to one where you want the clone to be made.
	2. Run ``git init`` to initialise a local repository.
	3. Run ``git remote add origin`` and paste the copied link right after. Running this command sets the GitHub repository as the 'origin'.
	4. Run ``git branch -M main`` if the local repository doesn't have a main branch.
	5. Run ``git pull origin main`` to make the pull request.

### Cloning project into GitPod

To clone this project into GitPod, you will need:
- A [GitHub](https://github.com) account.
- A Chrome browser or compatible browser.

Then follow these steps:
1. Install the [GitPod browser extension for Chrome](https://www.gitpod.io/docs/configure/user-settings/browser-extension).
2. Restart the browser after installation.
3. Log into [GitPod](https://www.gitpod.io) with your GitHub account.
4. Navigate into the [Project GitHub repository](https://github.com/cosmicCode42/CI-MP3).
5. Click the green **GitPod** button in the top right corner of the repository. This will trigger a new GitPod workspace to be created from the code in GitHub where you can work normally.

## Credit

### Code

Code not written by me and not covered below is attributed to proper sources in comments within the code. All other code is written by me.

#### Guidance and Inspiration