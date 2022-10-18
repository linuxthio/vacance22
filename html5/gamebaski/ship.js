
class Ship
{
    constructor(x,y,parent)
    {
        this.x=x;this.y=y;
        this.r=30;
        this.w=100
        this.h=100
        this.vie=100
        this.parent=parent
        this.widget=document.createElement("div")
        this.widget.style.position='absolute'
        // this.widget.style.margin="0px"
        // this.widget.style.padding="0px"

        this.widget.style.backgroundColor="green"
        this.info=document.createElement("p")
        this.info.style.color="yellow"
        this.info.style.fontSize="32px"
        this.info.style.textAlign="center"
        this.info.innerHTML=this.vie
        this.widget.appendChild(this.info)

        this.change_coord(x,y)
        this.widget.style.width=this.w+"px"
        this.widget.style.height=this.h+"px"
    }

    setInfo()
    {
        this.info.innerHTML=this.vie
    }
    change_coord(a,b)    
    {
        this.x=a;this.y=b;
        this.widget.style.left=this.x+"px"
        this.widget.style.top=this.y+"px"

    }
    show()
    {
        // this.parent.innerHTML="x="+this.x+" : y="+this.y +"<p>"+this.widget.style.left+" :: "+this.widget.style.top+"</p>"
        this.parent.appendChild(this.widget)        
    }
    checkVie()
    {
        if(this.vie<=0){
            this.vie=0
            this.widget.removeChild(this.info)
            this.parent.removeChild(this.widget)
            this.widget.style.zIndex="-1000"
        }
    }

    move(dx,dy,w,h)
    {
        // this.parent.innerHTML="x="+this.x+" : y="+this.y +"<p>"+this.widget.style.left+" :: "+this.widget.style.top+"</p>"
        w=parseInt(this.parent.style.width.substr(this.parent.style.width.lenght-2))
        h=parseInt(this.parent.style.height.substr(this.parent.style.height.lenght-2))
        
        console.log("parse : w="+w+" h ="+h)

        if(this.vie==0 || this.vie<0)
        {
            this.info.display="none"
            this.widget.display="none"
            this.vie=0
            this.parent.removeChild(this.widget)
        }else
        {

            if(this.x>=0 && this.x<=w-100)
            {
                
                this.x=this.x+dx
                if (this.x<0)
                {
                    this.x=0
                }
                if (this.x>w-100)
                {
                    this.x=w-100
                }
            }
            if  (this.y>=0 && this.y<=h-100)
            {
            this.y=this.y+dy   
            if (this.y<0)
            {
                this.y=0
            } 
            if (this.y>h-100)
            {
                this.y=h-100
            }
            
        }
        this.change_coord(this.x,this.y)
        console.log("x="+this.x+" : y="+this.y)
        this.info.innerHTML=this.vie
    }
       
    }

    shoot(chargeur)
    {
        chargeur.push(new Ball(this.x ,this.y,this.parent))
    }
}