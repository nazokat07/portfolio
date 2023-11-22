const url = 'http://127.0.0.1:8000/api/posts';
const posts = document.getElementById('posts');
let allposts = ''

fetch(url)
    .then(res => res.json())
    .then(data => {
        data.forEach(element => {
        allposts += `
        <div class="flex gap-10 border rounded-md p-5 w-max">
            <img class="bg-yellow-500 w-[150px]" src="${element.photo}" alt="">
            <div class="w-[60%]">
                <h1 class="text-3xl font-bold">Project title</h1>
                <p>${element.title}</p>
            </div>
        </div>`
        
        posts.innerHTML = allposts

        });
    })

{/*  */ }