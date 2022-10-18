let main=document.getElementById("main")

let w=window.screen.width
let h=window.screen.height


let gatling=[]
let enemies=[]

let w2=w/2
let h2=h/2

let LEVEL=10


let menu=new Menu(w2,100,"gamebaski",main)

function create_enemie(n)
  {
  for (i=0;i<n;i++)
  {
    var x=Math.random()*w
    var y=Math.random()*h2
    enemies.push(new Enemie(x,y,main))
  }
}

function getScreenSize(pas)
{
  var w=window.screen.width
  var h=window.screen.height
 
  var q1=0
  var r1=0
  var q2=0
  var r2=0
  
  q1=(w-w%pas)/pas
  q2=(h-h%pas)/pas
  
  var ws=q1*pas
  var hs=q2*pas
  return [[w,h],ws,hs]
  
}

var ww=getScreenSize(100)[1]
var hh=getScreenSize(100)[2]

let ship=new Ship(ww/2,hh-200,main)
function charger_gatling(n)
  {
  for (i=0;i<n;i++)
  {
    var x=Math.random()*w
    var y=Math.random()*h2
    
    gatling.push(new Ball(x,y,main))
  }
}


function clear_screen()
{
    main.style.width=getScreenSize(100)[1]+"px"
    main.style.height=(getScreenSize(100)[2]-100)+"px"
    main.style.marginLeft="50%"
    main.style.transform="translateX(-50%)"

    main.style.backgroundColor="blue"
}

console.log(getScreenSize(100))
clear_screen()

function openFullscreen(elem) {
    if (elem.requestFullscreen) {
      elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) { /* Safari */
      elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { /* IE11 */
      elem.msRequestFullscreen();
    }
  }

// openFullscreen(main)
ship.show();

window.addEventListener("keydown",(event)=>{
    console.log(event.key)
    var dx=100
    var dy=100
    if (event.key=="ArrowLeft")
    {
        ship.move(-dx,0,ww,hh)
    }else if (event.key=="ArrowRight")
    {
        ship.move(dx,0,ww,hh)

    }else if (event.key=="ArrowUp")
    {
        ship.move(0,-dy,ww,hh)

    }else if (event.key=="ArrowDown")
    {
        ship.move(0,dy,ww,hh)

    }else{
        console.log("ok")
    }
    // console.log(event.code)

},true)

function level()
{
  LEVEL=LEVEL+1
  var n=LEVEL*2
  create_enemie(n)
}

// charger_gatling(20)

function loop()
{
  // charger_gatling(1)
  if(enemies.length==0)
  {
    level()
  }
  gatling.forEach(function(e){
    e.move(0,5,hh)
    e.show()
    e.hitShip(ship)
  })
  enemies.forEach(function(e){
    e.move(0,ww)
    e.show()
    e.shoot(gatling)
  })

  menu.titre=""+gatling.length+" Vie: "+ship.vie
  ship.setInfo()
  menu.show(1)
  // ship.show()
  // ship.move(1,0)
  console.log("ok")
  requestAnimationFrame(loop)
}

loop()
