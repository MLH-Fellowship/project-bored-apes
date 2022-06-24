# Get random lorem ipsum

content=$(curl -s http://asdfast.beobit.net/api/ | jq -r '.["text"]')

# echo $content

# curl -s http://localhost:5000/api/timeline_post | jq -r '.["timeline_posts"][] | {id: .id}'

# curl -s http://localhost:5000/api/timeline_post | jq -r '[.["timeline_posts"][] | .id]' | grep 7

# Post Data
id=$(curl --request POST http://localhost:5000/api/timeline_post -d "name=Justin&email=justin.monteza@gmail.com&content=$(echo "$content")" | jq -r '.["id"]')

echo $id

# Get 
curl -s http://localhost:5000/api/timeline_post | jq -r '[.["timeline_posts"][] | .id] | @sh' | grep $id

# Sends a delete request
curl -X DELETE http://localhost:5000/api/timeline_post/$id

