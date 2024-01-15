function like(slug, id) {
    var element = document.getElementById('like')
    var count = document.getElementById('count')
    $.get(`http://127.0.0.1:8000/blog/like/${slug}/${id}`).then(response => {
    if (response['response']==='liked'){
        element.style.color="red";
        count.innerText = Number(count.innerText)+1
    }else {
         element.style.color="white";
         count.innerText = Number(count.innerText)-1
    }
    })

}