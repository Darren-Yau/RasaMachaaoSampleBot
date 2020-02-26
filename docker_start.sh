# Starts your action server and NLU with the MessengerX connector in Docker

cd app

rasa run actions --actions actions&

# Start rasa server with nlu model
rasa run --model /app/models --enable-api \
        --cors "*" \
        --debug \
        --endpoints /app/endpoints.yml \
        --credentials /app/credentials.yml \
        --connector "MachaaoConnector.MachaaoInputChannel" \
        -p $PORT