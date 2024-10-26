document.getElementById('loadDataBtn').addEventListener('click',() => {fetch('/api/data')
    .then(reponse => reponse.json())
    .then(data => {document.getElementById('content').innerText = JSON.stringify(data);
    })
    .catch(err => console.error('Error', err));
});