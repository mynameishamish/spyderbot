from slackclient import SlackClient

slack_token = "xoxp-110015888069-110992073120-249898224518-c2ebe2ef2b985d2f0e28f552d75658cc"
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="#scripting",
  print(users.info)
  # text="Spyderbot Lives! :tada:"
)
