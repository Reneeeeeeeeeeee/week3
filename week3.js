
let url= 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json';
fetch(url)
.then(function(response){
    return response.json();
}).then(function (data){
    const meterial=data["result"].results;
    let promo = document.querySelectorAll('.promo');
    let divpromo= document.createElement('div');
    var img= document.getElementById("img1");
    var img1= document.getElementById("img2");
    var photo8= document.querySelectorAll("#photo8");
    ///let eleimg= document.createElement("img");
    let content= document.querySelectorAll('.detail')
    let eletext= document.createElement('div')
    for(let i=0; i<2; i++){ 
        promo[i].textContent= meterial[i]['stitle'];
        promo[i].appendChild(divpromo); 
    }
    for(let z=2,y=0; z<10,y<8; z++,y++){
        content[y].textContent= meterial[z]['stitle'];
        content[y].appendChild(eletext);
        console.log(z,y)
         
    }
    var imgurl = meterial[0]['file'];
    img.src= imgurl.split("jpg")[0]+"jpg";
    var imgurl1 = meterial[1]['file'];
    img1.src= imgurl1.split("jpg")[0]+"jpg"
    for (let a=0,b=2; a<8,b<10; a++,b++){
        var photourl= meterial[b]['file'];
        photo8[a].src=photourl.split("jpg")[0]+"jpg";
    }
    
     
})
