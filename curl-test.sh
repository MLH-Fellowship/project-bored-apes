
curl --request POST http://localhost:5000/api/timeline_post -d 'name=Hadi&email=chaabanhadi22@gmail.com&content=First email!'
wait
curl --request GET http://localhost:5000/api/timeline_post
