class Enemie
{
    constructor(x,y,parent)
    {
        this.x=x;this.y=y;
        this.r=30;
        this.w=60
        this.h=20
        this.parent=parent
        this.widget=document.createElement("div")
        this.widget.style.position='absolute'
        this.widget.style.backgroundColor="yellow"
        this.dx=Math.random()*10
        while(this.dx<5){
            this.dx=Math.random()*10 
        }
        this.change_coord(x,y)
        this.widget.style.width=this.w+"px"
        this.widget.style.height=this.h+"px"
    }
    show()
    {
        this.parent.appendChild(this.widget)
    }
    change_coord(a,b)    
    {
        this.x=a;this.y=b;
        this.widget.style.left=this.x+"px"
        this.widget.style.top=this.y+"px"
    }
    move(dy,w)
    {
        if (this.x <0 || this.x>w-60-Math.abs(this.dx))
        {            

            this.dx=-this.dx
        }
        this.x=this.x+this.dx
        this.y=this.y+dy
        this.change_coord(this.x,this.y)
    }

    shoot(gatling)
    {
        var a=Math.random()*2000

        if (a>1890 && a<1900)
        {
            gatling.push(new EBall(this.x,this.y,this.parent))
        }
    }

}