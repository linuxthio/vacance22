
function ranger(tb)
{
    let t=[]
    // tb.forEach(e => {
    //     t.push(e.toLowerCase());        
    // });

    for (var i=0;i<tb.length;i++)
    {
        t.push(tb[i].toLowerCase());
    }
    t=t.sort();
    return t
}

let tab=[]

let prenom=document.getElementById("prenom")
let aff=document.getElementById("aff")


function rranger()
{

    if (prenom.value.trim()!="")
    {

    tab.push(prenom.value)

    var recup=ranger(tab)

    aff.innerHTML=""

    for (var i=0;i<recup.length;i++)
    {
        aff.innerHTML=aff.innerHTML+"<p>"+recup[i]+"</p>"
        console.log(recup[i]);
    }
    prenom.value=""
    }
}

prenom.addEventListener("keydown",(e)=>{
    console.log(e.code)
    if(e.code=="Enter")
    {
        rranger();
    }
})


