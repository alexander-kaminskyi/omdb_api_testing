import pytest
from rest.OmdbClient import *

omdb_client = OmdbClient()


@pytest.mark.parametrize("title_name",
                         ["The STEM Journals", "Activision: STEM - in the Videogame Industry"])
def test_omdb_rest_api(title_name, title='stem'):
    result_search = omdb_client.search(title)
    assert len(
        result_search) >= 30, f"The result search should contain at least 30 items.Actual quantity is {len(result_search)}"
    found_title = False
    for item in result_search:
        if title_name == item["Title"]:
            found_title = True
            break
    assert found_title, f"Expected title - {title_name} doesn't exist in result search - {result_search}"

    imdbid = ''
    for item in result_search:
        if "Activision: STEM - in the Videogame Industry" == item["Title"]:
            imdbid = item["imdbID"]
    movie_details = omdb_client.get_by_id(imdbid)
    release = "23 Nov 2010"
    director = "Mike Feurstein"
    assert movie_details["Released"] == release, \
        f"Expected movie release - {release} isn't equal to actual - {movie_details['Released']}"
    assert movie_details["Director"] == director, \
        f"Expected director - {director} isn't equal to actual - {movie_details['Director']}"

    title = 'The STEM Journals'
    result_search = omdb_client.get_by_title(title)
    expected_string = "Science, Technology, Engineering and Math"
    expected_run_time = "22 min"
    assert expected_string.lower() in result_search["Plot"], \
        f"Expected string - {expected_string.lower()} was not found in result search - {result_search['Plot']}"
    assert expected_run_time == result_search["Runtime"], \
        f"Expected run time - {expected_run_time} isn't equal to actual - {result_search['Runtime']}"
