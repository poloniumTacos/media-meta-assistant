import os
import json
import requests
import logging
from tmdbv3api import TMDb, Movie, TV

class MediaMetaAssistant:
    def __init__(self, config_file='config.json'):
        with open(config_file, 'r') as file:
            self.config = json.load(file)
        self.tmdb = TMDb()
        self.tmdb.api_key = self.config.get('tmdb_api_key')
        self.tmdb.language = 'en'
        self.log_level = self.config.get('debug_level', 'INFO')
        logging.basicConfig(filename='debug.log', level=self.log_level)

    def get_items_with_year(self, directory, is_folder=True):
        items_with_years = []
        for item in os.listdir(directory):
            if item.startswith('.'):
                continue  # Skip files starting with "."
            year = self.extract_year_from_name(item)
            items_with_years.append((item, year))
        return items_with_years

    def extract_year_from_name(self, name):
        start_index = name.find('(') + 1
        end_index = name.find(')')
        if start_index != -1 and end_index != -1:
            year = name[start_index:end_index]
            if year.isdigit() and len(year) == 4:
                return year
        return None

    def filter_media_by_year(self, media_list, year, is_movie=True):
        filtered_media = []

        for media in media_list:
            if is_movie and hasattr(media, 'release_date') and media.release_date and media.release_date.startswith(year):
                filtered_media.append(media)
            elif not is_movie and hasattr(media, 'first_air_date') and media.first_air_date and media.first_air_date.startswith(year):
                filtered_media.append(media)

        return filtered_media

    def get_poster(self, media_name, year=None, is_movie=True):
        media_name = media_name.split('(')[0].strip()
        media_type = Movie() if is_movie else TV()
        try:
            search_results = media_type.search(media_name)
            if search_results:
                if len(search_results) == 1:
                    media_info = search_results[0]  # Get the only result
                else:
                    if year:
                        filtered_results = self.filter_media_by_year(search_results, year, is_movie)
                        if filtered_results:
                            media_info = filtered_results[0]  # Get the most relevant result
                        else:
                            logging.debug(f"No poster found for '{media_name}' in year '{year}'")
                            search_url = f"https://www.themoviedb.org/search?query={media_name}&year={year}"
                            logging.debug(f"Search URL: {search_url}")
                            return None
                    else:
                        media_info = search_results[0]  # Get the most relevant result
                
                if hasattr(media_info, 'poster_path'):
                    poster_url = "https://image.tmdb.org/t/p/original" + media_info.poster_path
                    return poster_url
                else:
                    logging.debug(f"No poster found for '{media_name}'")
                    return None
            else:
                logging.debug(f"No search results found for '{media_name}'")
                return None
        except Exception as e:
            logging.error(f"Error occurred while searching for media: {e}")
            return None

    def download_poster(self, poster_url, directory, filename="poster.jpg"):
        try:
            if not os.path.exists(directory):
                logging.debug(f"Directory '{directory}' does not exist for downloading poster '{filename}'")
                return
            
            response = requests.get(poster_url)
            if response.status_code == 200:
                with open(os.path.join(directory, filename), 'wb') as f:
                    f.write(response.content)
                    logging.debug(f"Poster downloaded for: {filename}")
            else:
                logging.error(f"Failed to download poster for: {filename}")
        except Exception as e:
            logging.error(f"Error occurred while downloading poster: {e}")

    def process_media(self, media_type, media_path, is_movie=True):
        print(f"Folders in {media_type.capitalize()} Directory:")
        items_with_years = self.get_items_with_year(media_path, is_folder=not is_movie)

        if len(items_with_years) > 0:
            for item, year in items_with_years:
                poster_url = self.get_poster(item, year, is_movie=is_movie)
                if poster_url:
                    print(f"{media_type.capitalize()}: {item}, Poster URL: {poster_url}")
                    item_directory = os.path.join(media_path, item)
                    self.download_poster(poster_url, item_directory)
                else:
                    print(f"No poster found for: {item}")
                    search_url = f"https://www.themoviedb.org/search?query={item}&year={year}"
                    print(f"Search URL: {search_url}")
        else:
            print(f"No {media_type} found in the {media_type} directory")

    def main(self):
        for media_info in self.config.get('media_paths', []):
            media_type = media_info.get('type')
            media_path = media_info.get('path')
            if media_type and media_path:
                self.process_media(media_type, media_path, is_movie=(media_type == 'movie'))
            else:
                print(f"{media_type.capitalize()} path not found in config.json")

if __name__ == "__main__":
    processor = MediaMetaAssistant()
    processor.main()
