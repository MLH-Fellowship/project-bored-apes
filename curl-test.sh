#!/bin/bash

# Get random lorem ipsum content
content=$(curl -s http://asdfast.beobit.net/api/ | jq -r '.["text"]')

# Post data with name, email, and random lorem ipsum content
id=$(curl -s --request POST http://localhost:5000/api/timeline_post -d "name=Justin&email=justin.monteza@gmail.com&content=$(echo "$content")" | jq -r '.["id"]')

# Get the post we just added using its id
check=$(curl -s http://localhost:5000/api/timeline_post | jq -r '[.["timeline_posts"][] | .id] | @sh' | grep $id)

# Check must be non-empty
if [ "$check" ]
then 
    echo "Successfully added a timeline post with id $id"
# We cannot find the post, therefore it failed to add
else
    echo "Failed to add a timeline post"
fi

# Sends a delete request
curl -X DELETE http://localhost:5000/api/timeline_post/$id 