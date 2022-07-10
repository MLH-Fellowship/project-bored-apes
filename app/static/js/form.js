var form = document.getElementById('form');
form.addEventListener('submit', function(e) {
    e.preventDefault();
    const payload = new FormData(form);
    fetch('api/timeline_post', {
    method: 'POST',
    body: new FormData(this)
    })
    .catch(error => {
        console.log("Error")
    })
    console.log("hi")
})