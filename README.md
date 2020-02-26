### A sample Rasa bot that showcases messaging types on the Machaao Platform.<br>


**Setting up locally:**<br>

1. Apply for an api token from the machaao team and place it in the credential.yml file<br>

2. Download ngrok at [https://ngrok.com/download](https://ngrok.com/download), and place it in the project directory.<br>

3. Run ngrok on port 5005 with the following command, and note the generated https url.<br>

```
	ngrok http 5005
```

4. Start your action server either in a separate terminal or in the same tab as a background process.<br>

In a separate terminal:<br>
```
	rasa run actions
```

As a background process: <br>
```
	rasa run actions &
```
<br>

5. Start rasa core and specify the custom connector.<br>
```
	rasa run -m models --enable-api --cors “*” --connector MachaaoConnector.MachaaoInputChannel
```
<br>

6. Configure your webhook to Machaao with a simple curl command.<br>
&lt;YOUR API-TOKEN> can be requested from the Machaao team<br>
&lt;YOUR URL> can be found from ngrok in step 2<br>

```
	curl --location --request POST 'https://ganglia-dev.machaao.com/v1/bots/<YOUR API-TOKEN> \
	--header 'api_token: <YOUR API-TOKEN>' \
	--header 'Content-Type: application/json' \
	--data-raw '{
		"url": "<YOUR URL>/webhooks/rest/webhook",
		"description": "<YOUR BOT DESCRIPTION>",
		"displayName": "<YOUR BOT NAME>"
	}'
```

**Deploying your bot on a Heroku server:**<br>

1. Apply for an api token from the machaao team and place it in the credential.yml file<br>

2. Sign up for free on Heroku.<br>

3. Create a new app on Heroku and note down the app name.<br>

4. Create a docker image for this project.<br>
```
	docker build -t herokurasa .
```
<br>

5. Push and deploy the docker image to Heroku.<br>
```
	heroku container:push web -a <Your App Name>
	heroku container:push release -a <Your App Name>
```
<br>
6. Configure your Webhook to Machaao with a simple curl command.<br>
&lt;YOUR API-TOKEN> can be requested from the Machaao team<br>
&lt;YOUR URL> is generally a link that looks like &lt;Your App Name>.herokuapp.com<br>

```
	curl --location --request POST 'https://ganglia-dev.machaao.com/v1/bots/<YOUR API-TOKEN> \
	--header 'api_token: <YOUR API-TOKEN>' \
	--header 'Content-Type: application/json' \
	--data-raw '{
		"url": "<YOUR URL>/webhooks/rest/webhook",
		"description": "<YOUR BOT DESCRIPTION>",
		"displayName": "<YOUR BOT NAME>"
	}'
```
