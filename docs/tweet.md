# Tweet Class

The **Tweet** class is a custom operator for managing tweets. It is responsible for sending a tweet containing the given text and a URL. The class uses the Tweepy library to interact with the Twitter API.

## Parameters

There are no parameters for the **Tweet** class.

## Inputs

- **tweet_text** (string): Input text to be tweeted. Placeholder: "Enter the text to tweet".

## Outputs

- **tweet_status** (string): Output string containing the status of the tweet, whether it was successful or there was an error.

## Method Overview

### set_twitter_keys_and_secrets

This helper method sets the required API keys and secrets for connecting to the Twitter API using Tweepy. The keys and secrets are stored in the AI Context.

### run_step

This is the main method that runs the current step of the operator. It gets the input tweet_text and the ingested URL from the AI Context. It then sets the API keys and secrets using `set_twitter_keys_and_secrets`. After that, it calls the `send_tweet` method to send the tweet containing the text and the URL. The method also stores the tweeted URL in the memory.

### trim_trailing_hashtags

This helper method trims the trailing hashtags from the input text, if the combined length of the text and URL exceeds the maximum limit of 280 characters for a tweet.

### send_tweet

The method creates a Tweepy client with the API keys and secrets. It calls the `trim_trailing_hashtags` method to ensure the text's length is within the limit. Then, it formats the tweet by concatenating the text and URL. After validating the final text, it sends the tweet using `create_tweet` from the Tweepy library. It then returns the output status, either a success message (with the tweet URL) or an error message.