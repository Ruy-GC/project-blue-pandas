window.onload = seePosts;

const form = document.getElementById('timeline-form');
const timeline = document.getElementById('timeline');


form.addEventListener('submit', function(e) {
    e.preventDefault();

    if(confirm("Are you sure, you want to add this new post?")){
        const payload = new FormData(form);
    
        fetch('/api/timeline_post', {
            method: 'POST',
            body:payload,
        })

        .then(res => res.json())
        .then(data => seePosts())

        form.reset();
    }
})


async function seePosts(){
    fetch('/api/timeline_post', {
        method: 'GET',
    })
    .then(res => res.json())
    .then(data => {

        var timelineItems = "";
        for(var i = 0; i < data.timeline_posts.length;i++){
            timelineItems += genItem(data.timeline_posts[i]);
        }

        document.getElementById("eventList").innerHTML = timelineItems;
    })
}

function genItem(item){
    return "<li class='list-inline-item event-list'>\n\t<div class='px-4'>\n\t <div class='event-date bg-soft-primary text-primary'>"+
    item['created_at']+
    "</div>\n\t"+"<h5 class='font-size-16'>"+ 
    item['name'] +
    "</h5>\n\t<h5 class='font-size-16'>"+
    item['email']+
    "</h5>\n\t<p class='text-muted'>"+
    item['content']+
    "</p>\n</div>\n </li>\n"
}

