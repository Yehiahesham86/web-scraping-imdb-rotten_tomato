import csv
from bs4 import BeautifulSoup
import requests


def main():
    page = requests.get("https://www.imdb.com/chart/top")

    src = page.content
    soup = BeautifulSoup(src, "lxml")
    movies_details = []
    movies = soup.findAll("td", {'class': 'titleColumn'})

    number_movies = len(movies)
    # print(movies,number_movies)

    # print(tournments)
    for i in range(number_movies):
        def movie_details_title(movies):
            movie_ranking = movies.contents[0].text.strip()
            movie_title = movies.contents[1].text.strip()
            movie_link = movie_title.replace(":", "").replace(" ", "_").lower()
            movie_release = movies.contents[3].text.strip()
            try:
                page1 = requests.get(f"https://www.rottentomatoes.com/m/{movie_link}")
                src1 = page1.content
                soup1 = BeautifulSoup(src1, "lxml")
                audiencescore = soup1.find("score-board")["audiencescore"]
                tomatometerscore = soup1.find("score-board")["tomatometerscore"]
                # print(audiencescore)
                # print(tomatometerscore)

            except:
                audiencescore = 0
                tomatometerscore = 0
            movies_details.append(
                {"Ranking": movie_ranking, "Title": f"{movie_title} {movie_release}", "audiencescore": audiencescore,
                 "tomatometerscore": tomatometerscore})
            # print(movie_ranking, movie_title, movie_release)

            # all_matchs = movies.contents[3].find_all("li")
            # number_match = len(all_matchs)
            # if i==0:()
            # else:(
            # print("--------------------------------------")
            # )
            # print(tournment_title)

        movie_details_title(movies[i])
    print(movies_details)

    keys = movies_details[0].keys()

    with open("C:/Users/Yehia/Desktop/movies_rates.csv", 'w', encoding='utf-8-sig') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(movies_details)
    output_file.close()


main()
