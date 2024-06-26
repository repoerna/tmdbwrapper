import vcr
from pytest import fixture
from tmdbwrapper import TV

@fixture
def tv_keys():
    # Responsible only for returning the test data
    return ['id', 'origin_country', 'poster_path', 'name',
              'overview', 'popularity', 'backdrop_path',
              'first_air_date', 'vote_count', 'vote_average']

@vcr.use_cassette('tests/vcr_cassettes/tv-popular.yml', filter_query_parameters=['api_key'])
def test_tv_popular(tv_keys):
    """Tests an API call to get a popular tv shows"""

    response = TV.popular()

    assert isinstance(response, dict)
    assert isinstance(response['results'], list)
    assert isinstance(response['results'][0], dict)
    assert set(tv_keys).issubset(response['results'][0].keys())

@vcr.use_cassette('tests/vcr_cassettes/tv-popular-param.yml', filter_query_parameters=['api_key'])
def test_tv_popular_param(tv_keys):
    """Tests an API call to get a popular tv shows"""

    params = {}
    params['language'] = 'id'

    response = TV.popular(params)

    assert isinstance(response, dict)
    assert isinstance(response['results'], list)
    assert isinstance(response['results'][0], dict)
    assert set(tv_keys).issubset(response['results'][0].keys())

@vcr.use_cassette('tests/vcr_cassettes/tv-top-rated.yml', filter_query_parameters=['api_key'])
def test_tv_top_rated(tv_keys):
    """Tests an API call to get a top rated tv shows"""

    response = TV.top_rated()

    assert isinstance(response, dict)
    assert isinstance(response['results'], list)
    assert isinstance(response['results'][0], dict)
    assert set(tv_keys).issubset(response['results'][0].keys())

@vcr.use_cassette('tests/vcr_cassettes/tv-top-rated-param.yml', filter_query_parameters=['api_key'])
def test_tv_top_rated_param(tv_keys):
    """Tests an API call to get a top rated tv shows"""

    params = {}
    params['language'] = 'id'

    response = TV.top_rated(params)

    assert isinstance(response, dict)
    assert isinstance(response['results'], list)
    assert isinstance(response['results'][0], dict)
    assert set(tv_keys).issubset(response['results'][0].keys())

@vcr.use_cassette('tests/vcr_cassettes/tv-info.yml', filter_query_parameters=['api_key'])
def test_tv_info(tv_keys):
    """Tests an API call to get a TV show's info"""

    tv_instance = TV(1396)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == 1396, "The ID should be in the response"
    assert set(tv_keys).issubset(response.keys()), "All keys should be in the response"
