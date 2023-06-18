# Tweet Operator Documentation

## Summary
The "Tweet" operator is used to send a tweet to a specified Twitter account with a message and URL.

## Inputs
- "tweet_text": the text to be tweeted.

## Parameters
None

## Outputs
- "tweet_status": the status of the tweet (success or failure)

## Functionality
The `run_step` function takes in the `tweet_text` input and uses the `set_twitter_keys_and_secrets` function to authenticate with the Twitter API. If the tweet_text is too long, trailing hashtags are removed using the `trim_trailing_hashtags` helper function. The tweet is then sent using the `send_tweet` function and the `tweet_status` output is set. Additionally, the tweeted URL is stored in memory using the `memory_add_to_list` function.