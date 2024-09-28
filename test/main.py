import requests

# Base URL of the API
base_url = "https://missingdata.pythonanywhere.com/"

# Endpoint URLs
signup_url = base_url + "/signup"
login_url = base_url + "/login"
users_url = base_url + "/users"
tweets_url = base_url + "/users/1/tweets"
followers_url = base_url + "/users/1/followers"
make_a_tweet_url = base_url + "tweet"
follow_url = base_url + "follow"


# Test data
new_user = {
    "username":"hrittwik@a.com",
	"email": "hrittwik@a.com",
	"password": "notsosecurepassword"
}


# Test Login endpoint
def test_login():
    response = requests.post(login_url, json={"email": new_user["email"], "password": new_user["password"]})
    assert response.status_code == 200
    token = response.json()
    assert "token" in response.json()  # Assuming the API returns a JWT token upon successful login
    print("Login successful")
    return token

# Test Get Users endpoint
def test_get_users():
    # Assuming the user ID of the newly signed up user is returned upon successful sign up or login
    token = test_login()
    jwt_token = token["token"]
    headers = {
        "X-JWT-Token": jwt_token,
        "Content-Type": "application/json"
    }
    response = requests.get(users_url, headers=headers)
    assert response.status_code == 200
    print("Get Users successful")
    print(response.text)

# Test Get Tweets endpoint
def test_get_tweets():
    token = test_login()
    jwt_token = token["token"]
    headers = {
        "X-JWT-Token": jwt_token,
        "Content-Type": "application/json"
    }
    response = requests.get(tweets_url, headers=headers)
    assert response.status_code == 200
    print("Get Tweets successful")
    print(response.text)

# Test Get Followers endpoint
def test_get_followers():
    token = test_login()
    jwt_token = token["token"]
    headers = {
        "X-JWT-Token": jwt_token,
        "Content-Type": "application/json"
    }

    response = requests.get(followers_url, headers=headers)
    assert response.status_code == 200
    print("Get Followers successful")


def test_make_a_tweet_live():
    token = test_login()
    jwt_token = token["token"]
    headers = {
        "X-JWT-Token": jwt_token,
        "Content-Type": "application/json"
    }

    tweet_data = {
        "content": "from testing app"
    }

    response = requests.post(make_a_tweet_url, headers=headers, json=tweet_data)

    if response.status_code == 201:
        print("Tweet successfully published!")
    print(response.json()["message"])
    #print(response.json()["tweet"])

def test_follow_user():
    token = test_login()
    jwt_token = token["token"]
    headers = {
        "X-JWT-Token": jwt_token,
        "Content-Type": "application/json"
    }

    user_id = {
        "user_id": 1
    }
    response = requests.post(follow_url, headers=headers, json=user_id)
    assert response.status_code == 200
    print(response.json()["resp"])

# Run all test functions
def run_tests():

    test_login()
    test_get_users()
    test_get_tweets()
    test_make_a_tweet_live()
    test_get_followers()
    test_follow_user()

# Run the tests
if __name__ == "__main__":
    run_tests()