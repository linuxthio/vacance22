class EBall
{
    constructor(x,y,parent)
    {
        this.x=x;this.y=y;
        this.r=12;
        this.w=this.r
        this.h=this.r
        this.degat=parseInt(Math.random()*5)+1
        
        this.parent=parent
        this.widget=document.createElement("div")
        this.widget.style.position='absolute'
        this.widget.style.backgroundColor="white"
        this.widget.style.borderRadius=50+"%"
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

    dehors(h) {
        if(this.y>h)    
        {
            return true;
        }
        return false
    }
    move(dx,dy,h)
    {
        if(this.y<h-60)
        {
            this.x=this.x+dx
            this.y=this.y+dy
            this.change_coord(this.x,this.y)
        }
    }

    hitShip(ship)
    {
        var ex=this.x>ship.x && this.x<ship.x+ship.w
        var ey=this.y>ship.y && this.y<ship.y+ship.h
        if (ex && ey)
        {
            if(ship.vie<=0)
            {
                ship.vie=0
            }else{

                ship.vie=ship.vie-this.degat
            }
            // enemies.remove(enemie)
        }
    }
}