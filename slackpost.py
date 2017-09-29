from slackclient import SlackClient

slack_token = ""
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="#scripting",
  print(users.info)
  text="Spyderbot Lives! :tada:"
)
