from langserve import RemoteRunnable

runnable = RemoteRunnable("http://127.0.0.1:8000/chain/")
question = "অনপমের বাবা কী করে জীবিকা নির্বাহ করতেন?"
result = runnable.invoke(question)

print(result)