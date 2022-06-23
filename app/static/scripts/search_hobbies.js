function search(hobbies_obj,pics,memos){
    var text = document.getElementById("searchHobbies").value.toLowerCase();
    var names = [];
    var indexes = [];
    const filtered = {};

    for(var i = 0; i < Object.keys(hobbies_obj).length; i++){
        indexes.push(i);
        names.push(hobbies_obj[i].toLowerCase());
    }

    const result = names.filter(hobbie => hobbie.includes(text));

    var new_content = ""
    for(var i = 0; i < names.length; i++){
        for(var j = 0; j < result.length; j++){
            if(names[i] == result[j]){
                filtered[i] = result[j];
            }
        }
    }

    for(var i in filtered){
        new_content = new_content.concat(create_card(i,pics,hobbies_obj,memos))
    }

    document.getElementById('hobbies-container').innerHTML = new_content;
}

function create_card(key,pics,names,memos) {
    var text = "<div class = ' col-sm-12 col-lg-4'> \n\t <div class = 'card hobbies_shadowing margins'>" +
                "<img src = '"+pics[key]+"' class = 'hobbies-img'>\n\t"+
                "<div class = 'card-body'>"+
                "<h4 class = 'card-title'>"+names[key]+"</h4>"+
                "<p class = 'card-text'>"+memos[key]+"</p></div></div></div></div>"

    return text
}

