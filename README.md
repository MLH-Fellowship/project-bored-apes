# Bored Apes Portfolio - MLH Fellowship Orientation Hackathon

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
[![GitHub contributors](https://badgen.net/github/contributors/MLH-Fellowship/project-bored-apes)](https://github.com/MLH-Fellowship/project-bored-apes/graphs/contributors)


<p align="center">
  <img src="https://storage.googleapis.com/justinmonteza/logo.png" alt="Material Bread logo">
</p>

Portfolio inspired by Bored Apes, unique digital collectibles living on the Ethereum blockchain 

## Screenshot

![Bored Apes Logo](https://storage.googleapis.com/justinmonteza/Screen%20Shot%202022-06-06%20at%2011.11.51%20AM.png)

## Tasks

Once you've got your portfolio downloaded and running using the instructions below, you should attempt to complete the following tasks.

For each of these tasks, you should create an [Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) and work on them in a new [branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches). When the task has been completed, you should open a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) and get another fellow in your pod to give you feedback before merging it in.

*Note: Make sure to include a link to the Issue you're working on inside of your Pull Request so your reviewer knows what you're working on!*

### GitHub Tasks
- [x] Create Issues for each task below
- [x] Work on each task in a new branch
- [x] Open a Pull Request when a task is finished to get feedback

### Portfolio Tasks
- [x] Add a photo of yourself to the website
- [x] Add an "About youself" section to the website.
- [x] Add your previous work experiences
- [x] Add your hobbies (including images)
- [x] Add your current/previous education
- [x] Add a map of all the cool locations/countries you visited

### Flask Tasks
- [x] Get your Flask app running locally on your machine using the instructions below.
- [x] Add a template for adding multiple work experiences/education/hobbies using [Jinja](https://jinja.palletsprojects.com/en/3.0.x/api/#basics)
- [x] Create a new page to display hobbies.
- [x] Add a menu bar that dynamically displays other pages in the app


## Getting Started

You don't need to submit any pull requests to this repository. You need to do all your work here.

## Prerequisites
- Flask
- Google Maps API
- Gmail API

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using venv

**Bash**
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

**CMD**
```cmd
> python -m venv python3-virtualenv
> python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Tech Stack
Python, HTML, CSS, JavaScript, JSON, Gmail API, Google Maps API, jQuery, Flask, Bulma

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server

**Bash**
```bash
$ export FLASK_ENV=development
$ export FLASK_DEBUG=1
$ flask run
```

**CMD**
```cmd
> set FLASK_ENV=development
> set FLASK_DEBUG=1
> flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal. We'll go through how to host it in the cloud in the next few weeks!* 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

Please see [CONTRIBUTING.md](./CONTRIBUTING.md).

## Roadmap
- Integrate database
- Add a blogging feature
- Host it on the cloud
- Add automated tests

## License

Bored Apes Portfolio is [MIT licensed](./LICENSE).

## Authors
Justin Monteza [@jmonteza](https://github.com/jmonteza) 

Logan Hoogendijk [@LoganHoogendijk](https://github.com/LoganHoogendijk) 

Hadi Chaaban [@HadiCya](https://github.com/HadiCya) 

