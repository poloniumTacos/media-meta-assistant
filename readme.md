# Plex Meta Assistant

Plex Meta Assistant is a Python script designed to search for and download posters for movies and TV shows based on their names and release years. It utilizes the TMDb (The Movie Database) API to search for media information and obtain poster URLs. Tries to keep the poster name friendly so plex can read it properly.

## Features

- Search and download posters for both movies and TV shows.
- Automatic filtering based on release year.
- Detailed logging for debugging purposes.

## Requirements

- Both movies and TV shows need to have the release year in the folder name.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/poloniumTacos/plex-meta-assistant.git
```

2. Navigate to the cloned directory:

```bash
cd plex-meta-assistant
```

3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Configuration

Before using Plex Meta Assistant, you need to rename `config_example.json` to `config.json` and provide your TMDb API key in a `config.json` file. Follow these steps:

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

2. Run the Plex Meta Assistant script by executing the following command:

```bash
python poster_grabber.py
```

3. The script will search for posters for each movie and TV show in the specified directories and download them if found.

## Logging

The script logs detailed information about its operations to a `debug.log` file in the current directory. You can adjust the logging level in the `config.json` file.

---

Feel free to customize this README to fit your specific requirements or add any additional information as needed.

# plex-meta-assistant
