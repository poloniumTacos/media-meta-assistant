Sure, here's a README file for your poster-grabber:

---

# Poster Grabber

Poster Grabber is a Python script designed to search for and download posters for movies and TV shows based on their names and release years. It utilizes the TMDb (The Movie Database) API to search for media information and obtain poster URLs.

## Features

- Search and download posters for both movies and TV shows.
- Automatic filtering based on release year.
- Detailed logging for debugging purposes.

## Installation

1. Clone this repository to your local machine:

```bash
git clone <repository_url>
```

2. Navigate to the cloned directory:

```bash
cd poster-grabber
```

3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Configuration

Before using Poster Grabber, you need to provide your TMDb API key in a `config.json` file. Follow these steps:

1. Create a TMDb account if you haven't already: [TMDb Sign Up](https://www.themoviedb.org/signup)
2. Generate an API key from your TMDb account: [TMDb API Documentation](https://developers.themoviedb.org/3/getting-started/introduction)
3. Copy your API key and paste it into the `config.json` file under the key `"tmdb_api_key"`.
4. Optionally, you can adjust the debug level in the `config.json` file to control the verbosity of logging.

Example `config.json`:

```json
{
  "tmdb_api_key": "YOUR_API_KEY_HERE",
  "debug_level": "INFO"
}
```

## Usage

1. Ensure your media files are organized into folders with the following structure:

   ```
   |- Movies
   |  |- MovieName (ReleaseYear)
   |- TV Shows
      |- TVShowName (ReleaseYear)
   ```

2. Run the Poster Grabber script by executing the following command:

```bash
python poster_grabber.py
```

3. The script will search for posters for each movie and TV show in the specified directories and download them if found.

## Logging

The script logs detailed information about its operations to a `debug.log` file in the current directory. You can adjust the logging level in the `config.json` file.

---

Feel free to customize this README to fit your specific requirements or add any additional information as needed.
# plex-meta-assistant
